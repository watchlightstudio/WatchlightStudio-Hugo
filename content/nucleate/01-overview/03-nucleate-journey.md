---
linkTitle: "Dev journey"
type: docs
weight: 5
slug: "journey"
---
## Humble beginnings

Nucleate is the product of months of building, tuning, testing—and re-inventing.

>Is a transcription and summarization app all that hard to make?
>Not really.
>
>Did I manage to make it hard anyway?
>Absolutely!

All told, Nucleate has been written (or rewritten) three times.

The **first version** was a backend-only set of scripts: a simple pipeline that transcribed my Obsidian audio notes and produced short summaries. It worked—but only for _me_. No UI, no flexibility, no ambition beyond “get text out.”

The **second version** became a Tkinter-based tray app. This is where Nucleate started to feel like a product instead of a script. Customization appeared. Early “special notes” were introduced (the early version of today’s _Insights_). Tagging, config management, and basic AI engine flexibility followed.

This phase forced a lot of “responsible developer” growth—cleaner data handling, fewer assumptions, better structure. At the time, I genuinely thought this version (then called **Echo**) might ship as a small, focused devlog tool.

And yet, scope creep...

The **third version** was a full reset. As features expanded, Tkinter stopped being the right foundation. I migrated the app to PySide6 and rebranded the project from _Echo_ to **Nucleate**. What I thought was a “finished” app was actually noodle after noodle of spaghetti code.

Only after this third iteration did the app really start to mature. Deep customization, a full suite of Insights, diarization, cross-platform support, automated setup flows, proper error handling, state management, in-app recording, and far more flexibility than the original vision allowed. Content and customization blossomed.

>Nucleate isn’t the result of chasing features—it’s the result of chasing clarity.

And now, here we are. Nucleate is entering beta—and for the first time, it feels _ready to be shared_.

## Development stats

I like data! See the stats that went into Nucleate pre-release.

### Git commits
See heat map of git commits vs time.

### Lines of Code
See figure of lines of code vs time.

### Logged Dev hours
See clockify number of logged hours.