---
linkTitle: "01 Requirements"
type: docs
weight: 5
draft: true
---
## Recommended hardware and software pre-requisites
### Operating system
Currently, Echo is available only for Windows users. Please ensure you are running Windows 10 or 11 (Home and Professional are both fine) and your operating system is up to date.

### Hardware recommendations
An NVIDIA GPU is strongly recommended (>12GB VRAM is ideal) and provides the most flexible configuration support. If you have an AMD/Intel GPU or an NVIDIA GPU with inadequate VRAM (4-6 GB), local LLM summarization models and transcription will automatically default to CPU-only support, which can be quite slow and requires at least 16GB of RAM to be performative.

In-app, you can change the default models to use OpenAI API if desired for faster speed, but this option requires an internet connection and may cost money to perform transcription and summarization.

| CPU | RAM (min) | GPU    | VRAM    | Transcription | Summarization | OpenAI support | Local speed |
| --- | --------- | ------ | ------- | ------------- | ------------- | -------------- | ----------- |
|     |           |        |         | (recommended) | (recomemnded) |                |             |
| Any | <16GB     | -      | -       | -             | -             | Yes            | N/A         |
| Any | 16-128GB  | -      | -       | CPU-only      | CPU-only      | Yes            | Slow        |
| Any | 16-128GB  | AMD    | -       | CPU-only      | CPU-only      | Yes            | Slow        |
| Any | 16-128GB  | Intel  | -       | CPU-only      | CPU-only      | Yes            | Slow        |
| Any | 16-128GB  | Nvidia | <8GB    | GPU<span style="color:yellow;">**</span>          | CPU-only      | Yes            | Slow        |
| Any | 16-128GB  | Nvidia | 8-12GB  | GPU           | GPU           | Yes            | Medium      |
| Any | 16-128GB  | Nvidia | 12-24GB | GPU           | GPU           | Yes            | Fast        |

{{< callout type="info" >}}
<span style="color:yellow;">**</span>Use "medium" or smaller faster-whisper model to comfortably stay within VRAM limits.
{{< /callout >}}
### Software pre-requisites
The only required SW prerequisites for Echo installation are Python and Ollama, which must be installed before running first time setup. If you want NVIDIA GPU acceleration, you must also download the CUDA Toolkit. If the toolkit is not installed, Echo will default to CPU-only support.
- Download and install [Python for Windows](https://www.python.org/downloads/), v3.13.5 confirmed working. During installation, check that "Add to system PATH" is enabled.
- Download and install [Ollama for Windows](https://ollama.com/download). No models need to be pre-downloaded.
- Download and install the appropriate [Cuda toolkit](https://developer.nvidia.com/cuda-downloads) for your system. Ensure that the toolkit is on the system PATH.
	- To check that the toolkit is on the system PATH, find "Edit the system environment variables" in the Windows search bar.
	- In "System Properties," navigate to the "Advanced" tab and select "Environmental Variables"
	- The list of "System variables" should include a "Path." Double click to view all environment variables.
	- If installed correctly, you will find a directory path to:
```bash
\NVIDIA GPU Computing Toolkit\CUDA\v12.x
```