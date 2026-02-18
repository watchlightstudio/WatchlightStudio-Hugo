---
linkTitle: "Cloud & mobile"
type: docs
weight: 6
url: "/nucleate/setup-and-compatibility/cloud"
---
## Cloud-based workflow and mobile integration

Nucleate can be used entirely hands-free with a cloud-based workflow, allowing you to **record audio on your phone anywhere** and have it automatically transcribed and summarized on your primary machine.

This approach works with any major cloud storage provider (Google Drive, OneDrive, Box, Dropbox, etc.) and does not require paid apps. Premium sync or recording apps can improve reliability and reduce ads, but are optional.

Once configured, this workflow is highly robust and well suited for:
- Walking notes
- Commute reflections
- Meetings or lectures away from your desk
- Quick, unplanned recordings

The goal is simple: **capture thoughts when they happen**, without managing files manually.

## Core cloud-based workflow

1. Choose a cloud storage provider  
   Any provider that supports desktop and mobile sync will work. Since Nucleate outputs Markdown files (typically 2–20 KB each), storage requirements are minimal.

2. Create cloud folders  
   - One folder for **incoming audio**
   - One or more folders for **summary outputs**  
   Nucleate supports up to five output directories, configurable in-app.

{{< callout type="warning" >}}
If you rename or move folders, be sure to update the paths in Nucleate:  
**Menu → File Sync → Folder settings**
{{< /callout >}}

3. Enable desktop sync  
   On the machine where Nucleate is installed, enable your cloud provider’s desktop sync so files appear locally in Explorer (Windows) or Finder (macOS). Ensure two-way sync is active.

4. Configure Nucleate folders  
   - Set the **incoming audio folder** to the synced cloud directory  
   - Set summary output folders to synced cloud locations  
   - Optionally set an **audio archive folder** for completed recordings

5. Record and forget about it  
   When a new audio file appears in the cloud:
   - Nucleate automatically detects it
   - Transcription and summarization run locally
   - Summaries are saved in-app and synced back to the cloud

{{< callout type="info" >}}
After transcription completes, audio files can be moved out of the cloud and archived locally to keep cloud storage lightweight.
{{< /callout >}}

## Android setup (cloud-based recording)

1. Install a cloud sync app  
   Use a sync app that can mirror a cloud folder to local storage.  
   One option is [BoxSync Pro](https://play.google.com/store/apps/details?id=com.ttxapps.boxsync&hl=en&pli=1), which supports two-way sync. The free version works; the paid version removes ads.

2. Install a recording app  
   Choose a recorder that allows saving files to a specific folder, such as  
   [Easy Voice Recorder](https://play.google.com/store/apps/details?id=com.coffeebeanventures.easyvoicerecorder&hl=en_US).

3. Match save directories  
   Configure the recorder to save audio files into the same local folder used by the sync app.

Once configured:
- Record audio on your phone
- Files sync automatically to the cloud
- Nucleate picks them up and processes them without manual steps

## iPhone / iPad setup

Mobile workflows on iOS are more constrained due to platform sandboxing.

At minimum, the workflow requires:
- A cloud storage app with background uploads
- A recording app that can save or share files directly into that cloud location

Detailed iOS setup examples will be added in a future update.

## Example: Box + Obsidian workflow (recommended)

This is the author’s primary workflow and is well suited for users who already use Obsidian.

### Desktop setup

1. Create a [Box](https://www.box.com/home) account (if needed)
2. Install and configure [Box Sync](https://support.box.com/hc/en-us/articles/360043697194-Installing-Box-Sync) on the machine running Nucleate
3. Inside the synced Box directory, create a folder to serve as your **Obsidian Vault**

{{< callout type="info" >}}
Optional: Create subfolders inside the vault for daily, weekly, monthly, or lab summaries.
{{< /callout >}}

4. Configure Nucleate:
   - Incoming audio folder → Obsidian Vault
   - Summary output folders → Obsidian subfolders

When audio files appear in the vault, Nucleate processes them and writes summaries back into Obsidian automatically.

### Android setup (Box + Obsidian)

1. Install [BoxSync Pro](https://play.google.com/store/apps/details?id=com.ttxapps.boxsync&hl=en&pli=1)
2. Install the [Obsidian](https://play.google.com/store/apps/details?id=md.obsidian&hl=en) app
3. Open the synced Box folder as an Obsidian Vault

With this setup:
- The same Obsidian Vault exists on mobile, cloud, and desktop
- Audio recorded in Obsidian syncs automatically
- Nucleate processes recordings and returns summaries to the vault

If Nucleate is configured to archive processed audio, completed recordings will be removed from the vault automatically after processing.

## Summary

Cloud-based workflows allow Nucleate to function as a **mobile-first capture tool** with zero manual file handling. Once configured, recording is fast, frictionless, and reliable — making it easier to build consistent habits around audio notes.