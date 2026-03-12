---
linkTitle: "Nucleate - 2026-02"
type: docs
---

## Overview

February was a month of both progress and challenges as I worked towards getting the app ready for release. The main focus was on improving compatibility across various platforms, tackling technical issues, and refining the overall user experience. I also took steps to build a dedicated beta page within the app, which has been crucial for identifying beta users and managing downloads.

## Highlights & Progress

### Tools & Workflow
- Built a dedicated beta page within the app to streamline the process of identifying beta users. This included implementing abort buttons for downloads and sub-processes, which should help manage user experience during testing.
- Made the decision to not bundle FFmpeg or FFpro due to GPL requirements, which has implications for how I approach licensing and app size going forward.
### Systems & Features
- Diarization was offered for free, with speaker identification available as an optional toggle. I limited the free auto notes feature to three summaries per week.
- Implemented a toggle for light and full modes in the custom user mode, and moved the import/export buttons to the user mode creation menu.
- Set faster whisper as the default option for most users.
### Technical Challenges
- Investigated PyTorch and pyannote imports on Mac with Intel hardware.
- Encountered speed related concerns with Ollama on Mac.
- Dealt with GUI flicker issues caused by the app subprocess launching events, which has been frustrating and needs a more permanent fix.
- Noted a significant issue where failed or incomplete processes return an empty string instead of stopping/aborting, which could lead to confusion if not addressed.
## Reflections

This month has been a mixed bag. On one hand, I made some solid progress in terms of features and user experience, particularly with the beta page and custom user modes. On the other hand, the technical challenges, especially with CUDA support and GUI stability, have been a bit of a setback. I was surprised at how much time was consumed by these issues, which made me rethink my approach to testing and compatibility across different hardware.

The decision to offer diarization for free has raised some open questions about app size and licensing that I need to explore further. It’s clear that I need to finalize the number of beta testers and their hardware requirements soon to move forward effectively.

## Next Steps

- Resolve the Whisper processing issues to ensure a smoother user experience.
- Finalize the number of beta testers and establish their hardware requirements.
- Investigate the implications of app size and licensing after the decision to give diarization for free.
- Continue addressing the GUI flicker and the empty string issue for failed processes.
- Prepare for testing the app on a Mac with metal hardware to evaluate performance improvements.

> Generated with `Nucleate by Watchlight Studio` — distilled from full transcription.
---
