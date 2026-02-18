---
linkTitle: "Compatibility"
type: docs
weight: 1
slug: "compatibility-cheat-sheet"
url: "/nucleate/setup-and-compatibility/compatibility-cheat-sheet"
---
## Compatibility Cheat Sheet
This page provides a quick overview of which features are available on different hardware configurations. These indicators describe **capability and support**, not performance guarantees.

When possible, Nucleate automatically optimizes settings for your system.

### Recommended Configurations

These configurations provide the best balance of compatibility, performance, and flexibility for local transcription, summarization, and analysis.

|Capability ↓ /// Hardware → (>16GB RAM)|Win CUDA<sup>*</sup>|Metal Mac|Win No CUDA|Intel Mac|
|---|---|---|---|---|
|Faster-Whisper (CPU)|✅|✅|✅|✅|
|Faster-Whisper (GPU)|✅|❌|❌|❌|
|Whisper (CPU)|✅|✅|✅|❌|
|Whisper (GPU / MPS)|✅|✅|❌|❌|
|Transcription: base → large-v3-turbo|✅|✅|✅|✅|
|Ollama (local)|✅|✅|✅|✅|
|Ollama Overdrive|✅|✅|✅|✅|
|Diarization (CPU)|✅|✅|✅|❌|
|Diarization (GPU/MPS)|✅|✅|❌|❌|
|OpenAI API|✅|✅|✅|✅|

{{< callout type="info" >}}
• <sup>*</sup>Windows CUDA (≥16GB RAM, ≥8GB VRAM)  
• On Windows, Ollama Overdrive stores models in memory and benefits from ≥16GB of memory.  
• Faster-Whisper GPU acceleration is only available on Windows with CUDA.  
• On macOS, GPU acceleration requires the Whisper backend and Apple Metal.  
• Intel Macs cannot run Whisper or diarization models due to PyTorch limitations.  
{{< /callout >}}

### CUDA GPU VRAM Guidance (Windows)

These are recommendations for Windows systems with NVIDIA CUDA-capable GPUs. Nucleate will automatically adapt to available VRAM when possible.

| GPU VRAM | Expected experience |
|---------|---------------------|
| 8GB | Fully supported. Best results with base, small, or medium transcription models. Large models may require reduced batch sizes. |
| 12GB | Ideal baseline for most workflows. Supports all transcription models and GPU diarization comfortably. |
| 16GB+ | Best overall experience. Fastest local transcription, diarization, and large-model summarization with minimal constraints. |


### Limited / Low-Memory Configurations

The following configurations are supported, but functionality is constrained and performance may be significantly reduced. These setups are best suited for lighter workloads or OpenAI-backed processing.

|Hardware|Key limitations|
|---|---|
|Intel Mac (8GB)|Faster-Whisper (CPU) only; base/small transcription models; no Whisper or diarization support; Ollama Overdrive not recommended|
|Apple Silicon Mac (Metal, 8GB)|Whisper GPU supported but limited to base/small models; Ollama Overdrive not recommended|
|Windows (No CUDA, 8GB)|CPU-only transcription; base/small models only; Ollama Overdrive not recommended|
|Windows (CUDA, 8GB VRAM)|GPU acceleration supported, but limited to base/small transcription models|