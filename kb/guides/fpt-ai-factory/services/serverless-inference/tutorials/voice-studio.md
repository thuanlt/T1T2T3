# Voice Studio (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/fpt-ai-factory/services/serverless-inference/tutorials/voice-studio/

# Voice Studio

Voice Studio is the Text-to-Speech tool in the Serverless Inference section. Enter Vietnamese text, choose a model and voice settings, then receive an audio file you can play back, download, or share via URL.

Voice Studio is suitable for:

  * Previewing voice quality before integrating the API into a product.
  * Quickly generating audio files for short content (announcements, prompts, demos).
  * Comparing results across different models, voices, and settings.

* * *

## 1\. Access Voice Studio​

  1. Sign in to FPT AI Factory.
  2. In the top bar, confirm the correct **Organization / Project** (e.g. `BigDream / AI Research Lab`). Usage costs will be charged to this project.
  3. In the left menu, go to **FPT Token Factory → Serverless Inference → Voice Studio**.

* * *

## 2\. Screen layout​

The screen is divided into 3 main areas:

Area| Position| Function| **Configuration (Model & Settings)**| Left column| Select model, output format, voice, speed, and advanced parameters| **Text input & Result**| Center column| Enter text, run conversion, listen to and download results| **History**|  Right column| List of runs in the past 24 hours  
---|---|---  
  
Two utility buttons appear in the top-right corner:

  * **Get API Keys** — go to the API Key management page to integrate TTS into your application.
  * **View Code** — view sample code for calling the API with the current configuration.

* * *

## 3\. Choose a model​

Under **Model** (left column), choose one of two models. The unit price is shown below the selector.

| FPT.TTS-pro| FPT.TTS-ultra| Displayed price| $16.5 / 1M characters| $99 / 1M characters| Voice selection| Direct selection from the **Voice** list| Via **Mode** and the **Advanced** group| Advanced parameters| No| Yes (Language, Num steps, Guidance scale)| Common options| Response format, Speed| Response format, Speed  
---|---|---  
  
note

When you switch models, the **Settings** section below updates accordingly.

* * *

## 4\. Configure FPT.TTS-pro​

This is the simpler model, suitable for quickly selecting an available voice.

Field| Description| Sample value| **Response format**|  Audio file format returned| MP3| **Voice**|  Reading voice. Each voice lists region and gender (North/Central/South · Male/Female). The selected voice has a ✓ mark| Viet Khoa · North · Male| **Speed**|  Reading speed| 1x  
---|---|---  
  
**Steps:**

  1. Select **Model = FPT.TTS-pro**.
  2. Select **Response format**.
  3. Open the **Voice** list and select the voice matching your desired region and gender.
  4. Select **Speed** (1x is standard speed).
  5. Proceed to enter text (section 6).

* * *

## 5\. Configure FPT.TTS-ultra​

This model allows deeper customization of voice quality and generation.

Field| Description| Default| **Response format**|  Audio file format returned| MP3| **Mode**|  Voice selection mode. `Auto` lets the system choose the best voice| Auto| **Advanced** (expandable group)| Advanced parameters below| —| → **Language**|  Language of the text. Leave blank for automatic detection| —| → **Num steps**|  Number of audio generation steps. Higher = better quality but slower processing| 32| → **Guidance scale**|  How closely the audio follows the text/voice characteristics| 2.0| → **Reset to default**|  Reset all Advanced parameters to default values| —| **Speed**|  Reading speed| 1x  
---|---|---  
  
**Steps:**

  1. Select **Model = FPT.TTS-ultra**.
  2. Select **Response format**.
  3. Select **Mode**. For new users, keep `Auto`.
  4. (Optional) Click **Advanced** to expand the advanced parameter group: 
     * Keep defaults for the first run.
     * For higher quality, increase **Num steps** (expect longer processing time).
     * If results are unsatisfactory, click **Reset to default** to restore the original configuration.
  5. Select **Speed**.
  6. Proceed to enter text (section 6).

**Tuning tips:**

Goal| Adjustment| Quick preview, prioritize speed| Decrease **Num steps**|  Highest quality for final output| Increase **Num steps** , keep **Guidance scale** at default| Output sounds unnatural or drifts| Click **Reset to default** , then adjust one parameter at a time  
---|---  
  
* * *

## 6\. Enter text and run conversion​

  1. Enter or paste content into the **Text input** field (required, marked with `*`).
  2. Monitor the character counter in the bottom-left of the input area, e.g. `266/5000 characters`. **Maximum 5,000 characters per run.**
  3. Use **Clear** (top-right of the input area) to delete all content.
  4. Click **Run**.

The system processes and displays the result in the **Result** area below.

note

  * Use correct punctuation so the voice pauses naturally.
  * For text longer than 5,000 characters, split into multiple segments and run separately.
  * Costs are calculated based on the number of characters sent.

* * *

## 7\. View and use results​

The **Result** area shows:

  * **Audio player** — click ▶ to listen, drag the progress bar to seek. Duration is shown on the right.
  * **Recording info** — Format, Voice, Speed, Duration (also summarized in the top-right corner, e.g. `MP3 · Viet Khoa · 1x`).
  * **Three action buttons:**

Button| Function| **Download MP3**|  Download the audio file to your device| **Copy URL**|  Copy the direct link to the audio file| **Open in new tab**|  Open the audio file in a new browser tab  
---|---  
  
warning

**Audio links expire.** The blue notification below the buttons shows the expiry time (e.g. _Audio link is available until 10:12 10/09/2026_). Download or copy the URL before that time.

* * *

## 8\. History​

The right column saves recent runs.

  * **Retention period:** 24 hours. Records are automatically deleted after that.
  * **Search:** type in the **Search history…** field to filter by text content.
  * **Each record** shows the beginning of the text, voice, speed, and time of run, with 3 buttons: ▶ play, ⬇ download, 🗑 delete.
  * **Pagination:** navigate with ‹ › arrows, adjust records per page (default `5 / page`).
  * **Clear all:** delete the entire history.

note

History is private to you within the current project and does not replace long-term storage. **Download** any files you need to keep.

* * *

## 9\. API integration​

After finalizing your configuration:

  1. Click **View Code** to get sample code for calling the API with the exact model and parameters selected.
  2. Click **Get API Keys** to create or copy your API Key (**Serverless Inference → API Keys** menu).
  3. Monitor quota limits and usage at **User quotas** and **Usage** in the same menu.

* * *

## 10\. FAQ​

**Why is there no Voice selector when using FPT.TTS-ultra?** FPT.TTS-ultra selects voices via **Mode** (default `Auto`) and the **Advanced** group, rather than a fixed Voice list like FPT.TTS-pro.

**The Run button is greyed out / won't run?** Check that the **Text input** field has content and does not exceed 5,000 characters.

**Audio link says expired?** Re-run from **History** (if still within 24 hours) or re-run with the same text. Going forward, **Download** immediately after generating.

**Processing is slow with FPT.TTS-ultra?** Decrease **Num steps** in the **Advanced** group or shorten the text.

**How are costs calculated?** By the number of characters submitted, at the unit price shown below the Model selector. See **Pricing** or **Usage** for details.
