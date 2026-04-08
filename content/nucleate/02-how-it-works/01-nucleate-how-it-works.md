---
linkTitle: "Core behavior"
type: docs
weight: 2
slug: "core-behavior"
url: "/nucleate/how-it-works/core-background"
---
## How it works
### Nucleate
At its core, Nucleate automatically transcribes audio files and distills the transcripts into useful project notes. It supports multiple layers of summarization—daily notes, and weekly or monthly rollups for longer-term tracking. By default, Nucleate handles tagging, organization, and synchronization, with optional integration into tools like Notion and Obsidian.

User customization is a core focus of Nucleate. Out-of-the-box, you can choose from 20+ user modes tailored to different workflows, such as _Developer_, _Small Business_, or _Personal Journaling_. If none of those fit, you can build your own! There are in-app functions that allow you to design your own user modes, set your own tags, and customize summary preferences/content. You can also set preferred transcription and summarization models, keeping everything private and local to your machine or by making use of OpenAI API support.

The experience is supposed to be like having a project manager in your back pocket, someone who works in the background and doesn't require handholding. Once set-up, Nucleate is designed to support a smooth, autonomous workflow without the need for file management, tracking, etc. Just set it up and let it rip.

### Insights
Insights are optional, value-added analyses that sit _on top_ of transcripts and summaries. They’re designed to extract higher-level structure—things like priorities, decisions, unresolved questions, or key takeaways—and append them cleanly to your notes.

Rather than forcing a one-size-fits-all output, Nucleate lets you decide how much structure you want. You can explicitly select which Insights appear in your daily, weekly, or monthly notes, or enable **Smart Insights**, which automatically chooses relevant topics based on the content itself. I exclusively use Smart Insights to allow for automatic content analysis.

The whole point of having Insights is to help surface critical content and to give choice to the user what kind of material gets floated upwards. Not all Insights are useful for all kinds of users. I personally use Nucleate to monolog and have no particular use for diarized, speaker-aware notes. The best approach is to tune, test, and rebuild summaries until you find something that suits your needs.

### The Lab
Not everything fits neatly into an automated workflow. During development, I occasionally needed to summarize individual files that were separate from the core Nucleate backend. To prevent disrupting the automated workflow, I built-in secondary functionality for manual transcription and "Custom" summaries.

The Lab is Nucleate’s sandbox. It supports manual transcription, one-off summarization, and quick prompt development without affecting the core setup. Whether you’re summarizing a podcast, analyzing a lecture, condensing an article, or testing a new model or prompt style, the Lab gives you a place to do that safely.

There are 20+ Lab profiles included out of the box, and you can create & test your own. Mix user modes, models, and Insights freely—it’s a space designed for experimentation and one-off cases.

### Behind the scenes
Behind the scenes, Nucleate follows a pretty straightforward pipeline: **file detection → transcription → summarization → synchronization**. The system is designed to be deterministic and recoverable, so content can be rebuilt or adjusted without breaking your workflow.

#### New audio files + daily content

The pipeline starts with audio. You can either record in-app or figure out your own means of depositing new audio files into the  _Incoming Audio_ folder.

When a new audio file is detected, transcription begins immediately using your selected models and settings. Once transcription completes, optional speaker detection is performed and the transcript is segmented by speaker and timestamp (speaker detection is only available when transcription runs locally).

A cached copy of the transcript is stored inside the app, and the original audio file is moved to your designated _Archive_ folder.

Any transcript that does not yet have a matching summary automatically enters the summarization stage. The transcript is split into smaller sections, pre-processed, and summarized using your active user mode. The resulting summary, along with the raw transcript, is then passed through the optional Insights layer.

If **Smart Insights** are enabled, Nucleate evaluates the content and automatically selects the most relevant Insights. If Smart Insights are disabled, only the Insights you’ve explicitly enabled are applied.

The final markdown output—core summary & Insights—is cleaned up during post-processing, optionally tagged and cached in-app. The new summary is synchronized to your user folders, and, if configured, pushed to Notion. The cached version of the summary can be viewed in-app on the _Summaries_ panel.

#### Weekly and monthly content

On a weekly or monthly cadence, Nucleate reviews all newly generated markdown content from the previous period. Daily or weekly summaries are parsed and aggregated before being passed into the corresponding weekly or monthly model.

These higher-level summaries follow the same pipeline as daily content: summarization, optional Insights, post-processing, and synchronization. The intent is to surface patterns, trends, and long-term progress.

#### Rewriting and deleting

If a summary isn’t quite right, Nucleate includes tools to rebuild or remove it cleanly. Using the **Summaries** panel, you can regenerate a summary using your current user mode and settings.

You can also permanently delete a summary and its associated transcript. This does _not_ delete the original audio file, but it prevents the content from being reprocessed or re-synchronized.

{{< callout type="info" >}}  
Deleting a markdown file directly from your user directory (via Windows Explorer or macOS Finder) is not permanent. Nucleate will detect the missing file and restore it from cached data. To permanently delete content, you must do so from within the app.  
{{< /callout >}}

### Status indicators
Too much desktop clutter? Nucleate can be optionally toggled to run in the background as part of your system tray. Keep an eye on the tray status indicators to see what's going on.

<div style="display: flex; gap: 100px; text-align: center;">
    <div>
        <div>Disabled</div>
        <img src="/images/scribe_idle.ico" alt="Idle" style="max-width: 50px; height: auto;">
    </div>
    <div>
        <div>Enabled</div>
        <img src="/images/scribe_active.ico" alt="Active" style="max-width: 50px; height: auto;">
    </div>
    <div>
        <div>Processing</div>
        <img src="/images/scribe_busy.ico" alt="Busy" style="max-width: 50px; height: auto;">
    </div>
    <div>
        <div>Downloading</div>
        <img src="/images/scribe_downloading.ico" alt="Download" style="max-width: 50px; height: auto;">
    </div>
</div>

| **Status**         | **Behavior**                                               |
|--------------------|------------------------------------------------------------|
| **Disabled**       | Disabled and idle                                          |
| **Enabled**        | Enabled and watching for new files                         |
| **Processing**     | Actively transcribing, summarizing, or uploading something |
| **Downloading**    | Downloading an Ollama LLM or transcription model           |