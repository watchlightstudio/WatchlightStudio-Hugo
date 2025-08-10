---
linkTitle: "02 Installation"
type: docs
weight: 6
draft: true
---
## To install Echo
### Prerequisites
Check [this page](/projects-and-tools/echo/echo-requirements) to make sure you've already installed all of the required software before proceeding. At this point you should have installed:
- [Python for Windows](https://www.python.org/downloads/)  
- [Ollama for Windows](https://ollama.com/download)  
- [Cuda toolkit](https://developer.nvidia.com/cuda-downloads)  

### Basic installation instructions
Echo was designed for quick, two-step deployment. First, run an a short script to prepare the correct environment. Second, select preferred app settings. That's it!
- Download Echo.zip and unzip to the desired directory.
- Once extracted, double click on "first_launch.bat" which will open a new terminal and automatically complete a short set of activities:
	- Create a python virtual environment (.venv) within the Echo app folder
	- Download required python dependencies and faster-whisper "medium" model (1.5GB) for transcription
	- Create a new shortcut for Echo 
	- Launch Echo for the first time
- Follow the setup wizard using either "Simple" or "Advanced" setup.
	- "Advanced" setup allows for additional customization, folders, model settings, etc. All settings can be changed within the app, so don't sweat it too much.
	- Once wizard setup is complete, the app will automatically restart. It's OK to close the terminal window now.

{{< callout type="info" >}}
A short background script will also check whether an NVIDIA GPU is detected and available. If none is detected, a warning message will appear about limited settings.
{{< /callout >}}

### Supplemental install if using OpenAI services
- If the "Echo" task is greyed out after app restart, OpenAI was likely selected as a service for either summarization or transcription (or both) and an API key still needs to be added.
- To set the OpenAI API key, navigate to "Advanced Settings/Integrations" and add an API key. See help page for more details.
### To re-launch Echo after first-time setup
- The setup script only needs to be run once. Afterwards, simply search the Windows toolbar for "Echo" and select the app! You can save this shortcut as you would any other!

{{< callout type="info" >}}
For Windows 11, right-click the shortcut and "See more options" to find "Pin to taskbar" option.
{{< /callout >}}

## To uninstall Echo
By design, Echo is supposed to be self-contained and transparent about data. Simply find the unzipped folder and delete it. All cached transcripts, summaries, models, file data, preferences, and python virtual environment will be destroyed.

The following files and dependencies are no longer needed and could be removed, if desired. For each, open new PowerShell.
- Ollama models
```bash
ollama list
ollama rm model-base
ollama rm model-dailyDevlog
ollama rm model-weeklyDevlog
ollama rm model-monthlyDevlog
ollama rm mistral # or any other listed model
```
- nltk stopwords
```bash
pip uninstall nltk
```
- faster-whisper models

{{< callout type="warning" >}}
This command will delete all cached huggingface models.
{{< /callout >}}
```bash
Remove-Item -Recurse -Force "$env:USERPROFILE\.cache\huggingface"
```
You may also install Ollama, Python, and Cuda toolkit now, if desired.