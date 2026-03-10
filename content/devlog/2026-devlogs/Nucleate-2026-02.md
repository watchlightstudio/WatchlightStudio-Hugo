---
linkTitle: "Nucleate - 2026-02"
type: docs
---

## Overview

February was a month of significant development as I focused on packaging the app for Windows and enhancing the user experience through beta testing. I spent a lot of time addressing compatibility issues, particularly with Mac systems, while also refining the app's features and user feedback mechanisms. Overall, it felt like a month of laying down the groundwork for a smoother user experience and better performance.

## Highlights & Progress

### Tools & Workflow
- Successfully packaged the app for Windows CPU-only systems using PyInstaller, which was a crucial step in making the app more accessible.
- Created beta forms and feedback forms to gather insights from users testing the app, which helped shape future updates.
- Developed a dedicated beta page within the app to showcase critical feedback, making it easier for users to see how their input is being utilized.
### Systems & Features
- Updated the Gumroad page and added a bug report submission form directly in the app, streamlining the feedback process.
- Worked on compatibility charts, installation manuals, and simplified system requirements to help users better understand what they need to run the app.
- Added around 20 additional insights to the free version of the app and made the decision to offer diarization for free, which I believe will enhance user engagement.
### Technical Improvements
- Implemented a new hub event signal to group related content IDs, which should improve processing efficiency.
- Refactored the Whisper functionality by moving all primary backends into subprocesses, aiming to streamline the workflow and improve performance.
- Investigated abort functions for speaker identification on Mac, as I noticed a 50-50 success rate that needed addressing.
- Tested a debounce timer to manage state changes, which helped in reducing persistent bugs.
### Challenges
- Encountered issues with PyTorch and Pyannote on Mac and Intel hardware, which raised questions about compatibility and performance.
- Faced challenges in finding FFmpeg and FFprobe binaries that comply with GPL requirements, complicating the packaging process.
- Struggled with packaging issues on Macs with Apple Silicon, particularly concerning Whisper and Torch dependencies.
- Dealt with performance issues on Metal, especially with Ollama, which was slower than expected.
## Reflections

This month was a mixed bag of progress and challenges. I was pleased with the strides made in packaging and user feedback, but the ongoing issues with Mac compatibility were frustrating. It was surprising to see how many dependencies could complicate what I thought would be straightforward packaging. I also realized that offering more features for free could be a double-edged sword; while it may attract more users, I need to ensure that it doesn't compromise the app's performance or my ability to support it.

## Next Steps

- Investigate solutions for the issues with PyTorch and Pyannote on Mac and Intel hardware to improve compatibility.
- Address the performance concerns with Ollama on Metal to enhance user experience.
- Explore the implications of user licensing changes on app performance and features to ensure sustainability.
- Continue refining the beta testing process based on user feedback to guide future development.

> Generated with `Nucleate by Watchlight Studio` — distilled from full transcription.
---
