---
linkTitle: "Performance"
type: docs
weight: 4
slug: "performance"
url: "/nucleate/how-it-works/performance"
---
{{< callout type="info" >}}
There's an [in-app tool](/nucleate/help/menu/#performance-calculator) for measuring transcription and summarization speed.  

To contribute to this page, send your own hardware config and performance data to contact@watchlightstudio.com
{{< /callout >}}
## Summarization performance (TPS)
In-app summarization performance is measured in tokens per second (TPS). On average, a token is ~3/4 of a word, and faster is better. More efficient hardware gives higher TPS, which reduces the amount of time required to perform LLM services. Less time spent thinking means lower energy requirements, and thus less expensive compute.

In general, running local models is less expensive than running with OpenAI API services. If Nucleate is configured to use OpenAI, the default model is set to GPT3.5-turbo, which is a good balance of quality vs cost. OpenAI charges differently for input vs output tokens, but the approximate cost is ~0.57M tokens/dollar (as of July 2025). The cost of running locally varies, but estimates are provided below.

```bash
Running locally and assuming 250W device, 0.21 cents/kWh
100 TPS => 6.86M tokens/dollar  
50 TPS => 3.43M tokens/dollar  
25 TPS => 1.71M tokens/dollar  
8 TPS => 0.57M tokens/dollar (same as OpenAI pricing)
```

### Example performance
**Local LLM Summarization using a NVIDIA 3090 FE GPU (24GB VRAM):**

|                   | **Mistral**    | **+Overdrive** |
| ----------------- | -------------- | -------------- |
| **Run 1**         | 86             | 132            |
| **Run 2**         | 88             | 153            |
| **Run 3**         | 98             | 142            |
| **Run 4**         | 92             | 146            |
| **Run 5**         | 86             | 140            |
| **Average (TPS)** | 90 +/- 5.1     | 142 +/- 7.7    |

**Local LLM Summarization using a NVIDIA 3060 Laptop GPU (6GB VRAM):**


## Transcription performance (speed multiplier)
In-app transcription performance is measured as a simple ratio of transcription speed vs audio file length. If it takes 18s to transcribe a 180s audio file, the multiplier is 10x. Similar to TPS, more efficient hardware gives higher multipliers, which reduces the time required to perform analysis, energy, and cost.

There are two possible backends for transcription, Whisper and Faster-Whisper. Whisper is natively compatible on both Mac and Windows and enables hardware acceleration on both. Faster-Whisper is optimized on Windows and enables slight speed improvements for GPU-accelerated support and substantial improvements on CPU-only transcription.
	{{< callout type="info" >}}
	Whisper requires FFmpeg to be installed per the python openai-whisper dependency. I cannot ship FFmpeg as part of the app, but it is easily downloaded [following these instructions.](/nucleate/setup-and-compatibility/ffmpeg-ffprobe)
	{{< /callout >}}

There are several different models that can be used on both Whisper and Faster-Whisper, including: base, small, medium, large-v3, and large-v3-turbo. In general, there is a tradeoff between model size and accuracy, where larger models are more accurate but generally slower. Because Nucleate performs summarization on transcripts, minor errors are typically ignored or 'washed out' by the LLM. Medium, large-v3, and large-v3-turbo are all similarly performant. The default model is set to "medium" for Nucleate Pro users if adequate VRAM or RAM is detected.

Running local transcription is *far less expensive* than transcribing with OpenAI's API. OpenAI charges per minute of transcribed audio, at a rate of ~2.8h/dollar as of July 2025). The cost of running locally varies, but estimates are provided below.

```bash
Running locally and assuming 250W device, 0.21 cents/kWh
50 xMultiplier => 952h/dollar  
25 xMultiplier => 476h/dollar  
10 xMultiplier => 190h/dollar  
1 xMultiplier => 19h/dollar  
0.15 xMultiplier => 2.8h/dollar (same as OpenAI pricing)
```

### Example performance
**Local transcription using a NVIDIA 3090 FE GPU (24GB VRAM):**

| Whisper            | **Base**    | **Small**   | **Medium**  | **Large-v3** | **Large-v3-turbo**   |
| ------------------ | ----------- | ----------- | ----------- | ------------ | -------------------- |
| Model size         | 0.7 GB      | 1.8 GB      | 4.7 GB      | 9.7 GB       | 9.7 GB               |
| ------------------ | ----------- | ----------- | ----------- | ------------ | -------------------- |
| Run 1              | 27.10       | 17.79       | 10.25       | 6.24         | 4.73                 |
| Run 2              | 21.68       | 17.91       | 9.58        | 5.41         | 6.13                 |
| Run 3              | 30.09       | 18.34       | 10.47       | 6.33         | 5.36                 |
| Run 4              | 28.85       | 19.18       | 10.17       | 5.60         | 4.35                 |
| Average            | 26.9 ± 3.7  | 18.3 ± 0.6  | 10.1 ± 0.4  | 5.9 ± 0.5    | 5.1 ± 0.8            |

| Faster-Whisper     | **Base**    | **Small**   | **Medium**  | **Large-v3** | **Large-v3-turbo**   |
| ------------------ | ----------- | ----------- | ----------- | ------------ | -------------------- |
| Model size         | 0.5 GB      | 0.9 GB      | 2.0 GB      | 3.7 GB       | 1.9 GB               |
| ------------------ | ----------- | ----------- | ----------- | ------------ | -------------------- |
| Run 1              | 36.74       | 27.66       | 17.64       | 12.99        | 24.57                |
| Run 2              | 31.88       | 28.12       | 18.21       | 10.74        | 27.25                |
| Run 3              | 35.93       | 28.30       | 18.23       | 14.09        | 27.49                |
| Run 4              | 27.82       | 24.78       | 16.14       | 12.47        | 27.63                |
| Average            | 33.1 ± 4.1  | 27.2 ± 1.6  | 17.6 ± 1.0  | 12.6 ± 1.4   | 26.7 ± 1.5           |

**Local transcription using a Ryzen 7900 CPU (12 core):**

| Whisper            | **Base**    | **Small**   | **Medium**  | **Large-v3** | **Large-v3-turbo**   |
| ------------------ | ----------- | ----------- | ----------- | ------------ | -------------------- |
| Model size         | 1.0 GB      | 2.0 GB      | 5.6 GB      | 9.6 GB       | 5.1 GB               |
| ------------------ | ----------- | ----------- | ----------- | ------------ | -------------------- |
| Run 1              | 12.34       | 5.49        | 2.34        | 0.61         | 1.72                 |
| Run 2              | 12.57       | 5.87        | 2.49        | -            | -                    |
| Run 3              | 12.64       | 5.93        | 2.43        | -            | -                    |
| Average            | 12.5 ± 0.2  | 5.8 ± 0.2   | 2.4 ± 0.1   | 0.6 ± NA     | 1.7 ± NA             |

| Faster-Whisper     | **Base**    | **Small**   | **Medium**  | **Large-v3** | **Large-v3-turbo**   |
| ------------------ | ----------- | ----------- | ----------- | ------------ | -------------------- |
| Model size         | 0.5 GB      | 0.8 GB      | 1.5 GB      | 2.4 GB       | 1.7 GB               |
| ------------------ | ----------- | ----------- | ----------- | ------------ | -------------------- |
| Run 1              | 16.07       | 7.10        | 2.66        | 1.60         | 2.32                 |
| Run 2              | 19.87       | 6.79        | 3.16        | -            | -                    |
| Run 3              | 16.89       | 8.39        | 2.58        | -            | -                    |
| Average            | 17.6 ± 2.0  | 7.4 ± 0.8   | 2.8 ± 0.3   | 1.6 ± NA     | 2.3 ± NA             |

**Local transcription using a 2020 Macbook Pro (Intel x86, 8GB):**

| Faster-Whisper     | **Base**    | **Small**   | **Medium**  | **Large-v3** | **Large-v3-turbo**   |
| ------------------ | ----------- | ----------- | ----------- | ------------ | -------------------- |
| Model size         | - GB        | - GB        | - GB        | - GB         | - GB                 |
| ------------------ | ----------- | ----------- | ----------- | ------------ | -------------------- |
| Run 1              | 11.25       | 3.99        | 1.46        | -            | -                    |
| Run 2              | 11.28       | 4.06        | 1.49        | -            | -                    |
| Run 3              | 11.19       | 4.10        | 1.48        | -            | -                    |
| Average            | 11.2 ± 0.1  | 4.1 ± 0.1   | 1.5 ± 0.1   | -            | -                    |