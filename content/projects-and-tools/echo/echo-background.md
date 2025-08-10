---
linkTitle: "Background"
type: docs
weight: 1
draft: true
---
## Making "Echo"
### A private project manager for everything
Earlier this year I started Watchlight, a small business that focused on making video games and software for small teams. After a few months, I realized needed a smarter, better way of project tracking that enhanced my speed, identified weaknesses, and kept me on-track. If you've worked in the real world, you probably realize that I'm describing a "Project Manager." It's someone who keeps the team on-track, sees the big picture, and publishes-out status updates. These people can be extremely helpful and are often found at well-resourced companies.

For solo business owners who can't afford the time to do it themselves, being your own project manager is hard... Writing and publishing status updates, remembering everything on the to-do list, and keeping track is time consuming and difficult. The time spent reflecting, organizing, and updating can take more time away from you than it returns! It's an unfair reality and a barrier to many small businesses and solo developers.

>So I did something about it and built "Echo."

"Echo" is an AI-based project manager. I wanted a solution that reduced the time I spent worrying about next steps, progress updates, and project tracking. More importantly, I wanted a solution that was private - where my data was in my control and analyzed on my own machine, no strings attached and no subscriptions required. I hate games that are 'pay-to-play' and feel similarly about subscription software.

### Don't craft, just talk
At it's core, Echo is a lightweight tray application that transcribes audio files and writes summaries like a project manager. I realized it was easier, faster, and more natural to talk about my projects than it was to write everything down. The average person talks at about ~150 words per minute versus the average typing speed of ~40 words per minute (and that assumes you know what to write(!), this page took me about ~4 WPM to draft, proof, polish, and format into markdown). Most people don't know what to say, either, but large language models (LLM) are very good at digesting crude dialog.

Echo distills audio (.mp3, .mp4, .wav) into markdown files that contain summaries, keynotes (such as decisions, actions, and next steps), and raw transcripts. The summaries are automatically tagged so that similar topics can be easily identified and grouped. More powerfully, Echo also pays attention to what's happening week-on-week and month-on-month. It identifies the most important milestones, barriers, and look-ahead items that you're working towards and automatically creates digests and easy-to-read reports.

### Designed for customization
I intended Echo to be extremely modular, so that people with different goals and projects can make it their own. By default, it comes pre-loaded with different user modes to support software developers, small business owners, and personal users who just want to track progress and goals. For everyone else, I built Echo so that you can add your own mode.

>If you're an inventor, an engineer, a social service worker, a therapist, a dungeon master, a bedtime story reader, a college student, the list goes on. If someone's talking, Echo's listening.

In addition to automatic transcription and summarization (your primary user mode), I also added the ability to perform one-off summaries with custom prompting. Echo comes pre-loaded with prompting for Devlogs, Key Notes, Journals, and Meeting summaries. Like the user modes, you can also "build-your-own" prompts and customize Echo to suit your needs. I personally use this mode to occasionally summarize ongoings from my "real job," a separate space that is different from Watchlight Studio.

### Designed for enthusiasts
I designed Echo to run off my own machine so that I could preserve privacy and intellectual property. Audio logs, transcripts, and summaries all remain with me and under my own umbrella. While these goals were important to me, I designed Echo to also be compatible with API-based services. If configured, both transcription and summarization can be run using OpenAI models, removing the need for high-end hardware. The summaries can be excellent, but it does expose your data to OpenAI (for what it's worth).

Echo is natively compatible with both Obsidian and with Notion Integration, depending on your workflow. Obsidian can be setup as an offline-only service (again, in the spirit of privacy). Notion is cloud-based service and requires both internet connection and online server support.

This project has been a delight to make, and Echo has become a core part of my projects and business. For those of you who want to take the plunge, I wish you luck!