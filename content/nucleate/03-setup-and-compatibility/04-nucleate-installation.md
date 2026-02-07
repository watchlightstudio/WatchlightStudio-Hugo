---
linkTitle: "Installation"
type: docs
weight: 4
slug: "installation"
url: "/nucleate/setup-and-compatibility/installation"
---
## To install Nucleate
### Prerequisites
Check [this page](02-nucleate-hardware-prerequisites.md) to make sure you've identified your hardware prerequisites. If planning to use local summarization, be sure also to have installed [Ollama](https://ollama.com/download).  For the most flexible support, ensure also that [FFmpeg/FFprobe](05-nucleate-ffmpeg-installation.md) have been correctly installed.

### Basic installation instructions
Nucleate was designed for quick, one-step deployment. On Windows, select the .exe. On Mac, mount the .dmg and drag the app into your Applications folder. That's it!

On first startup, Nucleate will automatically seek a license file in your Downloads, Documents, and Desktop folders. If found, it will automatically validate and unlock all Pro options. If not found, you can navigate to the file manually via "System/License" after first time setup is complete.

Once inside the app, follow the guided setup. All that's needed to get going is to select a User Mode and to identify the directories to use for Nucleate inputs and outputs.

{{< callout type="info" >}}
In the background, Nucleate will audit the available hardware on your machine and will attempt to automatically optimize settings to give you the best experience. After first time setup, you can manually adjust the "AI Engine" settings to fit your specific style.
{{< /callout >}}

### Connecting APIs
Nucleate Pro can optionally connect to both OpenAI and Notion services.

#### OpenAI services
To connect to OpenAI requires a funded OpenAI account and [API key creation](https://platform.openai.com/api-keys). To set an OpenAI API key inside Nucleate, navigate to "Integrations/OpenAI API" and paste a key. The key is stored on your machine and in plain text. Select "Validate" to check for a valid connection.

If a valid OpenAI API key is provided, more settings become available in the "AI Engine/AI Model Settings" panel. Toggle any of the available Summarizer or Transcription options to make use of the API service.

#### Notion services
Notion is a cloud-based note taking app. Nucleate can optionally connect to a Notion database so that you can publish and manage your summaries to the cloud.

To connect Nucleate to Notion requires a Notion account, a formatted database, and an API key. See this video for a full setup guide: @@@

## To uninstall Nucleate
Nucleate works like any other desktop app. On Windows, find the app in "Add or remove programs" and select to uninstall. On Mac, drag the app to the trash.