---
linkTitle: "Performance Data"
type: docs
weight: 3
---
{{< callout type="info" >}}
There's an [in-app tool](/projects-and-tools/echo/echo-menu/#energy--savings) for measuring transcription and summarization speed.  

To contribute to this page, send your own hardware config and performance data to contact@watchlightstudio.com
{{< /callout >}}
## Summarization performance (TPS)
In-app summarization performance is measured in tokens per second (TPS). On average, a token is ~3/4 of a word, and faster is better. More efficient hardware gives higher TPS, which reduces the amount of time required to perform LLM services. Less time spent thinking means lower energy requirements, and thus less expensive compute.

In general, running local models is less expensive than running with OpenAI API services. If Echo is configured to use OpenAI, the default model is set to GPT3.5-turbo, which is a good balance of quality vs cost. OpenAI charges differently for input vs output tokens, but the approximate cost is ~0.57M tokens/dollar (as of July 2025). The cost of running locally varies, but estimates are provided below.

```bash
Running locally and assuming 250W device, 0.21 cents/kWh
100 TPS => 6.86M tokens/dollar  
50 TPS => 3.43M tokens/dollar  
25 TPS => 1.71M tokens/dollar  
8 TPS => 0.57M tokens/dollar (same as OpenAI pricing)
```

### Example performance
**Local LLM Summarization using a NVIDIA 3090 FE GPU (24GB VRAM):**

|                   | **Mistral**    | **Llama2**     | **LLama2:7B**  |
| ----------------- | -------------- | -------------- | -------------- |
| **Run 1**         | 115.3          | 107.7          | 110.7          |
| **Run 2**         | 92.2           | 128.5          | 123.9          |
| **Run 3**         | 113.2          | 41.5           | 36.8           |
| **Run 4**         | 116.2          | 99.0           | 130.5          |
| **Run 5**         | 113.7          | 130.1          | 133.7          |
| **Average (TPS)** | 110.1 +/- 10.1 | 101.4 +/- 36.0 | 107.1 +/- 40.3 |
## Transcription performance (speed multiplier)
In-app transcription performance is measured as a simple ratio of transcription speed vs audio file length. If it takes 18s to transcribe a 180s audio file, the multiplier is 10x. Similar to TPS, more efficient hardware gives higher multipliers, which reduces the time required to perform analysis, energy, and cost.

The backend for transcription is faster-whisper, which is a derivative of OpenAI's Whisper model. There are several different models that can be used, including: base, small, medium, large-v2, large-v3. In general, there is a tradeoff between model size and accuracy, where larger models are more accurate. Because Echo performs summarization on these transcripts, minor errors are typically ignored or 'washed out.' Medium, large-v2, and large-v3 are all similarly performant, and the default model is set to "medium."

Running local transcription is *far less expensive* than transcribing with OpenAI's Whisper API. OpenAI charges per minute of transcribed audio, at a rate of ~2.8h/dollar as of July 2025). The cost of running locally varies, but estimates are provided below.

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

|                        | **Base**     | **Small**    | **Medium**   | **Larve-v2** | **Large-v3** |
| ---------------------- | ------------ | ------------ | ------------ | ------------ | ------------ |
| **Run 1**              | 53.3         | 37.7         | 20.7         | 20.7         | 15.6         |
| **Run 2**              | 64.1         | 45.6         | 27.8         | 22.5         | 18.5         |
| **Run 3**              | 64.7         | 45.4         | 30.1         | 22.5         | 18.1         |
| **Run 4**              | 70.1         | 45.4         | 28.0         | 18.4         | 18.1         |
| **Average** | 63.1 +/- 7.0 | 43.5 +/- 3.9 | 26.7 +/- 4.1 | 21.0 +/- 1.9 | 17.6 +/- 1.3 |

**Local transcription using an AMD Ryzen 9 7900 (64GB DDR5):**

|                        | **Base** | **Small** | **Medium** | **Larve-v2** | **Large-v3** |
| ---------------------- | -------- | --------- | ---------- | ------------ | ------------ |
| **Run 1**              | 25.2     | 9.4       | 3.6        | 1.6          | 1.6          |
| **Run 2**              | 23.3     | 7.6       | 2.8        | 1.6          | 1.3          |
| **Average** | 24.2     | 8.5       | 3.2        | 1.6          | 1.4          |