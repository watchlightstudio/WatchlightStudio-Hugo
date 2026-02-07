---
linkTitle: "Software"
type: docs
weight: 3
slug: "software"
url: "/nucleate/setup-and-compatibility/software"
---
## Recommended software

## Ollama
Ollama is required if you want to perform local summarization. If you use OpenAI API services instead, Ollama is not required and can be ignored.

The recommended Ollama models will be automatically downloaded during first-time setup. Model variants will be built to support both the core summarizers (Daily, Weekly, Monthly) and all Insights. The models will be re-built if the user mode is changed.

### In-app status
During app launch, Nucleate will check whether Ollama is currently running in the background or system tray. If not running, Nucleate will attempt to start Ollama. The indicator light on the Hub reflects the current launch status.
{{< callout type="info" >}}
Ollama will remain open in the background when Nucleate is closed.
{{< /callout >}}

### In-app model customization
Mistral 7B is the preferred LLM for Nucleate summarization. It is performant and punchy, and the system prompts and Insights have been tuned to support its typical output.

>Prefer a different model? You can change it at any time.

Pick from one of the most common Ollama downloads or enter your own. Anything listed on the Ollama models page can be pulled into Nucleate.

## FFmpeg and FFprobe
FFmpeg and FFprobe are essential for handling a wide range of audio formats and enabling Whisper-based transcription. Without them, Nucleate is limited to WAV-only audio and cannot use certain transcription backends.

{{< callout type="info" >}}
Installing FFmpeg is strongly recommended. [Installation instructions are available here](05-nucleate-ffmpeg-installation.md). Once installed, Nucleate will automatically detect it and unlock full audio support.
{{< /callout >}}

### Why isn't FFmpeg bundled with Nucleate?
FFmpeg is a powerful open-source toolkit, but many distributions are licensed under terms that restrict bundling and redistribution within commercial applications.

To avoid licensing conflicts and to give users control over how FFmpeg is installed and updated, Nucleate does not include FFmpeg by default. Instead, you can install it separately using the method that best fits your system.

Once installed, Nucleate will automatically detect FFmpeg and enable full audio and transcription capabilities.