---
linkTitle: "03 Cloud/mobile"
slug: "cloud"
type: docs
weight: 6
---
## Cloud-based workflow and phone integration
To get the most out of Echo, I setup my workflow so that I can record on my phone anywhere/anytime and it automatically gets processed via Echo. I subscribe to cloud-based storage using Box, but this approach should work for any cloud-service, including free options (Google Drive, OneDrive, etc). The below configuration does not require any additional paid apps, but I do pay for some pro/premium versions to help support the devs and reduce ads.

It may sound a bit scary, but once setup this process is extremely robust and makes it easy to whip out your phone on the road, on a walk, or during other quiet time. Being mobile makes it easy to work "on the fly" without having to schedule time to sit down, record, and move files around. Make it easy on yourself - you're already working hard enough!

### Core workflow for cloud-based Echo
- Select your preferred cloud-based storage app (Google Drive, OneDrive, Box, Dropbox, etc). Echo produces markdown files, which are very small (2-20 KB on average), and so not much storage is needed. I have a folder of 57 summaries, and the size is only 539KB.
- In your storage app, create at least one new folder for incoming .mp4 files. If "Simple" setup was used during first time install, this will also be the default output folder. Echo can support up to five output directories, if desired, which can be set within the app.

{{< callout type="warning" >}}
If you change folder names, remember to update them in the app:  
(menu) Advanced Settings/Directory & Sync/Set folders
{{< /callout >}}
- On the machine where Echo is installed, setup a cloud-to-desktop sync service that is supported by your preferred cloud client and allows you to view your cloud files in Windows Explorer. Ensure that the sync service is active and performs two-way synchronization (most do).
- In Echo, set output folders to point to the cloud. Also, select a directory that you can use to store the old .mp4 files once they have been transcribed and are no longer needed.
- Anytime a new audio file is added to the cloud, it is automatically detected by Echo, transcribed and summarized on the local machine. When complete, a summary is saved in the Echo app folder and a copy is pushed back to the cloud.

{{< callout type="info" >}}
When transcription is complete, the .mp4 in the cloud can be transferred to a different destination folder. I recommend a backup hard drive to de-clutter the cloud.
{{< /callout >}}

### Setup Android integration for cloud-based support
- Download a mobile sync service that is supported by your preferred cloud client. Whatever app you choose should be able to write locally to a folder on your phone. I use [BoxSync Pro](https://play.google.com/store/apps/details?id=com.ttxapps.boxsync&hl=en&pli=1). This 3rd party app allows me to two-way sync my Box account onto my phone. The app is free, but the paid version is inexpensive and professional. There are other apps by the same developer to support your preferred cloud client.
- Download a recording app like [Easy Voice Recording](https://play.google.com/store/apps/details?id=com.coffeebeanventures.easyvoicerecorder&hl=en_US) that allows you to save audio files to a folder on your phone. When setting up, make sure to set the save directory to the same folder/location as the sync service.
- Once setup, simply start/stop recording and talk! Once complete, the audio file will be saved to your phone's directory and moved to the cloud using your sync service. Once in the cloud, the sync service on your machine should detect the new file and automatically pull it into the Echo core process.

### Example for for Box/Obsidian users (dev-preferred solution)
My core workflow uses [Obsidian](https://obsidian.md/download), an open source, markdown-based, notetaking app. Notes are stored as markdown (.md) files in a "Vault," which is simply the default app directory. Obsidian has built-in recording options, which allows for an all-in-one Echo flow.
#### Setup Echo with cloud-based Box/Obsidian
- Create a [Box](https://www.box.com/home) account, if one does not already exist.
- Using [Box Sync](https://support.box.com/hc/en-us/articles/360043697194-Installing-Box-Sync), synchronize the cloud to the desktop where Echo is installed.
- Inside of the synchronized directory, create a new folder for the Obsidian Vault. This folder is where Obsidian natively saves new .mp4 files if audio is recorded within the app.

{{< callout type="info" >}}
Optional: Inside the Obsidian Vault, create four new folders for daily, weekly, monthly, and custom summaries. 
{{< /callout >}}
- Anytime a new .mp4 is added to the cloud-based Obsidian Vault, it is automatically detected by Echo, transcribed and summarized. When complete, the summary is pushed back to the Obsidian Vault and into one of the specified folders.

{{< callout type="info" >}}
When transcription is complete, the .mp4 in the cloud can be transferred to a different destination folder. I recommend a backup hard drive to de-clutter the cloud.
{{< /callout >}}

#### Setup Android integration for cloud-based Box/Obsidian
In addition to the above core process, I also setup my phone (Android, S24) to sync with Box/Obsidian so that I can quickly record audio and it automatically gets pulled through the system. I do not subscribe to Obsidian Sync, but I have found a good workaround using 3rd party apps.
- Download [BoxSync Pro](https://play.google.com/store/apps/details?id=com.ttxapps.boxsync&hl=en&pli=1), a 3rd party app, which allows two-way sync between a Box account and phone local storage. The app is free, but the paid version is inexpensive and professional. There are other apps by the same developer to support your preferred cloud client.
- Download the [Obsidian](https://play.google.com/store/apps/details?id=md.obsidian&hl=en) app. During setup, "Open folder as vault" and set the directory to match the BoxSync Pro sync location. If setup correctly, the same Obsidian Vault is always up-to-date on mobile, in the cloud, and on your desktop (with Echo).
- Record audio logs natively in the Obsidian app. In the app, tap "Start/Stop recording" and talk! Once done, the .mp4 is uploaded back to the cloud via BoxSync Pro and is returned to the core Echo process. If Echo is configured to move .mp4 files off the cloud, the local .mp4 copy on your mobile device will automatically get removed/cleaned up when Echo work is complete and the cloud server is updated.

{{< callout type="info" >}}
This setup has also been tested with [Easy Voice Recording](https://play.google.com/store/apps/details?id=com.coffeebeanventures.easyvoicerecorder&hl=en_US), which is a different press-to-record app. The app directory can be set to save the .mp4 files to the BoxSync Pro folder, which again picks it up and returns the file to the core Echo process.
{{< /callout >}}