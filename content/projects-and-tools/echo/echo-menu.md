---
linkTitle: "Menu Details & Help"
type: docs
weight: 8
draft: true
---
## Menu Details & Help
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

### Basic settings
<details>
<summary>Echo - "User Mode" [Local/OpenAI]</summary>

- The Echo task is enabled upon launch by default but can be toggled on/off by selecting the menu item.

	{{< callout type="warning" >}}
	If the Echo task is greyed out, App configuration is incomplete or invalid. 
	{{< /callout >}}

- When enabled, Echo automatically looks for new audio files, performs summarization based on the current User Mode, and uploads new files to the user-defined folders.
	- If Notion is enabled and setup, new summaries are automatically uploaded to a Notion database.
	- If Autosync is enabled, newly generated summaries will automatically overwrite old files if there is a filename match.  
- The Echo task status shows the current User Mode as "Developer," "Business," "Personal," or "Custom."
- The Echo task status shows the current compute resource as either "Local" or "OpenAI."
	- If the UI says "Local," then both transcription and summarization are set to your local machine.
	- If the UI says "OpenAI," then either transcription or summarization (or both) are set to use OpenAI and an API key has been provided.

	{{< callout type="warning" >}}
	Using OpenAI means that data is sent to the OpenAI servers before being returned to your computer. An internet connection is required for this mode and it may incur expenses depending on selected OpenAI models.
	{{< /callout >}}
</details>

<details>
<summary>Show Advanced Settings</summary>

- Advanced settings is toggleable and is saved to the configuration file. Restarting the App will automatically load the last saved menu mode.
</details>

<details>
<summary>Exit</summary>

- App exits from tray and no longer runs in the background. Ollama will remain in the tray app but cached models will be cleared from memory and may need to re-initialize during next app launch.
</details>

### Advanced settings
<details>
<summary>Manual Actions</summary>

### Manual Actions
- #### Run custom summary
	- Enables the user to manually select one more files for summarization with custom prompting. These prompts are different than the currently selected User Mode and allow the user to run individual summaries without having to change current mode or stop automatic background processes.
	- The output file quality and format will vary based on the selected prompting, though typically are simple summary paragraphs.
	- To use custom summary
		- Select one or multiple files using standard keyboard shortcuts.
		- Select your preferred prompt from the dropdown menu. You can add, edit, and delete custom prompts elsewhere in the App advanced settings.
		- After selecting the custom prompt, summarization will start, using either Local or OpenAI resources depending on current settings.
		- Once summarization is complete, name the file and select "Save." Files will automatically be moved to the user-selected "Custom" folder path. 

		{{< callout type="warning" >}}
		The custom summary function does not automatically apply Tags, prepare Keynotes, or append Transcripts from the selected files. 
		{{< /callout >}}

- #### Run weekly summary
	- If selected, will force the app to check whether any new weekly summaries are available for generation.
- #### Run monthly summary
	- If selected, will force the app to check whether any new monthly summaries are available for generation. 
 
	{{< callout type="info" >}}
	If the Echo task is enabled, the app automatically checks whether new weekly and monthly summaries are available once per hour.
	{{< /callout >}}

- #### Tag file with keywords
	- Enables the user to select any .md file and apply tags from the current User Mode. When selected, navigate to the target .md file and confirm selection in the App. Tags will automatically be applied if any matches are found.
</details>

<details>
<summary>Modes & Prompts</summary>

### Modes & Prompts
- #### Switch mode
	- Select the currently active User Mode. Available and correctly configured modes can be selected from the dropdown menu. Changing the active User Mode will update the current "Echo" task status.
	- All new summaries will use the newly selected mode. Existing summaries from the prior user mode will not be overwritten.

- #### Edit modes 
	{{< callout type="warning" >}}
	Adding or modifying a custom user mode is an advanced action and is not recommended for casual users.
	{{< /callout >}}
	- Add, remove, or edit custom user modes, such as personal journaling, goal setting and reflection, fitness and health tracking, bedtime storytelling, D&D worldbuilding, etc. Anything you talk a lot about! 
	- Select Add/Remove/Edit from the first dropdown menu.
	- To "Add" a new custom user mode, the user must first prepare several files, including:
		- Ollama system prompt for individual summaries (no filetype suffix)
		- Ollama system prompt for weekly summaries (no filetype suffix)
		- Ollama system prompt for monthly summaries (no filetype suffix)
		- OpenAI system prompt for individual summaries (.txt)
		- OpenAI system prompt for weekly summaries (.txt)
		- OpenAI system prompt for monthly summaries (.txt)
		- Taglist .json file
	- Using the GUI, provide a custom name for the new user mode and navigate to the prepared files. Once all fields exist and the custom user mode name is unique, "Save" the new user mode.
	- To "Remove" a custom user mode, simply select the desired mode from the dropdown and complete confirmation prompting. Removing a custom user mode does not delete or modify the matching system prompts or taglist files.
	- To "Edit" a custom user mode, navigate to the desired mode from the dropdown menu.
	- Using the GUI, make any necessary modifications and/or select updated system prompts and taglist files (see "Add" custom user mode for details). Once all fields exist and the name is unique, "Save" edits to the user mode.
- #### Edit prompts
	- Add, remove, or edit custom prompts for the "Run custom summary" function. These custom prompts are meant as lightweight prompting options that allow the user run one-off summaries with flexibility and without preparing system prompts or custom models. Some prompt tuning via "Edit" may be required to get the desired output. 
	- Select Add/Remove/Edit from the first dropdown menu.
	- To "Add" a new custom prompt, provide a custom name and prompting instructions for each step of summarization. The summarization script "chunks" the text-to-be-summarized into more manageable pieces, and so you must provide both an initial prompt (for the first chunk) and chunk prompts (to for continued summarization). All prompts must contain "{chunk}" at the end of the prompt in order for the script to ingest appropriately. See autofill examples for formatting details.
		- Summary initial prompt - provide initial context and instructions to the LLM about what the scope of the summary should contain.
		- Summary chunk prompt - provide supporting context and instructions to the LLM about what is being summarized. 
		- Keynote initial prompt
		- Keynote chunk prompt
	- Once all fields exist and the custom prompt name is unique, "Save" the new custom prompts. The app will automatically restart, and the new prompt will become available in "Run custom summary."
	- To "Remove" a prompt, simply select the desired prompt from the dropdown and complete confirmation screens. Removing the custom prompt deletes all prompting instructions and cannot be undone.
	- To "Edit" a custom prompt, navigate to the desired prompt from the dropdown menu.
	- Using the GUI, make any necessary modifications to the prompts or name. Once all fields exist and the name is unique, "Save" edits to the custom prompt.

	{{< callout type="info" >}}
	If the mode is set to "local," all currently installed Ollama models will be shown in the dropdown menu. To install additional models, either do so directly via Ollama or by entering the desired model in [Set Ollama model](#set-ollama-model). Using the in-app method will set the default Echo summarization model to whatever is entered, so you may need to reset the original model after download is complete.

	If the mode is set to "openai," you may select from the dropdown menu or enter alternative [OpenAI](https://platform.openai.com/docs/models) models of your choosing.
	{{< /callout >}}

- #### Edit tags
	- Allows the user to customize the taglist of the currently selected User Mode displayed in the "Echo" task bar. Tags can be added, removed, or edited via the GUI.
	
	{{< callout type="info" >}}
	Echo does not support multi-word tags or nonsense words. Abbreviations occasionally work, such as "LLM" or "API," though not always. For the most consistent tagging, use simple, one-word tags and enter as lower-case.
	{{< /callout >}}
	
</details>

<details>
<summary>Directory & Sync</summary>

### Directory & Sync
- #### Set folders
	- Set new folder paths for the output summary files. Simply navigate to the desired location for each folder.

	{{< callout type="info" >}}
	The summary file type in the Notion database is set based on the folder path. If Notion is enabled, it is strongly recommended to set separate folders for individual, weekly, monthly, and custom outputs for clear labeling. If a single folder is used for multiple summary types, Notion will report "unknown" summary type.
	{{< /callout >}}

- #### Set preferences
	- Customize the output summary files from "Echo," including output filename, tags, keynotes, and appended transcripts.
	- To change filename, simply enter the preferred name. The GUI will automatically update to show what the new filesname will look like. Currently, it is impossible to remove or modify the appended dates/timestamps and (Weekly)/(Monthly) labels.

	{{< callout type="warning" >}}
	When a new filename is selected, the user must confirm deletion of cached summary files within the App folder. This does not impact the saved files in the users folders or Notion uploads (if enabled). Canceling out will not delete any files and will not save the updated filename.  
	
	Once "Confirm" is selected, the cached files will be deleted and Echo will automatically start re-summarizing all existing transcripts, weekly, and monthly summaries with the new filename. Please note, this may take a while depending on the number of files to be re-summarized.
	{{< /callout >}}

	- In addition to filename, the user can toggle the output format of the various summaries to include or exclude "Tags," "Keynotes," and "Transcripts." Changing these toggles will not reset cached files. These new settings will only apply to newly generated summaries.

	{{< callout type="info" >}}
	Disabling "Keynotes" will reduce both input and output tokens required to perform summarization tasks.  However, disabling "Transcripts" does not impact the number of required tokens.
	{{< /callout >}}

- #### Set autosync
	- Enable/disable Autosync functionality. It is recommended to enable Autosync.
	- If Autosync is enabled:
		- Summaries generated by Echo are automatically pushed to user folders and overwrite files of the same name.
		- Manual edits to summaries in the user folders are automatically pushed to Notion.
		- The direction of file overwrite is: cached summaries (not seen) --> summaries in user folders --> Notion database entries

		{{< callout type="warning" >}}
		 Because of file overwrite actions, there is a possibility of data loss under a very specific set of conditions:
		- If Autosync is enabled and Notion is disabled:
			- Any manual edits will be overwritten if in-app "cached files" are deleted and regenerated (very uncommon and requires manual confirmation).
		- If Autosync is enabled and Notion integration is enabled:
			- Any manual edits to the Notion database entries will be overwritten if 1) the user makes separate edits to the original summary file or 2) if in-app "cached files" are deleted and regenerated (very uncommon and requires manual confirmation).
		{{< /callout >}}

- #### Notion re-sync
	- Manually force a re-sync of user files to Notion database based on most recent timestamp.

		{{< callout type="warning" >}}
		If the files in the user directories have been manually modified or updated, these changes will overwrite current Notion database files.
		{{< /callout >}}
</details>

<details>
<summary>Integrations</summary>

### Integrations
- #### OpenAI API
	- Set an API key for OpenAI, which is required to use OpenAI summarization or transcription functionality. Before setting up, create an OpenAI account and add balance to the account.
	- To setup:
		- Visit [OpenAI](https://platform.openai.com/api-keys) for an API key.
		- In the upper right hand corner, select "Create a new secret key" and follow prompting.
		- Copy the secret key to the clipboard and paste into the Echo app.

		{{< callout type="warning" >}}
		The API key is stored locally and in plain text in the config.toml file, which is in the root directory of the Echo app folder.
		{{< /callout >}}

- #### Notion setup
	- Connect Echo with [Notion](https://www.notion.com/), a cloud-based note taking and organization app.
	- A setup video is shown here (@@@) and is documented below.
	- Before proceeding, create a Notion account. Setup can be performed with either the in-browser app or the downloaded Notion app
	- In the browser or app, select "Add a page" and label as preferred (e.g. using "Echo" as an example for the below instructions)
	- On the new page, add a new "Database - Inline"
	- Format the new database with the following columns in this exact order:
		- First column: "Name"
		- Second column: "Tags" - change column type to "Multi-select"
		- Third column: "Date" - change column type to "Date"
		- Fourth column: "Type" - change column type to "Multi-select"
		- Fifth column: "Last uploaded" - change column type to "Date"
	- Once the database is setup, API access needs to be given to the specific page. Visit [Notion Integrations](https://www.notion.so/my-integrations) and login/create an account.
	- Add a "New Integration" and select the associated workspace containing the "Echo" page. "Type" can be set to "Internal." 
	- Navigate to the "Access" tab, "+Select pages," and select the new "Echo" page. Confirm access.
	- Navigate to the "Configuration" tab and ensure access to Read/Update/Insert content.
	- Show the "Internal Integration Secret" API key and copy into the Echo app Notion setup page.

	{{< callout type="warning" >}}
	The API key is stored locally and in plain text in the config.toml file, which is in the root directory of the Echo app folder.
	{{< /callout >}}
	
	- Return to the Notion "Echo" page and navigate to database settings. Select "Copy link to view," which provides a URL string.
	- In the Echo app, paste the unique, 32 character string from the URL into the setup dialog and save changes.
	
	{{< callout type="info" >}}
	The 32 character string is buried in the URL and precedes "?v", such as:  
	`www.notion.so/`<span style="background: yellow; color:black;">22767a106600802ab991fba13bf1f8b8</span>`?v=22767a1066008032bd49000c64c00285&source=copy_link`
	{{< /callout >}}
	
	- If performed correctly, the app will restart and summary files will automatically start updating in the Notion database.

- #### Obsidian setup
	- The Echo app was originally designed for [Obsidian](https://obsidian.md/download) users. Simply set the file directory paths for summary outputs to the desired Obsidian Vault. No additional actions are required.
</details>

<details>
<summary>LLM Settings</summary>

### LLM Settings
- #### Echo model settings
	- Set or edit the default summarization and transcription settings for Echo.

	{{< callout type="info" >}}
	During app start-up, Echo quickly checks for the presence of an NVIDIA GPU. If a compatible NVIDIA GPU is not detected, the user can select either OpenAI or CPU-only local fallback.
	{{< /callout >}}

	- Summarization options:
		- If summarization is set to "Local," Echo will use custom Ollama models, which are generated by the App during first time setup. By default, the Ollama base model is Mistral, which is lightweight and performant for basic summarization tasks.
		- If summarization is set to "OpenAI," the default model is set to GPT3.5-turbo, which is a good balance of summarization quality, speed, and token cost (as of July 2025).

		{{< callout type="info" >}}
		Alternative local models can be set using [Ollama models](#set-ollama-model). Alternate [OpenAI](https://platform.openai.com/docs/models) models can be manually entered by writing-in the dropdown menu.
		{{< /callout >}}

	- Transcription options:
		- If transcription is set to "local" the user can choose the selected model and compute resource.
			- The transcription models include base, medium, large, etc.

			{{< callout type="info" >}}
			The highest fidelity model is large_v3, which can be resource intensive. Smaller models, like "medium" may be more practical on lower-end hardware if the transcription speed is too slow (see [Echo speed check](#echo-speed-check) for in-app testing method).
			{{< /callout >}}

			- The transcription compute options are either cuda-based (i.e. GPU) or CPU-based. Cuda will be selected by default for most users and is strongly preferred if an NVIDIA GPU is available.
		- If transcription is is set to "OpenAI," audio files will be uploaded to OpenAI and transcribed using "Whisper."

			{{< callout type="warning" >}}
			Transcription via OpenAI can be expensive, especially for large files.
			{{< /callout >}}

- #### Set Ollama model
	- Select different Ollama model as the "base" model, for testing and development.
	- By default, Mistral 7B is used as the base model. Three custom models are generated from the base model, using the provided, in-app system prompt files. If the user wants to test alternates (i.e. Deepseek, Mixtral, Llama2, etc), they can enter or select within this dialog page.
	- Currently installed Ollama models (cmd, "ollama list") are shown in the dropdown menu. New models, not yet downloaded, can be entered manually but must explicitly match one of the models listed on the [Ollama page](https://ollama.com/search).
	- If a new model is selected that has not yet been downloaded, the user must approve of the 3rd party download.

	{{< callout type="info" >}}
	In testing and development, Mistral consistently generated the highest quality summarization results and is strongly recommended. It is relatively lightweight, compared to many alternatives, and is operable on most hardware.
	{{< /callout >}} 
	
</details>

<details>
<summary>Tools & Reports</summary>

### Tools & Reports
- #### Echo statistics
	- A simple dialog page that shows the user app statistics and usage. Values can be reset, if desired.
- #### Echo speed check
	- An in-app calculator that allows the user to test in-app transcription and summarization speeds, as well as estimate cost of running locally versus using OpenAI servers.
	- To test transcription speed, select the appropriate button. A short, 3 minute test file will be transcribed and the time taken to perform transcription is used to calculate a speed multiplier (i.e. 1 minute to transcribe 3 minutes = 3x). Run this test twice to get more accurate values.

	{{< callout type="info" >}}
	 The transcription speed test feature is not available if transcription services are set to OpenAI.
	{{< /callout >}}

	- To test summarization speed, select the appropriate button. The app will cache the base Ollama model and perform measurement of "tokens per second" or TPS. The summarization speed test is not available if summarization services are set to OpenAI.
	- Select the appropriate wattage of your compute hardware (i.e. GPU wattage or CPU wattage) and approximate cost of electricity (per kWh) for your area.
	- Selecting "calculate" will compare the cost of local analysis, based on cost of electricity, total minutes of transcription, and total accumulated tokens during the app lifetime (from App Statistics). Comparisons are also provided as-if both transcription and summarization are performed with OpenAI.

	{{< callout type="info" >}}
	The cost of OpenAI transcription and summarization is dependent on the selected model, but the calculator assumes GPT3.5-turbo is used for summarization and Whisper is used for transcription (pricing as-of July 2025).
	{{< /callout >}}

</details>

<details>
<summary>App Control</summary>

### App Control
- #### Setup wizard
	- Reset all settings and perform first-time setups again.
- #### License
	- Add or update the Echo app license. The app is free to use without a license, but please do not proliferate or share. If you find value in Echo, please consider supporting the developer.
	- If the app license is absent or invalid, the user will be notified with occasional reminders about activation and total usage.
- #### Cached files

	{{< callout type="warning" >}}
	Clearing cached files may result in data loss, if manual edits have been made to the output summary files. Please carefully review below notes before proceeding.
	{{< /callout >}}

	- Clear all
		- Clear all in-app cached transcripts and summaries. This is not a typical action and will require re-compute of all audio files and re-summarization of all transcripts. If Autosync is enabled, newly generated summaries will overwrite old files and manual edits will be lost.
	- Clear summaries
		- Clear all in-app cached summaries. This is not a typical action and will require re-summarization of all transcripts. If Autosync is enabled, newly generated summaries will overwrite old files and manual edits will be lost.
	- Clear transcripts
		- Clear all in-app cached transcripts. This is not a typical action. There will be no impact to summaries or to user files. No data will be ovewritten.
- View logs
	- Access to the Echo app logs. If errors occur, logs may be useful for diagnosing the root cause.
- Restart
	- Tray app restart. In the event that multiple functions are greyed out, restarting the app can often clear errors.
- About / Help
	- Provides information about the app, including help links.
	- If the app license is valid, the user can toggle whether or not the default footer appears in the Echo summaries. This toggle is not available if the license is absent or invalid and is the only restricted function of the app.
</details>