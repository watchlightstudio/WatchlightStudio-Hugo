---
linkTitle: "Nucleate - 2025-04"
type: docs
---

## Overview

This month, I focused on refining the Local Language Model Scribe project, which aims to streamline workflow in game development by improving the transcription and summarization of audio files. I spent a lot of time exploring various local language models for speech-to-text and summarization, integrating new tools into existing systems, and tackling some bugs and performance inconsistencies that arose during development.

## Highlights & Progress

### Tools & Workflow
- I established a workflow where audio files are transcribed directly into Obsidian using a script and Faster Whisper. This setup has been functioning well, producing time-stamped transcripts based on pauses in the audio.
- I decided to use Obsidian for text-to-speech and note organization, which has helped in keeping everything organized and accessible.
- Integrated a tagging system within the Python script to help categorize transcripts, though this is still a work in progress.
### Systems & Features
- The transcription script is working effectively, and I've set up a system where the summarization of transcripts is handled by a large language model. The results are saved to a separate folder in Obsidian, which has helped in managing the outputs.
- I downloaded and tested the Whisper model for text-to-speech conversion, which has shown promise in improving the quality of audio outputs.
### Experiments
- I experimented with Obsidian's built-in text recognition functions to see if they could streamline the transcription process further.
- I also considered using the Mistral Q4 model as an alternative to enhance performance, although I haven't fully committed to that yet.
### Roadblocks
- I encountered several bugs and performance inconsistencies during development, particularly with formatting issues in the transcripts and challenges with single file summaries. These have been frustrating and are still open questions that need addressing.
## Reflections

Looking back, I realize that while the transcription workflow is largely functional, the bugs and inconsistencies have been a significant source of frustration. I was surprised by how much time I spent troubleshooting these issues rather than moving forward with new features. My thinking has shifted towards prioritizing stability and usability in the tools I’m developing. I also need to clarify my strategy regarding the program manager AI agent and how to implement backlinks effectively using tools like KeyBert.

## Next Steps

- Resolve the formatting bugs in transcripts and find a solution for issues with single file summaries.
- Continue refining the tagging system within the Python script.
- Evaluate the flexibility of the language models for different tasks and contexts.
- Make decisions regarding the program manager AI agent and the implementation of backlinks.
- Develop a naming and visibility strategy for Watchlight Studio.

> Generated with `Nucleate by Watchlight Studio` — distilled from full transcription.
---
