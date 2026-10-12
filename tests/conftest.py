import os
import tempfile
from pathlib import Path

_TMP = tempfile.mkdtemp(prefix="fpt-agent-test-")
os.environ["DB_PATH"] = os.path.join(_TMP, "test.db")
os.environ["LLM_API_KEY"] = ""
os.environ["KB_DIR"] = str(Path(__file__).resolve().parent.parent / "kb")
os.environ["KEYWORD_CONF_THRESHOLD"] = "0.05"
os.environ["LOW_CONF_THRESHOLD"] = "0.02"

import pytest  # noqa: E402

from app import db  # noqa: E402

DB_PATH = os.environ["DB_PATH"]


@pytest.fixture(autouse=True)
def clean_db():
    db.init_db(DB_PATH)
    with db.db_session(DB_PATH) as conn:
        conn.execute("DELETE FROM tickets")
        conn.execute("DELETE FROM chunks")
    yield