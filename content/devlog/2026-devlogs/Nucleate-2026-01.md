---
linkTitle: "Nucleate - 2026-01"
type: docs
---

## Overview

This month has been a blend of polishing Nucleate's user experience and tackling technical hurdles, particularly around cross-platform compatibility. I focused on enhancing features, especially around transcription and diarization, while also addressing some persistent issues on the Mac side. The month was marked by a shift in testing approaches and a deeper integration of various audio processing technologies.

## Highlights & Progress

### Tools & Workflow
- Polished the app's stylization and resolved several Mac-related issues, which has been a long-standing pain point.
- Created a single point of contact theme class for easier customization, streamlining the styling process.
- Updated the website and documentation materials for Nucleate's features.
### Systems & Features
- Added new features like Ollama detection, an Ollama overdrive toggle, and gated diarization behind pro features.
- Addressed additional bugs specifically affecting the Mac version of the app.
- Integrated OpenAI's Whisper and Faster Whisper for transcription, as well as resolved diarization subprocess woes in the app.
- Implemented M4A file conversion into .wav and normalized backend transcription processing.
### Experiments
- Successfully tested diarization via pyannote audio on CPU and on GPU.
- Upgraded to the GPU package for torch and identified CUDA version 11.1 for GPU compatibility, although I faced some limitations with Torch options on Mac.
### Roadblocks
- Encountered inconsistencies in app performance between Windows and Mac, which has been frustrating and requires further investigation.
- Faced dependency issues on Mac, leading to a workaround using a virtual environment and CPU-only Torch builds on Intel Mac hardware.
- OpenAI Whisper's incompatibility with Intel Macs led to the decision to make Faster Whisper available to all users, which feels like a necessary compromise.
## Reflections

Overall, I feel like I made solid progress this month, especially in terms of feature development and improving the user interface. However, the ongoing issues with Mac compatibility have been a significant roadblock. I was surprised by how much I had to pivot my approach to testing and development, particularly with the CPU-based strategies. The decision to gate certain features behind a pro tier is still up in the air, as I’m weighing the benefits of making hardware-accelerated transcription more widely available. 

## Next Steps

- Continue addressing the ongoing bugs on the Mac side and investigate the VRAM spike during diarization.
- Finalize decisions around the accessibility of hardware-accelerated transcription and the gating of features.
- Reach out to potential testers on Reddit to form a small beta group for user feedback.
- Enhance the reliability of diarized insights and explore when to create marketing animations for the app.

> Generated with `Nucleate by Watchlight Studio` — distilled from full transcription.
---
