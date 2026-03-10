---
linkTitle: "Nucleate - 2025-04"
type: docs
---
## Overview

This month was primarily focused on developing local large language models (LLMs) for various tasks, including speech-to-text transcription, summarization, and patent drafting. I spent a lot of time experimenting with different models and features, which led to some interesting breakthroughs but also highlighted several challenges that need addressing. The ongoing struggle with token limits and app stability became prominent themes as I navigated through the development process.

## Highlights & Progress

### Tools & Workflow
- I started using the Whisper-large 3 model for transcription tasks. While it successfully transcribes audio files, I've encountered issues with pause timing and crashes when notifications are added.
- To improve flexibility, I modified the transcription script to accept a configuration file, which has made it easier to adjust settings on the fly.
- I explored packaging the transcription script as a system tray-only application, which could streamline access and usability.
### Systems & Features
- I began building a multi-file analyzer for LLM Scribe aimed at achieving publication-level quality. However, I faced significant token limit issues when trying to handle multiple files, which range from 4,000 to 8,000 tokens.
- Developed a semi-automated system using Python for summarizing transcripts, which integrates with the LLM. This has been a promising step towards automating some of the more tedious aspects of the workflow.
- Added new features to the local language model scribe, including toggling transcription on/off and scheduling summaries, which have improved the overall user experience.
### Experiments
- I explored using alternative models like Mistral and Mixtral for text-to-speech tasks, hoping to find better performance or quality.
- Tried out Easy Auto Record on my phone for faster audio logging instead of relying on Obsidian.

### Roadblocks
- The app has been crashing when notifications are added, which has been frustrating and has raised questions about how to effectively integrate the LLM into my workflow.
- I found myself struggling with whether to continue focusing on the local scribe app or shift back to AutoTerrainer, as both projects have their merits and challenges.
- Open questions remain regarding the performance impact of compression on LLM Scribe and the effectiveness of custom summarizers.
## Reflections

Looking back, I can see that the month was a mixed bag. I made some solid progress in terms of features and flexibility, but the stability issues with the app and the token limit challenges were significant setbacks. I was surprised by how much the integration of notifications affected the app's performance, and it’s clear that I need to rethink that aspect. My thinking has evolved towards a more modular approach, where I can test different components independently to see what works best without causing crashes.

## Next Steps

- Continue refining the transcription script and address the crashing issues when notifications are added.
- Investigate the token limit issues further and explore ways to handle larger data sets more effectively.
- Decide whether to prioritize the local scribe app or shift focus back to AutoTerrainer based on the progress made.
- Experiment with the performance impact of compression on LLM Scribe and evaluate the effectiveness of custom summarizers.
- Further explore the potential of the Mistral and Mixtral models for text-to-speech tasks.

> Generated with `Nucleate by Watchlight Studio` — distilled from full transcription.
---
