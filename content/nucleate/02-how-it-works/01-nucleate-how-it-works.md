---
linkTitle: "Core behavior"
type: docs
weight: 2
slug: "core-behavior"
url: "/nucleate/how-it-works/core-background"
---
## How it works
### Nucleate
At its core, Nucleate transcribes audio files and automatically crystallizes the transcripts into useful project notes. It supports multiple layers of summarization—daily notes for short-term recall, and weekly or monthly rollups for longer-term tracking. By default, Nucleate handles tagging, organization, and synchronization, with optional integration into tools like Notion and Obsidian.

User customization is a core focus. Out of the box, you can choose from 20+ user modes tailored to different workflows, such as _Developer_, _Small Business_, or _Personal Journaling_. If none of those fit, you can create your own using the in-app **Mode Builder.** Customization extends beyond modes too—define your own tags, structure, and summary preferences, and choose which transcription or summarization models to use. Everything can run fully local, or optionally with OpenAI API support.

The goal is simple: once it’s set up, Nucleate works quietly in the background. For those seeking productivity, the experience is supposed to be like having a project manager in your back pocket. No file babysitting. No constant decisions. Just record, and let the system do the rest.

### Insights
Insights are optional, value-added analyses that sit _on top_ of your transcripts and summaries. They’re designed to extract higher-level structure—things like priorities, decisions, unresolved questions, or key takeaways—and append them cleanly to your notes.

Rather than forcing a one-size-fits-all output, Nucleate lets you decide how much structure you want. You can explicitly select which Insights appear in your daily, weekly, or monthly notes, or enable **Smart Insights**, which automatically chooses relevant analyses based on the content itself.

The intent is restraint, not noise. If you’re talking through bugs, planning work, or thinking out loud, Insights help surface what matters—without cluttering your notes with irrelevant metrics or filler.

### The Lab
Not everything fits neatly into an automated workflow. Sometimes you just want to experiment, explore, or summarize something once.

The Lab is Nucleate’s sandbox. It supports manual transcription, one-off summarization, and adaptive prompting without affecting your core setup. Whether you’re breaking down a podcast, analyzing a lecture, summarizing an article, or testing a new model or prompt style, the Lab gives you a place to do that safely.

There are 20+ Lab profiles included out of the box, and you can create your own. Mix user modes, models, and Insights freely—it’s a space designed for experimentation, creativity, and “what if” scenarios.

### Behind the scenes
Behind the scenes, Nucleate follows a predictable pipeline: **file detection → transcription → summarization → synchronization**. The system is designed to be deterministic and recoverable, so content can be rebuilt or adjusted without breaking your workflow.

#### New audio files + daily content

When a new audio file appears in the _Incoming Audio_ folder, transcription begins immediately using your selected models and settings. Once transcription completes, optional speaker detection is performed and the transcript is segmented by speaker and timestamp (speaker detection is only available when transcription runs locally).

A cached copy of the transcript is stored inside the app, and the original audio file is moved to your designated _Archive_ folder.

Any transcript that does not yet have a matching summary automatically enters the summarization stage. The transcript is split into smaller sections, pre-processed, and summarized using your active user mode. The resulting summary, along with the raw transcript, is then passed through the optional Insights layer.

If **Smart Insights** are enabled, Nucleate evaluates the content and selects the most relevant analyses automatically. If Smart Insights are disabled, only the Insights you’ve explicitly enabled are applied.

The final markdown output—core summary plus Insights—is cleaned up during post-processing, optionally tagged, cached in-app, synchronized to your folders, and, if configured, pushed to Notion.

#### Weekly and monthly content

On a weekly or monthly cadence, Nucleate reviews all newly generated markdown content from the previous period. Daily or weekly summaries are parsed and aggregated before being passed into the corresponding weekly or monthly model.

These higher-level summaries follow the same pipeline as daily content: summarization, optional Insights, post-processing, and synchronization. The intent is to surface patterns, trends, and long-term progress rather than repeat day-to-day detail.

#### Rewriting and deleting

If a summary isn’t quite right, Nucleate includes tools to rebuild or remove it cleanly. Using the **File Sync / Summary Rebuild and Deletion** interface, you can regenerate a summary using your current user mode and settings.

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