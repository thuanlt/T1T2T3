"""Client gọi LLM qua API tương thích OpenAI (chat + embeddings)."""
from __future__ import annotations

import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)


class LLMError(RuntimeError):
    pass


class LLMClient:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str,
        chat_model: str,
        embed_model: str,
        timeout: float = 60.0,
        verify_ssl: bool = True,
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.chat_model = chat_model
        self.embed_model = embed_model
        self.timeout = timeout
        self._client = httpx.Client(timeout=timeout, verify=verify_ssl)

    @property
    def available(self) -> bool:
        return bool(self.api_key)

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

    def chat(self, messages: list[dict[str, str]], *, temperature: float = 0.2, max_tokens: int = 600, model: str | None = None) -> str:
        if not self.available:
            raise LLMError("LLM chưa được cấu hình (thiếu LLM_API_KEY)")
        for attempt in range(2):
            payload: dict[str, Any] = {
                "model": model or self.chat_model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens * (attempt + 1),
            }
            try:
                resp = self._client.post(f"{self.base_url}/chat/completions", headers=self._headers(), json=payload)
                resp.raise_for_status()
                data = resp.json()
                content = data["choices"][0]["message"].get("content")
                if content and content.strip():
                    return content.strip()
                logger.warning(
                    "Chat API trả content rỗng (attempt %d, max_tokens=%d), retry với budget lớn hơn",
                    attempt + 1,
                    max_tokens * (attempt + 1),
                )
            except httpx.HTTPStatusError as exc:
                logger.error("Chat API HTTP %s: %s", exc.response.status_code, exc.response.text[:300])
                raise LLMError(f"Chat API lỗi HTTP {exc.response.status_code}") from exc
            except (httpx.HTTPError, KeyError, IndexError) as exc:
                logger.error("Chat API lỗi: %s", exc)
                raise LLMError(f"Chat API lỗi: {exc}") from exc
        raise LLMError("Model không trả về nội dung (content rỗng sau khi retry)")

    def embed(self, texts: list[str]) -> list[list[float]]:
        if not self.available:
            raise LLMError("LLM chưa được cấu hình (thiếu LLM_API_KEY)")
        if not texts:
            return []
        payload = {"model": self.embed_model, "input": texts}
        paths = ["/embeddings", "/v1/embeddings"]
        last_err: Exception | None = None
        for attempt in range(3):
            for path in paths:
                try:
                    resp = self._client.post(f"{self.base_url}{path}", headers=self._headers(), json=payload)
                    if resp.status_code == 404 and path != paths[-1]:
                        continue
                    resp.raise_for_status()
                    data = resp.json()
                    items = sorted(data["data"], key=lambda it: it["index"])
                    return [it["embedding"] for it in items]
                except httpx.HTTPStatusError as exc:
                    last_err = exc
                    logger.warning(
                        "Embed API %s HTTP %s (attempt %d): %s",
                        path,
                        exc.response.status_code,
                        attempt + 1,
                        exc.response.text[:200],
                    )
                except (httpx.HTTPError, KeyError, IndexError) as exc:
                    last_err = exc
                    logger.warning("Embed API %s lỗi (attempt %d): %s", path, attempt + 1, exc)
            if attempt < 2:
                import time

                time.sleep(1.5 * (attempt + 1))
        raise LLMError(f"Embed API lỗi: {last_err}") from last_err

    def systemone(self, model: str, message: str, questions: dict) -> dict:
        """Gọi /v1/systemone (FPT Quyet) — quyết định có cấu trúc. Trả về dict answers."""
        if not self.available:
            raise LLMError("LLM chưa được cấu hình (thiếu LLM_API_KEY)")
        payload = {
            "model": model,
            "state": {"message": message},
            "questions": questions,
        }
        try:
            resp = self._client.post(f"{self.base_url}/v1/systemone", headers=self._headers(), json=payload)
            resp.raise_for_status()
            data = resp.json()
            answers = data.get("answers")
            if not answers:
                raise LLMError("systemone trả về answers rỗng")
            return answers
        except httpx.HTTPStatusError as exc:
            logger.error("SystemOne API HTTP %s: %s", exc.response.status_code, exc.response.text[:300])
            raise LLMError(f"SystemOne API lỗi HTTP {exc.response.status_code}") from exc
        except (httpx.HTTPError, KeyError, IndexError) as exc:
            logger.error("SystemOne API lỗi: %s", exc)
            raise LLMError(f"SystemOne API lỗi: {exc}") from exc

    def generate_image(self, prompt: str, model: str | None = None, *, size: str = "1024x1024") -> str:
        """Gọi images/generations, trả về URL ảnh (hoặc chuỗi base64 nếu không có URL)."""
        if not self.available:
            raise LLMError("LLM chưa được cấu hình (thiếu LLM_API_KEY)")
        payload = {"model": model or self.chat_model, "prompt": prompt, "n": 1, "size": size}
        try:
            resp = self._client.post(f"{self.base_url}/images/generations", headers=self._headers(), json=payload)
            resp.raise_for_status()
            data = resp.json()
            item = data["data"][0]
            if item.get("url"):
                return item["url"]
            if item.get("b64_json"):
                return "data:image/png;base64," + item["b64_json"]
            raise LLMError("Response image không có url/b64_json")
        except httpx.HTTPStatusError as exc:
            logger.error("Image API HTTP %s: %s", exc.response.status_code, exc.response.text[:300])
            raise LLMError(f"Image API lỗi HTTP {exc.response.status_code}") from exc
        except (httpx.HTTPError, KeyError, IndexError) as exc:
            logger.error("Image API lỗi: %s", exc)
            raise LLMError(f"Image API lỗi: {exc}") from exc

    def chat_with_image(
        self,
        prompt: str,
        image_url: str,
        *,
        system: str | None = None,
        model: str | None = None,
        max_tokens: int = 600,
    ) -> str:
        """Chat completions kèm ảnh (chuẩn OpenAI multimodal)."""
        if not self.available:
            raise LLMError("LLM chưa được cấu hình (thiếu LLM_API_KEY)")
        user_content = [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": image_url}},
        ]
        messages: list[dict] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": user_content})
        payload = {
            "model": model or self.chat_model,
            "messages": messages,
            "max_tokens": max_tokens,
        }
        try:
            resp = self._client.post(f"{self.base_url}/chat/completions", headers=self._headers(), json=payload)
            resp.raise_for_status()
            data = resp.json()
            content = data["choices"][0]["message"].get("content")
            if content and content.strip():
                return content.strip()
            raise LLMError("Model trả về content rỗng")
        except httpx.HTTPStatusError as exc:
            logger.error("Vision API HTTP %s: %s", exc.response.status_code, exc.response.text[:300])
            raise LLMError(f"Vision API lỗi HTTP {exc.response.status_code}") from exc
        except (httpx.HTTPError, KeyError, IndexError) as exc:
            logger.error("Vision API lỗi: %s", exc)
            raise LLMError(f"Vision API lỗi: {exc}") from exc

    def close(self) -> None:
        self._client.close()