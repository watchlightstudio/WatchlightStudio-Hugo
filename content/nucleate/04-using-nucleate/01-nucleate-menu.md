---
linkTitle: "Navigate"
type: docs
weight: 1
slug: "menu"
---
## Menu Details & Help
### Status indicators
<details>
<summary>Nucleate hub status</summary>
<div style="display: flex; gap: 68px; text-align: center;">
    <div>
        <div>Disabled</div>
        <img src="/images/idle.gif" alt="Idle" style="max-width: 125px; height: auto;">
    </div>
    <div>
        <div>Enabled</div>
        <img src="/images/active.gif" alt="Active" style="max-width: 125px; height: auto;">
    </div>
    <div>
        <div>Processing</div>
        <img src="/images/busy.gif" alt="Busy" style="max-width: 125px; height: auto;">
    </div>
    <div>
        <div>Downloading</div>
        <img src="/images/downloading.gif" alt="Download" style="max-width: 125px; height: auto;">
    </div>
</div>

| **Status**         | **Nucleate Behavior**                                        |
|--------------------|--------------------------------------------------------------|
| **Disabled**       | Disabled and idle                                            |
| **Enabled**        | Enabled and watching for new files                           |
| **Processing**     | Actively transcribing, summarizing, or uploading (if OpenAI) |
| **Downloading**    | Downloading an Ollama LLM or transcription model             |
</details>

<details>
<summary>Tray status status</summary>

<div style="display: flex; gap: 125px; text-align: center;">
    <div>
        <div>Disabled</div>
        <img src="/images/scribe_idle.ico" alt="Idle" style="max-width: 75px; height: auto;">
    </div>
    <div>
        <div>Enabled</div>
        <img src="/images/scribe_active.ico" alt="Active" style="max-width: 75px; height: auto;">
    </div>
    <div>
        <div>Processing</div>
        <img src="/images/scribe_busy.ico" alt="Busy" style="max-width: 75px; height: auto;">
    </div>
    <div>
        <div>Downloading</div>
        <img src="/images/scribe_downloading.ico" alt="Download" style="max-width: 75px; height: auto;">
    </div>
</div>

{{< callout type="info" >}}  
If Nucleate system tray settings are enabled, the tray app icon will update based on current backend activities.
{{< /callout >}}

</details>

### In-app panels
<details>
<summary>Hub</summary>
<img src="/menu/hub.png">

### Hub Overview

The Hub is your central dashboard in Nucleate, providing status, control, and quick access to key settings.

1. **Enable Nucleate**
    - Click a card to enable or disable automatic services.
    - Status indicators show whether each service is active, idle, or using OpenAI.
        
2. **Message Board**
    - Displays key events, alerts, and messages from Nucleate.
    - Provides real-time updates on processing, errors, and completed tasks.
        
3. **Quick Access Cards**
    - Navigate directly to **User Mode Settings**, **AI Settings**, or **Ollama Models**.
        
4. **Recording Controls**
    - Start or stop in-app recording.
    - Maximum recording: 30 minutes for Lite users, unlimited for Pro users.
    - Adjust maximum limits in **AI Advanced Settings**.
        
5. **Service Status Indicators**
    - Shows whether Nucleate is operating fully locally (private) or using OpenAI APIs.
        
6. **Third-Party / Integration Status**
    - Check connectivity and status for integrated services like Notion or OpenAI.
        
7. **Tray Behavior Toggle**
    - Keep Nucleate running in the system tray when the main GUI is closed.

</details>

<details>
<summary>Modes</summary>
<img src="/menu/user_modes.png">

### User Modes

Select, customize, and fine-tune how Nucleate interprets your audio. Switch between **Default** and **Custom** modes, edit which Insights are enabled, and control tagging and transcript behavior. Advanced users can adjust daily, weekly, and monthly preferences to create a workflow tailored to your needs.

1. **Mode selection**  
    Choose between **Default** and **Custom** modes. Modes created via the **Mode Builder** appear under the "Custom" tab.
    
2. **Pick a mode**  
    Select a specific mode from the dropdown menu. A description of the selected mode is shown below.
    
3. **Enabled content**  
    View the content enabled for the selected mode. Adjust which items are active via **Mode Preferences**.
    - **Smart Insights** automatically override other Insights.     
    - **Tags** and **Transcripts** are always enabled.

<img src="/menu/user_mode_preferences.png">

### Mode Insights

1. **Favorite Insights**  
    Favorites appear at the top of the list. Right-click to add or remove items.
    
2. **Enable Insights**  
    Choose which Insights are applied to **Daily**, **Weekly**, or **Monthly** summaries. Smart Insights will override other selections. Tags and Transcripts remain enabled regardless.
    
<img src="/menu/user_mode_preferences_2.png">

1. **Transcripts**  
    Optional for Daily summaries. Weekly and Monthly summaries digest Daily content, so transcripts remain disabled.
    
2. **Diarized Insights**  
    Require **Speaker Detection** in **AI Settings**. Available only for Daily summaries, since diarized transcripts are needed.

<img src="/menu/tag_files.png">

### Tagging Files
1. **Apply tags**  
	Tag any markdown file using the active user mode’s tag list.
	
2. **Batch selection**  
	Select one or multiple files to automatically apply the current tags.

</details>

<details>
<summary>AI settings</summary>
<img src="/menu/ai_engine_settings.png">

### AI / LLM Settings

This panel controls how Nucleate performs **summarization, transcription, and speaker detection**, and how those workloads are split between **local hardware** and **OpenAI services**.

Settings here are adaptive: available options update automatically based on detected hardware, enabled features, and selected backends.

1. #### Summarization services
	- Each summary type can be configured to use either:
	    - **Local models (Ollama)**, or
	    - **OpenAI API services**
	- You can freely mix local and cloud summarization depending on your workflow

2. **Local summarization**
	- Uses the currently selected Ollama model
	- The active model is shown here for reference
	- To change models, see **Ollama Backend** settings

3. **OpenAI summarization**
	- When at least one summarizer is set to OpenAI, additional options become available
	- Select from predefined OpenAI models or enter a custom model name manually
	
	{{< callout type="info" >}}  
	Local summarization is fully offline and private. OpenAI summarization uploads text to OpenAI’s servers and incurs usage-based costs.  
	{{< /callout >}}

4. #### Transcription services
	- Choose how audio is transcribed:
	    - **CPU**
	    - **GPU / MPS** (hardware accelerated)
	    - **OpenAI**
	- Available options are restricted automatically based on detected hardware

5. **Transcription backend**
	- **Faster-Whisper** (recommended for most users)
	    - Optimized for speed and efficiency
	    - Best choice for Windows and CPU-based workflows
	- **Whisper**
	    - Preferred on Apple Silicon Macs due to native Metal acceleration

6. **Transcription model**
	- Select from available Whisper model sizes
	- **Medium** is recommended by default when adequate hardware is detected
	- Larger models improve accuracy but require more RAM/VRAM and time
	
	{{< callout type="info" >}}  
	Because Nucleate performs summarization on transcripts, minor transcription errors are often corrected or ignored during analysis. Medium-sized models typically provide the best balance.  
	{{< /callout >}}
	
	**OpenAI transcription**
	- Uses OpenAI’s Whisper API
	- Audio files are uploaded to OpenAI for processing
	
	{{< callout type="warning" >}}  
	OpenAI transcription can become expensive for long recordings or large backlogs.  
	{{< /callout >}}

7. #### Diarization (speaker detection)
	- Select diarization compute:
	    - **CPU**
	    - **GPU** (when supported)
	
	- Diarization is **not compatible** with OpenAI transcription    
	- To enable these options:
	    - Ensure **Speaker Detection** is enabled in the AI Settings panel

8. #### Live memory & hardware state
	Real-time visibility into system resources:
	- **VRAM / Unified Memory** (Apple Silicon)
	- **System RAM**
	- Memory usage unrelated to Nucleate is shown in grey

	**Usage indicators**
	
	- Persistent usage reflects loaded Ollama models (when Overdrive is enabled)  
	- Peak usage represents additional memory allocated during:
		- Transcription
		- Diarization
		- Ollama inference (when models are not pinned in memory)
	
	These indicators help you understand performance limits, diagnose slowdowns, and tune model selection for your hardware.

<img src="/menu/ollama_settings.png">

### Ollama Model Selection

This panel controls which Ollama model Nucleate uses for local summarization and analysis.

Nucleate ships with a curated list of **preloaded** model selections, and also allows you to specify a **custom Ollama model name** if you want to experiment or bring your own.

1. **Model selection**
	- Choose from detected local models or select a recommended model from the preset list
	- You may also enter a custom model name manually (for example: `deepseek-r1`, `mixtral`, `llama2`, etc.)
	- Custom entries must exactly match a valid model listed on the Ollama model registry

**Model detection & status**
	- Nucleate checks Ollama connectivity in real time
	- The status indicator shows:
	    - Whether Ollama is reachable
	    - Whether the selected model is installed locally
	    - Whether the model is valid and usable
	- If a selected model is not yet installed, Nucleate will prompt before downloading it

**Downloads**
	- Model downloads are handled directly by Ollama
	- Third-party downloads always require explicit user approval
	- Download progress and completion status are surfaced in the UI

{{< callout type="info" >}}  
By default, Nucleate recommends **Mistral 7B**, which has consistently produced the best balance of quality, speed, and hardware compatibility during development and testing. It is relatively lightweight compared to many alternatives and runs well on most supported systems.  
{{< /callout >}}

<img src="/menu/diarization_settings.png">

### Advanced features

These options provide **direct control over Nucleate’s core processing pipeline**. They are optional, but can significantly affect performance, output quality, and available features.

Advanced features are available to **Nucleate Pro users**, provided the system meets the relevant compatibility requirements.

1. #### Ollama Overdrive
	Ollama Overdrive keeps the active local summarization model **persistently loaded in memory** (VRAM or system RAM, depending on configuration).
	
	By avoiding repeated model load and unload cycles, Overdrive:
	- Reduces overhead between summarization calls
	- Significantly increases summarization speed (≈ +50% TPS in many cases)
	- Is especially beneficial for frequent, automated, or background summaries
	
	{{< callout type="warning" >}}  
	Ollama Overdrive is **not recommended for systems with limited RAM or VRAM**. Keeping models resident in memory reduces resources available to other applications.  
	{{< /callout >}}

	{{< callout type="info" >}}  
	When enabled, persistent memory usage will appear in the live hardware monitor.
	{{< /callout >}}	
	
1. #### Speaker Detection
	Speaker Detection (also known as **diarization**) is an optional preprocessing step applied after transcription.
	
	During standard transcription, audio is converted to text without speaker context. Speaker Detection analyzes the audio waveform to identify **speaker boundaries**, allowing Nucleate to determine _when different speakers are talking_.
	
	When enabled:	
	- Multiple speakers are detected and separated	    
	- Transcripts are annotated with labels such as:
	    - `[Speaker 1]`, `[Speaker 2]`, etc.
	- Diarized transcripts become available for speaker-aware Insights

{{< callout type="info" >}}  
Speaker Detection requires **local transcription**. OpenAI API transcription does not support diarized backends.  
{{< /callout >}}

{{< callout type="info" >}}  
Speaker Detection must be enabled before diarization-related features become available elsewhere in the app.
{{< /callout >}}

2. #### Speaker Identification
	Speaker Identification is an optional **post-processing layer** applied to diarized transcripts.
	
	While Speaker Detection determines _that_ different speakers exist, Speaker Identification attempts to infer **who those speakers are**.	
	This process:
	- Reviews diarized transcripts using contextual and conversational cues
	- Attempts to assign real-world speaker identities
	- Applies confidence thresholds before replacing generic labels
	
	If confidence is sufficiently high, labels like `[Speaker 1]` are replaced with inferred names.  
	If confidence is low, generic speaker labels are preserved.
	
	{{< callout type="info" >}}  
	Speaker Identification only runs when Speaker Detection is enabled. No identities are assigned unless confidence thresholds are met.  
	{{< /callout >}}

### Why these settings exist
These features allow Nucleate to scale smoothly from:

- Simple, single-speaker personal notes to
- Multi-speaker meetings, interviews, and lectures

without forcing complexity on users who don’t need it.

Most users can safely leave these settings disabled until a specific workflow requires them.

The panels below are intended for users who want deeper control over how transcription and summarization behave.

<img src="/menu/advanced_settings_1.png">
<img src="/menu/advanced_settings_2.png">
<img src="/menu/advanced_settings_3.png">
<img src="/menu/advanced_settings_4.png">
</details>

<details>
<summary>File sync</summary>
<img src="/menu/directory_settings.png">

### File & folder settings

These settings control **where Nucleate reads from, writes to, and how it manages updates** across your local folders.

1. #### Summary filename
	Customize the filename used for generated summaries.
	- Changes apply to **all future summaries**
	- Existing summaries in the output folder **and Notion database** (if configured) are automatically renamed to match
	- Useful for aligning with Obsidian conventions or personal naming schemes

2. #### Incoming audio folder
	The folder Nucleate monitors for new audio files.
	- Any supported audio file dropped here is automatically queued
	- Folder watching runs continuously while the app is active
	- Files are processed in the order they appear

3. #### Audio archive folder
	The destination for audio files after transcription completes.
	- Keeps the incoming folder clean
	- Preserves original audio for reprocessing or auditing
	- Recommended: use a backup drive if storage is a concern.

4. #### Summary output folders
	Define where Nucleate writes generated summaries.
	- Separate folders can be assigned per summary type
	- A single folder may be reused for all outputs if preferred
	- Fully compatible with Obsidian vaults and plain Markdown workflows
	
	{{< callout type="info" >}}  
	The summary type in Notion is determined by the folder path. If Notion integration is enabled, it is strongly recommended to use separate folders for individual, weekly, monthly, and custom summaries. Using a single folder for multiple summary types may result in "unknown" summary types being reported in Notion.  
	{{< /callout >}}

5. #### Autosync
	When enabled, Nucleate **updates existing summaries in place** whenever new data becomes available.
	- Ensures summaries always reflect the most recent information
	- Updates local files and Notion entries (if configured)
	
	{{< callout type="warning" >}}  
	If you manually edit generated summaries, Autosync may overwrite those changes. Disable Autosync if you prefer to treat summaries as a starting point rather than a living document.  
	{{< /callout >}}

<img src="/menu/file_sync_settings.png">

### File Sync Settings

Manage recording saving properties, as well as synchronization of linked services.

1. #### Recording Save Behavior
	Controls how in-app recording sessions are saved and ingested.
	- **Auto-Save (Recommended)**  
	    Automatically saves recordings to the _Incoming Audio_ folder when recording ends. Files are immediately ingested by the Nucleate core process.    
	- **Prompt for Recording Save Path**  
	    Prompts for a save location at the end of each recording, allowing recordings to be stored outside the default folder.
   
2. #### Nucleate Re-Sync
	Forces an immediate refresh of long-range summaries.
	- Retriggers **weekly and monthly summaries** on demand
	- Normally checked automatically once per hour
	- Useful after bulk edits, config changes, or manual file updates   

3. #### Notion Sync Controls
	Synchronizes local summary output with your connected Notion database.
	
	- **Notion Re-Sync**  
	    Lightweight sync that updates existing Notion entries with current local summary content.
	- **Notion Push**  
	    Forces a full rebuild of the Notion database from local summary files.    
	
	{{< callout type="warning" >}}  
	Both actions may overwrite user-edited content in Notion. 
	{{< /callout >}}

<img src="/menu/summary_rebuild.png">

### Summary Rebuild
Reprocess or remove existing summaries with full control over content and preferences. Quickly rebuild a Daily, Weekly, or Monthly summary using the currently selected user mode and Insights, or safely delete transcripts and summaries without affecting original audio.

1. #### Rebuild Summary
	Regenerates a selected summary using the **current user mode, Insights, and preferences**.
	- Select a summary from the tabbed menu
	- Click **Rebuild** to regenerate content
	- If **Autosync** is enabled, the rebuilt summary is pushed to all synchronized folders

2. #### Delete Summary
	Permanently removes a summary and its supporting transcript.
	- Select a summary from the tabbed menu
	- Click **Delete** to remove:
	    - The summary
	    - The associated transcript
	- Content will **not** be rebuilt
	- The matching summary file in user folders can be safely deleted
	- The **original audio file is preserved** in the Audio Archive

</details>

<details>
<summary>Integrations</summary>
### Integrations

Nucleate integrates with third-party services to extend transcription, summarization, and note-sync workflows. All integration settings are optional and can be enabled or disabled independently.

<img src="/menu/openai_api.png">

#### OpenAI API

Configure access to OpenAI-powered transcription or summarization features.

1. Add a valid **OpenAI API key**.  
	The key is stored locally and in plain text.
	
2. Click **Validate** to confirm connectivity.  
	If validation fails, verify:    
	- An active internet connection
	- That the key is complete and valid

{{< callout type="info" >}}  
**Security note:** API keys are stored locally and unencrypted. Treat them accordingly.
{{< /callout >}}

<img src="/menu/notion_api.png">

#### Notion API

Synchronize summaries to a Notion database.

1. Toggle **Notion Integration** on or off.  
	When disabled, Nucleate will stop syncing to Notion even if credentials are present.    
2. Add a valid **Notion API Secret**.  
	The secret is stored locally and in plain text.
3. Add a valid **Database ID**.
4. If the Database ID is unknown, paste the **URL of the database page**.  
	Nucleate will attempt to extract a valid ID automatically.

{{< callout type="warning" >}}  
User-edited Notion content may be overwritten during sync or rebuild operations.
{{< /callout >}}

<img src="/menu/obsidian.png">

#### Obsidian

Enable compatibility with Obsidian vaults.

1. Define the **audio** and **summary output** directories.  
	These are the same directories configured in the File Sync menu.    
2. The status indicator will report whether the selected directory resides inside a valid **Obsidian Vault**.    

No additional setup is required.

</details>

<details>
<summary>Mode Builder</summary>

### Mode Builder

The **Mode Builder** allows you to create, modify, and extend user modes that control how Nucleate summarizes content. Each mode defines prompt structure, system behavior, and default tagging for daily, weekly, and monthly summaries.

This page provides direct access to the prompt layers used by Nucleate’s core summarization pipeline.

<img src="/menu/custom_modes.png">

#### Mode Selection & Identity

1. **Select a base mode**  
    Choose an existing user mode to populate the Mode Builder fields. This is the recommended starting point for creating new modes.
    
2. **Define a unique Mode ID**  
    Each mode must have a unique identifier in order to be saved as a new mode.
    - Existing modes do not require their ID to be changed
    - Custom modes must use a new, unique key
3. **Set the mode name**  
    This is the user-facing name displayed throughout the UI.
4. **Set the mode description**  
    A short description explaining the intended use case of the mode.

#### Daily Summary Prompts

5. **Define Initial and Final prompts (Daily)**  
    These prompts frame how daily summaries are constructed.
    - The **Initial prompt** primes the model
    - The **Final prompt** performs consolidation and formatting
    
	{{< callout type="info" >}}  
	The bracketed token **`[chunk]`** must remain unchanged. This placeholder is dynamically replaced with transcript content during processing.
	{{< /callout >}}

#### Weekly & Monthly Summary Prompts

6. **Define Initial and Final prompts (Weekly / Monthly)**  
    These prompts control how content is aggregated across multiple sessions.
    - Weekly and Monthly prompts may share structure or differ significantly
    
	{{< callout type="info" >}}  
	As with Daily prompts, **`[chunk]` must remain unchanged**
	{{< /callout >}}        

#### System Prompts

7. **Define the Daily system prompt**  
    The system prompt governs tone, structure, and behavioral constraints for daily summaries.  
    It is strongly recommended to use a prefabricated mode as a reference when authoring custom system prompts.
    
8. **Define Weekly and Monthly system prompts**  
    These prompts guide long-form synthesis and higher-level abstraction.  
    Matching the structure of existing modes will generally produce more consistent results.

#### Tags

9. **Define the initial tag list**  
    Tags are applied automatically to generated summaries.
    - One tag per line
    - Single-word tags only
    - No punctuation
    
    Tags can be modified at any time from either the **Mode Builder** page or the **User Mode** panel.

#### Notes & Recommendations
- Mode Builder changes affect **all future summaries** using that mode
- Improper prompt structure can lead to degraded or unstable outputs
- When in doubt, duplicate and modify an existing mode rather than starting from scratch

</details>

<details>
<summary>Nucleate Lab</summary>

### Nucleate Lab

**Nucleate Lab** is an experimental workspace for running controlled, one-off transcription and summarization jobs outside the automatic Nucleate pipeline.

Lab profiles allow you to combine user modes, summary types, models, and Insights in ways that do not affect your default configuration. This makes Lab ideal for testing, comparison runs, and specialized workflows.

<img src="/menu/nucleate_lab_profiles.png">

#### Lab Profiles

1. **Select a Lab profile**  
    Choose an existing Lab profile to view or modify its configuration.    
2. **Define profile name and unique key**  
    Each Lab profile requires a unique key in order to be saved. Existing profiles do not require the key to be changed.
3. **Choose parent mode and summary type**  
    Select:
    - A parent **User Mode** (prebuilt or custom)
    - A **summary type**: Daily, Weekly, or Monthly
    
    The selected mode and summary type define the baseline prompting and structure used by this profile.
4. **Select summarization backend and model**  
    Choose between:
    - **Local (Ollama)** — models already downloaded to your machine
    - **OpenAI** — preconfigured models, with the option to manually enter others
    Available options depend on the selected backend.
    
5. **Toggle two-pass summarization**  
    When enabled, content is first passed through a lightweight cleanup step before summarization.  
    This is recommended for Lab workflows that operate directly on raw transcripts or noisy input.

<img src="/menu/nucleate_lab_preferences.png">

#### Lab Preferences & Insights

1. **Favorite Insights**  
    Favorited Insights appear at the top of the list for quick access.  
    Right-click an Insight to add or remove it from Favorites.
    
2. **Enable Insights for Lab content**  
    Enables Insights for all Lab-generated output.
    - **Smart Insights**, when enabled, override all other Insight selections
    - **Tags** and **Transcript** options remain enabled regardless of Smart Insights

<img src="/menu/nucleate_lab_actions.png">

#### Lab Actions

1. **Select a Lab profile**  
    Choose one of the prefabricated or custom Lab profiles to use for processing.    
2. **Process audio files**  
    Select one or more audio files to:
    - Transcribe only (saving the transcript), or
    - Transcribe and summarize using the selected Lab profile
    
    This process is independent of the automatic Nucleate pipeline.
    
3. **Process markdown files**  
    Select one or more markdown files and summarize their contents using the selected Lab profile.

### Notes & Intended Use
- Lab output does not modify existing summaries unless Autosync is explicitly enabled elsewhere
- Lab profiles are isolated from default User Modes and settings
- This space is intended for experimentation, testing, and non-standard workflows

</details>

<details>
<summary>System</summary>
<img src="/menu/system_panel.png">

### System Settings

Apply a signature to summaries, validate your license, and view detailed usage statistics. Reset stats when needed and ensure the app operates according to your preferred workflow.

1. **Signature line toggle**  
	Enable or disable appending a signature line to the end of summaries generated by Nucleate.

<img src="/menu/license_settings.png">

#### License Management

1. **Validate Pro license**
	
	- If Nucleate Pro has been purchased, the app will automatically search common folders for a valid license.
	- If a license is not detected, manually browse to select the license file. Once found, it will be validated automatically.

<img src="/menu/statistics_panel.png">

#### App Statistics

A lightweight panel that displays usage statistics and other app metrics.

1. **Refresh statistics**  
    Updates the values since the last app launch.   
2. **Reset statistics**  
    Clears all recorded usage data.
    
    {{< callout type="warning" >}}  
    This action is irreversible. Only reset if you are sure you want to discard all current statistics.  
    {{< /callout >}}

<img src="/menu/performance_panel.png">

#### Performance Calculator

The Performance Calculator is an in-app benchmarking and cost estimation tool. It measures real transcription and summarization performance on _your_ hardware and compares local compute costs against OpenAI usage.

**What it measures**
- **Transcription speed** as a multiplier relative to audio length
- **Summarization speed** in tokens per second (TPS)
- **Estimated cost** of local compute based on power usage and electricity cost

1. **Transcription test**
	- Runs a short (~3 minute) internal audio file  
	- Measures total transcription time to calculate a speed multiplier  
	    _(e.g. 1 minute to transcribe 3 minutes of audio = 3×)_
	- Running the test multiple times improves accuracy

	{{< callout type="info" >}}  
	Transcription speed testing is unavailable when transcription services are set to OpenAI.  
	{{< /callout >}}

2. **Summarization test**
	- Uses the currently configured local Ollama model
	- Measures tokens processed per second (TPS)
	- The base model is cached automatically before measurement
	
	{{< callout type="info" >}}  
	Summarization speed testing is unavailable when summarization services are set to OpenAI.  
	{{< /callout >}}

**Cost estimation**
- Uses selected hardware wattage and local electricity cost (per kWh)    
- Combines:
	- Total transcription minutes
	- Total summarized tokens (from App Statistics)
- Produces a side-by-side comparison against OpenAI pricing
	    
{{< callout type="info" >}}  
OpenAI cost estimates assume GPT-3.5-turbo for summarization and Whisper for transcription (pricing as of July 2025).  
{{< /callout >}}

</details>