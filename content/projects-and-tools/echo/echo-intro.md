---
linkTitle: "How it works"
type: docs
weight: 2
draft: true
---
## How Echo works
### Core functionality
At it's core, Echo automatically transcribes audio files and distills the transcripts into useful project notes. There are multiple layers of summarization that allow for short term notes (i.e. daily) and for longer-term tracking (i.e. weekly/monthly). By default, Echo is equipped to support file tagging, synchronization, and integration with both Notion and Obsidian apps.

User customization is a core focus of Echo. Out-of-the-box, you can select user modes that are optimized to different kinds of tracking, such as "Developer," "Small Business," or "Personal Journaling." If none of those fit your needs, you can build your own! There are in-app functions that allow you to design your own user modes, set your own tags, and customize summary preferences/content. You can also set preferred transcription and summarization models, keeping everything private and local to your machine with or by making use of OpenAI models.

The experience is supposed to be like having a project manager in your back pocket, someone who works in the background and doesn't require handholding. Once set-up, Echo is designed to support a smooth, autonomous workflow without the need for file management, tracking, etc. Just set it up and let it rip.

### Custom prompts
During development, I occasionally needed to summarize individual files that were separate from the core Echo experience. To prevent disrupting the automated workflow, I built-in secondary functionality for "Custom summaries" and "Custom prompts." These functions are designed to enable lightweight, flexible prompting and manual summarization events. Want to summarize a podcast or news broadcast? What about a science article, a college lecture, or maybe a bedtime story?

By adding custom prompting, Echo can support the "what if" or "one off" cases. There are 10 different profiles out-of-the-box, but of course you can add your own! Write your own prompts and pick from local or OpenAI LLMs.

### Status indicators
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
        <div>Busy</div>
        <img src="/images/scribe_busy.ico" alt="Busy" style="max-width: 50px; height: auto;">
    </div>
    <div>
        <div>Download</div>
        <img src="/images/scribe_downloading.ico" alt="Download" style="max-width: 50px; height: auto;">
    </div>
</div>

| **Status**   | **Behavior**                                             |
|--------------|----------------------------------------------------------|
| **Disabled** | Echo is disabled and idle                                |
| **Enabled**  | Echo is enabled and watching for new files               |
| **Busy**     | Echo is actively transcribing, summarizing, or uploading |
| **Download** | Echo is downloading a LLM or transcription model         |

### Echo logic and behavior