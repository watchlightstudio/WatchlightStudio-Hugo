---
linkTitle: "Hardware"
type: docs
weight: 2
slug: "hardware"
url: "/nucleate/setup-and-compatibility/hardware"
---
## Recommended hardware
### Operating system
Nucleate is available on both Windows and macOS and runs on modern versions of each OS. There is no planned Linux release at this time.

### In-app optimization
Too many options? No problem. In the "AI Engine" settings panel, the one-button "Optimize" will sort you out and make recommendations based on OS and available hardware. You can also view persistent and peak hardware usage estimates in the same panel and adjust settings manually if desired.


### Hardware recommendations
#### Windows
On Windows, an NVIDIA GPU is strongly recommended and provides the most flexible configuration support. If you have an AMD/Intel GPU or a NVIDIA GPU with inadequate VRAM, local transcription and summarization model settings will be optimized based on available hardware or will automatically fall back to CPU-only support. If running on CPU-only hardware, at least 16GB of RAM is recommended for local transcription or summarization.

##### Windows hardware recommendations
| CPU | RAM (min) | GPU    | VRAM    | Transcription | Summarization | OpenAI support | Local speed |
| --- | --------- | ------ | ------- | ------------- | ------------- | -------------- | ----------- |
| Any | <16GB     | -      | -       | Limited       | Limited       | Yes            | Slow        |
| Any | 16-128GB  | -      | -       | CPU-only      | CPU-only      | Yes            | Slow        |
| Any | 16-128GB  | AMD    | -       | CPU-only      | CPU-only      | Yes            | Slow        |
| Any | 16-128GB  | Intel  | -       | CPU-only      | CPU-only      | Yes            | Slow        |
| Any | 16-128GB  | NVIDIA | <8GB    | GPU<span style="color:yellow;">**</span>          | CPU-only      | Yes            | Slow        |
| Any | 16-128GB  | NVIDIA | 8-12GB  | GPU           | GPU           | Yes            | Medium      |
| Any | 16-128GB  | NVIDIA | 12-24GB | GPU           | GPU           | Yes            | Fast        |

{{< callout type="info" >}}
<span style="color:yellow;">**</span>Use "medium" or smaller faster-whisper model to comfortably stay within VRAM limits.
{{< /callout >}}

#### Mac
On Mac, Nucleate supports hardware acceleration via Apple Metal (M-Series)/Unified Memory and will fall back to CPU-only support on older platforms (Intel series chips). Both Ollama and Whisper support native Metal acceleration and are strongly recommended. Faster-Whisper transcription does not currently support hardware acceleration on macOS and runs on CPU only.

##### Mac hardware recommendations
| CPU   | RAM (min) | GPU   | VRAM   | Transcription | Summarization    | OpenAI support | Local speed  |
| ------| ----------| ------| -------| ------------- | ---------------- | -------------- | ------------- |
| Any   | <16GB     | -     | -      | -             | -                | Yes            | N/A          |
| Intel<span style="color:red;">**</span> | 16-128GB  | -     | -      | CPU-only      | CPU-only         | Yes            | Slow         |
| M1    | 16-128GB  | Metal | Shared | GPU<span style="color:yellow;">**</span>   | GPU | Yes            | Medium       |
| M2    | 16-128GB  | Metal | Shared | GPU<span style="color:yellow;">**</span>   | GPU | Yes            | Medium       |
| M3    | 16-128GB  | Metal | Shared | GPU<span style="color:yellow;">**</span>   | GPU | Yes            | Fast         |

{{< callout type="info" >}}
<span style="color:red;">**</span>Legacy Mac cannot use Whisper or diarization models, which require PyTorch 2.8.x. The last official release on Intel hardware was PyTorch 2.2.x.

<span style="color:yellow;">**</span>Metal acceleration requires using the "Whisper" backend.
{{< /callout >}}

### OpenAI API
In-app, you can change the default summarization or transcription models to optionally use OpenAI's GPT models, Whisper, or both. These are useful alternatives if you need faster speed or desire higher-quality summaries. However, these options require an internet connection and may may incur usage costs via OpenAI.