---
linkTitle: "Background"
type: docs
weight: 1
slug: "background"
url: "/nucleate/overview/background"
---
## Making "Nucleate"

### Talk about anything and everything

In 2025, I started Watchlight — a small studio focused on making video games and software for small teams. After a few months, I realized needed a smarter, better way of project tracking that enhanced my speed, identified weaknesses, and kept me on-track. If you've worked in the real world, you probably realize that I'm describing a project manager. It's someone who keeps the team on-track, sees the big picture, and publishes-out status updates. These people can be extremely helpful and are often found at well-resourced companies.

For solo founders and small businesses who can't afford the time to do it themselves, being your own project manager is hard. Writing and publishing status updates, remembering everything on the to-do list, and keeping track is time consuming and difficult. The time spent reflecting, organizing, and updating can take more time away from you than it returns! It’s an unfair reality and a real barrier for people building on their own.

>So I did something about it and built "Nucleate."

To me, Nucleate is a personal, AI-based project manager. I wanted a solution that reduced the time I spent worrying about next steps, progress updates, and project tracking. More importantly, I wanted a solution that was private - where my data was in my control and analyzed on my own machine, no strings attached and no subscriptions required. I hate games that are 'pay-to-play' and feel similarly about subscription software.

To you, Nucleate can be whatever you need it to be.

### Don't craft, just talk
At its core, Nucleate is a tray application that transcribes audio and writes summaries. I realized it was faster and more natural to talk through my work than to sit down and write everything out.

The average person talks at about ~150 words per minute versus the average typing speed of ~40 words per minute (and that assumes you know what to write(!), this page took me about ~4 WPM to draft, proof, polish, and format into markdown). Most people don't know what to say, either, but large language models (LLM) are very good at digesting crude dialog.

With Nucleate, you just talk.

Nucleate converts audio files (.mp3, .mp4, .wav, .m4a) into Markdown files that contain summaries, keynotes (such as decisions, actions, and next steps), and raw transcripts. Disjointed ideas begin to coalesce. Topics are grouped, tagged, and optionally passed through a set of focused "Insights" that produce tuned, high-value content.

Over time, Nucleate also pays attention to patterns. It looks week-on-week and month-on-month to identify the most important milestones, barriers, and look-ahead items that you're working towards. From that, it automatically produces digests and structured reports without having to manually curate.

### Designed for customization

I intended Nucleate to be extremely modular, so people with different goals, projects, and interests can make it their own. By default, it includes more than 20 user modes designed for software developers, small business owners, students, program managers, and personal users who simply want to track progress and goals. 

For everyone else, I built Nucleate so that you can add your own mode. An astronaut passionate about extraterrestrial agriculture? You’re covered, Mark Watney.

> If you’re an inventor, an engineer, a social service worker, a therapist, a D&D nut, a bedtime-story reader, a college student… it doesn’t matter who you are or what you’re passionate about. Just start talking.

"Insights" are one of the most powerful parts of Nucleate. There are over 45 distinct Insights, covering everything from key points and decisions to bug tracking, progress summaries, stakeholder feedback, etc. Each built-in user mode comes preconfigured with notes I thought would be useful, but you can mix and match freely.

**Smart Insights** was my attempt at reducing customization overload... Rather than worrying about exactly which Insights you want per-summary, this optional pre-pass analyzes the target content and automatically selects the most relevant Insights. It's a powerful tool, and I use it exclusively to select Insights.

Alongside the automated workflow, I also built **Nucleate Lab**. The Lab is a sandbox for one-off transcription, summarization, and experimentation. You can try different user modes, notes, and models without disrupting your main workflow (your primary user mode). I personally use it to summarize work from my day job — a separate space from Watchlight Studio. Like user modes, Lab profiles are fully customizable.

### Designed for enthusiasts

I designed Nucleate to run off my own machine so that I could preserve privacy and intellectual property. Audio logs, transcripts, and summaries all remain with me and under my own umbrella. While these goals were important to me, I did build-in compatibility with API-based services. If configured, both transcription and summarization can be run using OpenAI models, removing the need for high-end hardware. The summaries can be excellent, but it does expose your data to OpenAI (for what it's worth).

Nucleate is also natively compatible with both Obsidian and Notion. Obsidian can be used fully offline and aligns to a privacy-first workflow. Notion is cloud-based and requires an internet connection, but offers a familiar and flexible workspace for many users. I use Obsidian as my primary endpoint, which allows me to pull-in Nucleate summaries directly into my Watchlight space.

This project has been a joy to build, and Nucleate has become a core part of my own projects and business. **Nucleate Pro** is available on Gumroad and Itch and runs on both Windows and Mac. If you just want to try it out, the core Nucleate experience is free with limited functionality.