---
linkTitle: "LLM Examples"
type: docs
weight: 2
---
## Example output summaries
Echo uses large language models for summarization. During initial install, the default model is [Mistral:7b](https://ollama.com/library/mistral), a lightweight, open source model that was trained largely on web, blog, and conversational text. In the Echo app, custom system prompts are used to create new derivatives of Mistral. These derivatives prioritize summaries that are written in first-person, as if blogged by the author, and follow a more natural, conversational cadence.

Mistral is strongly recommended as the primary summarization model in Echo, but I have also tested a few alternates. Below, you can see summaries that have been prepared by some of the most popular open source models, as well as summaries written by OpenAI (gpt-3.5-turbo-1106). The same system prompt and transcript was used for all models.

### Original transcript
<details>
<summary>Click to view transcript</summary>

**Detected Language:** en (confidence 1.00)

**[00:02 -> 00:43]** I've made good progress the last 24 hours on cleaning up the large language model scribe app. So at this point, it looks good. From a technical perspective, it's got everything I want it to have. I spent a lot of time polishing the output format files. Basically, I wanted the daily to always be in a strict format to have keynotes. And then I realized I wanted the weekly to have the same thing. So the weekly now also looks very similar to the daily. In fact, they share almost the same model file. And they share very similar formatting and structure in the output.

**[00:44 -> 01:52]** The monthly now also correctly summarizes just the simple paragraph text format of the weeklies. So it yields actually a different format than the other two. It gives a two to three sentence sort of high level overview. Of activities over the month. And then it starts breaking down into highlights, kind of key highlights and progress and development, as well as a reflection section that focuses on like answering a couple different questions. What worked well, what didn't work well, what surprised me, et cetera. And then there's a final section on next steps. And again, all of those are bulleted. So it's actually less of a formatted, like freeform writing style as much as it is. Like this is a list of things. That were accomplished that need to be accomplished and that I learned, I think that's good because the next significant development app, I'm going to be like working towards not immediately is a publisher, right? It's a, something that actually takes those monthlies and ingest them in ways that are like, Hey, how do I tell a story?

**[01:53 -> 03:06]** What? Yeah. How, how would I tell a story? And so it's okay if those aren't like totally formalized the exact same way. I also spent a lot of time working on polish, right? When I tag, when I tag stuff, now tags only read the summaries. They don't necessarily read the keynotes. There are too many tags that are being applied. I changed it such that the configuration file now contains basically everything that you'd want in the controller. So not only the file folders for exporting and for watching, but also the different parameters. So all of the different parameters that are being applied to the models, the models themselves have different initial and final prompts based off of like, sorry, not initial finals. It's chunk based prompts versus final prompts for how the models work. They chunk the large texts into the smaller pieces and analyze them and then provide little summaries of the individual texts. And then there's a final summary that looks at all of those little ones and puts it together. So. Those are all now captured. additional quality of life elements that I've worked on. So for instance, one of them is on,

**[03:09 -> 03:33]** it's basically like a prep for readiness check. It checks whether or not the configuration file is set up correctly, and that the user has actually set destination files for watching for audio logs, for output of the, like for archiving logs, for where you want the outputs to go. And what it does is it forces the user during first time startup to run this setup configuration.

**[03:35 -> 03:51]** If you don't run it, all of the different functions that I've built are grayed out. You cannot select them, they do not work. And so you have to set up the configuration file and it has to be valid before any of those activities are functional, which I think is really smart because it's, it proofs it somewhat.

**[03:53 -> 04:27]** I think that's important for like easy deployment and setup. I also have been working on some initial scripting to do first time setups. So out of the box, like which programs do you need to run? They're little bat files that script through command line and basically make sure that the user has an appropriate suite of dependencies. They've got Python, they've got faster whisper, that they've got CUDA enabled, that they're running the right kind of GPU.

**[04:28 -> 04:53]** So you can go through all that and check to make sure that they're installed. And if they're not installed, install them. And then finally, there's going to be just a little run.bat file that is actually gonna launch these virtual environments for the user and then kick off the app. And so if the user does wanna run the app, like on a schedule or in the background, they should just have to click that run.bat and everything is taken care of.

**[04:56 -> 05:03]** Oh, in addition to that, the setup, the setup also includes the preparation of custom LLM models.

**[05:05 -> 05:23]** So I've prepared a couple of different model files and a couple of different custom models that will automatically be created and generated as part of the setup. So again, they're automatically labeled correctly, they're given the right names and that it automatically works with the script in the way that I want it to work. So that all looks good.

**[05:24 -> 05:37]** I'm sure I'm forgetting more little nuances of things and I'm gonna return to that as well. So you can see that it's cleaned up, it's all done and polished. I changed a lot yesterday to make it really clean and polished.

**[05:40 -> 05:52]** I think, what else did I do? I also add the ability to delete entries. So I built in a little toolkit. It's mostly for development, but it's also, it's a nice utility.

**[05:53 -> 07:17]** So the tools are like delete all summaries, delete all transcripts, delete both. start the app. If the configuration file changes while the app is running, if you click the little option that says setup configuration, that prompts you graphically to set the right folder files via GUI. And then after you finish setting it, it says, okay, great, set correctly, the app is now restarting. And it restarts the app, which refreshes the configuration file and make sure that the new values took. And so that's, yeah, those are all little quality of life changes that I made, which I think are worthwhile. Next up is, I don't know if QA is the right description, but basically assuring that it starts up well on a fresh machine. And so I'm in the process of downloading VirtualBox or Windows Sandbox and basically building new environments on new virtual machines to make sure that it sets up correctly the first time. And it's going to be a little painful, I think, and tedious to get this bug free and working. But it is one of the important steps. It'll basically, the user will go through a README file and then basically double click setup and then double click run. And that should be as a goal, like, as difficult as it gets.

**[07:20 -> 07:46]** As also part of the next steps, I will have to document the setup procedures. So I talked about doing written documentation to describe not only how the app functions, like a flow chart, but also a setup how-to guide, like a very, very simple go to this link, down to this link, go to this link, down to this thing, run the setup, run the bat, go. And that should be it, but I'm sure there's always something that I'm surprised by.

**[07:54 -> 08:31]** Yeah, I think all those setups are going to be important for getting right. Oh, yeah, in addition to paperwork, I also want a video of this. I personally think it's very helpful and nice polish when the developer offers a video instruction of how to install and make sure it works, common troubleshooting problems, etc. So I'll probably record a video for getting this up and running once I work out all the kinks, again, from a virtual machine, like brand new, what do you do, how do you set it up? That'll be nice, I think. It may also be worthwhile, producing a small video on how it works. Again, like a, not quite a vlog. But

**[08:33 -> 09:23]** in a similar format, right, this is functionally how it was designed, this is how it generally works, etc. It's a bit more self promotiony, but it's not a bad thing. I'm debating on spending a little bit of time today refactoring the actual technical side of it. So cleaning up the code base, a lot of it is reused code. and doesn't necessarily need to be duplicated in multiple places, it doesn't really matter because frankly nobody's going to be digging through the code anyway. They're going to be simple non-power users and this is more for like if somebody goes into the code and looks it looks a little dumb. For instance, I have like two different ways of chunking text and that's unnecessary or I'm inconsistent with formatting on naming or commenting and just I can clean those up but that's all final polish. What else?

**[09:28 -> 10:00]** Oh yeah, I wanted to go through and prepare as part of that how to not the how to guide but like how it works guide some technical values basically like this is these are a number of files total audio length takes what time to transcribe with faster whisper large model three large model two large model one and give representative examples of what it produces.

**[10:02 -> 10:33]** In general, I think it does make sense I have a little folder as part of this downloadable zip of test files. So test audio logs and this is what the output should be generally to make sure that things are working correctly. I think that's that's nice as well. They don't have to necessarily record their own they can see what it looks like. I'm also debating on adding it's not required but from a technical tool set like a tool that's dedicated to data. So it's like it tells you

**[10:36 -> 10:42]** how many hours of the program was initiated, how many hours of audio has been analyzed,

**[10:44 -> 10:47]** how many words of text have been written, how many different dev logs have been written,

**[10:49 -> 10:54]** estimated time saved. That's a little trickier because every read to different speed.

**[10:56 -> 11:05]** Just like statistics. I think that would be kind of nice. I personally like those like total word count is x total time saved. Given a given like given a particular word count is y.

**[11:06 -> 11:39]** That's always just fun. I can probably think of a million things of doing that. How many different tags have been applied? Yeah, etc. How many months does this cover? How many times has the program been run just like counters, but it's not critical. Okay, I think that's everything. It's a lot on the to do list. Today, I think my goal is to just get through qa testing. If I can get farther, great. But that's the that's the priority.

</details>

### Mistral:7b
<details>
<summary>Click to view Mistral summary</summary>

#### Summary
Over the past day or so, I've been fine-tuning my language model scribe app. From a technical standpoint, it now includes all the features I desired. The last few days were spent polishing output format files, standardizing daily and weekly summaries to share similar structures, while monthly summaries offer a high-level overview of activities over the month.

I made improvements to the app's appearance, too, by having tags now only read the summaries instead of keynotes due to excessive tagging earlier on. I adjusted the configuration file to include everything you'd want in the controller, such as folders for exporting and watching, different parameters for models, and initial/final prompts based on the model type.

Other quality-of-life improvements include a readiness check for the configuration file, scripts to install dependencies like Python, Faster Whisper, CUDA, virtual environment setup, and a toolkit to delete entries during development.

Next up is testing the app on a fresh machine, creating written documentation and a video instruction for easy installation and troubleshooting. Although it'll be tedious, I believe it's an essential step toward ensuring a smooth user experience. I'm also planning to create a short video showcasing the app's functionality.

I spent today working on polishing and documentation tasks for my transcription tool. I addressed some inconsistencies in the code that needed fixing - duplicate chunking methods, inconsistent formatting, you name it. I compiled a 'how it works' guide for the tool, including technical values like total audio length, transcription times with different models, examples of output to ensure everything functions correctly.

I also thought about adding analytical metrics to the tool, such as hours initiated, analyzed audio, written text, different devlogs, estimated time saved, word count. However, calculating time saved is tricky since everyone reads at a different speed. I'm still deciding whether to include these additional metrics, but they'd provide valuable information for users.

#### Key notes
##### Decisions & Observations
- Decided to structure the app's output formats for daily, weekly, and monthly summaries with a focus on ease of reading and understanding.
- Implemented a prep for readiness check to ensure the configuration file is set up correctly before any functions become operational.
- Developed initial scripting for first-time setups, ensuring users have necessary dependencies and virtual environments.
- Prepared custom LLM models as part of the setup process.
- Decided to clean up inconsistencies in code formatting and naming
- Added tools for deleting entries in the app, primarily for development purposes but also as a utility.
- Priority for today is QA testing, with the goal of getting through it; further progress will depend on available time.
##### Issues & Next Steps
- Planning to document the setup procedures with both written and video instructions.
- Considering refactoring the technical side of the codebase to improve efficiency and organization.
- Will create a technical guide for the project, including details about file count, audio length, transcribe time with different models, and representative examples of output
- Considering adding additional features to the tool set, such as tracking hours of program initiated, analyzed audio, written text, and estimated time saved, but acknowledges these might be tricky due to variable read speeds
- Ensuring the app starts up correctly on a fresh machine by testing it in new virtual environments.
- Thinking about including counters for words count, different tags applied, months covered, and number of times the program has been run, although these are not critical
</details>

### OpenAI (gpt-3.5-turbo-1106)
<details>
<summary>Click to view OpenAI summary</summary>

#### Summary
Over the past day, I've been deep in refining the output format for the large language model scribe app. The technical aspects are shaping up well, and I've dedicated significant time to ensuring that the daily, weekly, and monthly summaries all follow a consistent format with keynotes. The monthly summary now provides a high-level overview of activities, followed by key highlights, progress, and a reflection section. I've also been streamlining the user experience by refining the tagging system and configuration file, and I've added a readiness check during the first-time setup to ensure the configuration file is valid before the app's functions become accessible.

In addition, I've scripted the first-time setups to ensure users have all the necessary dependencies installed, including programs like Python, FastAPI, and CUDA. I've also prepared custom LLM models as part of the setup process. To enhance usability, I've incorporated the ability to delete entries and restart the app if the configuration file changes while the app is running, aiming to make the user experience smoother.

Looking ahead, my focus will shift to quality assurance, ensuring the app starts up smoothly on a fresh machine. This will involve thorough testing on new virtual machines to guarantee a seamless setup process. I also plan to document the setup procedures and consider creating instructional videos to guide users through installation and troubleshooting. Additionally, I'm contemplating refactoring the technical side of the app to clean up the code base, although this may not be a top priority as most users won't be digging through the code.

During today's review of the code, I noticed a few areas that need cleaning up, such as inconsistent formatting on naming and unnecessary duplication in text chunking. It's all part of the final polish, but definitely worth addressing. I also worked on preparing a guide to explain how the system works, including technical values and representative examples of output. I'm considering including a folder of test files in the downloadable zip, so users can see what the output should look like and ensure everything is working correctly. Additionally, I'm thinking about adding a dedicated data tool to track stats like the number of files analyzed, hours of audio processed, and words written. Estimating time saved due to different reading speeds is a bit tricky, but I believe it could be a valuable addition. My main goal for today is to focus on QA testing, and if I can make further progress, that's a bonus.

#### Key notes
##### Decisions & Observations
- Decided to create a strict format for daily and weekly outputs, with the weekly output now resembling the daily format.
- Decided to clean up code by removing unnecessary duplicate text chunking methods and ensuring consistent formatting and commenting for final polish.
- Priority is to focus on QA testing today, with the goal of making progress beyond that if possible.
##### Issues & Next Steps
- Needs to resolve the issue of tags only reading the summaries and not the keynotes.
- Will explore setting up a readiness check to ensure the configuration file is correctly set up before any app functions can be used.
- Plans to conduct initial scripting for first-time setups to ensure all necessary dependencies are installed.
- Next steps include testing the app on a fresh machine and documenting the setup procedures, including written documentation and a video tutorial for installation and troubleshooting.
- Needs to prepare a guide on how the program works, including technical values such as total audio length, transcription times with different models, and representative output examples.
- Will explore the addition of a dedicated tool for tracking data analysis metrics, such as files analyzed, audio hours transcribed, word count, and time saved, to enhance technical insights and statistics.
</details>

### Llama2:7b
<details>
<summary>Click to view Llama2:7b summary</summary>

#### Summary
Hey there! So, yesterday was a productive day. I spent most of my time cleaning up the large language model scribe app, and it's looking good now. Technically, everything is in order, and the output format files are polished. I updated the monthly summaries to provide a more streamlined overview of activities throughout the month, highlighting what worked well, what didn't, and what I learned.

I also spent time refining the auto-pathing system in Blender. I added variation logic to make it more organic, especially near slopes. However, there are still some edge cases where the system breaks down. I plan to test it further with a bigger environment next. Additionally, I scripted initial virtual environment setup through command line using bat files to ensure the user has the appropriate dependencies installed, such as Python and CUDA. The run.bat file will launch these virtual environments and kick off the app if needed.

To improve the setup process further, I want to create custom LLM models and include them in the setup. These models will be automatically labeled and given the right names to work seamlessly with the script. I also considered refactoring the technical side of the project, cleaning up the code base, and consolidating redundant code.

Today, my goal is to get through QA testing and see if I can make further progress. I'm thinking about documenting the setup procedures to ensure a smooth first-time setup experience for users. Oh, and I also wanted to prepare a "how it works" guide for users, including technical values and representative examples of what the output looks like.

Overall, things are looking good, but there's still work to be done.

#### Key notes
##### Decisions & Observations
- Decided to polish the output format files for daily, weekly, and monthly summaries to have a consistent structure and formatting.
- Plans to document the setup procedures in written form, including a flowchart and a how-to guide, to make it easy for users to follow.
- Wants to record a video tutorial for installing and troubleshooting the app, to provide nice polish and helpful instructions for users.
- Decided to refactor the technical side of the project (codebase cleanup, inconsistent formatting, etc.)
- Debating on spending time today to do this
- It doesn't matter if nobody digs through the code, it's more for internal use and polish
- Wanted to prepare a how-it-works guide for users
- May include examples of output for testing purposes
- Debating on adding a dedicated data tool for tracking progress (e.g., word count, audio analyzed, etc.)
- Would be useful but not critical
- Priority today is to finish QA testing and see if further progress can be made
##### Issues & Next Steps
- Needs to resolve the issue of too many tags being applied to the models and create a configuration file that contains everything needed for the controller.
- Will explore the option of using a virtual machine or Windows Sandbox to download and build new environments for testing the app's startup on a fresh machine.
- Will include technical values such as file size, transcription time, etc.
</details>

### Llama2:13b
<details>
<summary>Click to view Llama2:13b summary</summary>

#### Summary
Hey there! Today was focused on tidying up the large language model scribe app and polishing the output format files. From a technical perspective, everything looks good, and I spent time refining the output format files to ensure they're in a strict format for daily, weekly, and monthly summaries. The monthly summary will give a high-level overview of activities over the month, followed by key highlights, progress, development, and reflection questions. Users can also tag specific sections for easy access.

Besides these changes, I worked on some quality-of-life elements like a prep readiness check to ensure the configuration file is set up correctly, and a script that checks if all necessary dependencies are installed before launching virtual environments. These changes will make it easier for users to deploy and set up the app. I also added the ability to delete entries and restart the app if necessary.

I'm sure there are other small details I forgot to mention, but these changes should improve the user experience. Next, I want to focus on ensuring that it starts up well on a fresh machine by downloading VirtualBox or Windows Sandbox and building new environments on new virtual machines. Documenting the setup procedures is also important, so I'll create written documentation to describe how the app functions and how to set it up. A video instruction of how to install and troubleshoot problems may also be helpful.

Today, I worked on preparing a how-to guide for using the program. I cleaned up any unnecessary code and formatting inconsistencies, and added some technical values to the guide, such as total audio length, number of files analyzed, and estimated time saved. I also debated adding a tool that would give users a breakdown of their progress since initiating the program, including word count, hours saved, and number of dev logs written. While these aren't critical features, they could be fun and interesting to include. My goal for today is to finish QA testing, but we'll see how far I can get.

#### Key notes
##### Decisions & Observations
- Decided to polish the output format files for the daily, weekly, and monthly summaries.
- Shared similar formatting and structure across all three.
- Used a strict format to ensure consistency.
- Spent time working on quality of life elements, such as:
- Prepared custom LLM models for automatic generation during setup.
- Added the ability to delete entries, restart the app, and automatically refresh configuration files.
- Assuring that it starts up well on a fresh machine through virtual environments or sandboxes.
- Documenting the setup procedures with written documentation and video tutorials.
- Refactoring the technical side of the project to clean up the code base and reduce duplication.
- Decided to simplify and clean up the code for non-power users, focusing on minor polishing issues rather than extensive changes (09:23 - 09:42)
- Consistency in formatting and naming
- Removing unnecessary chunking methods
- Cleaning up inconsistent formatting
- Wanted to create a how-it-works guide, not just a how-to guide (09:44 - 10:00)
- Explaining the technical values behind the program
- Providing representative examples of output
- Debating on adding a dedicated data tool for tracking progress (10:15 - 10:49)
- Estimated time saved
- Total audio length transcribed with Faster Whisper
- Number of files analyzed since program initiation
- Personal preferences for fun stats to include (11:16 - 11:26)
- Total word count
- Total time saved
- Number of months covered
- Number of times the program has been run
- Today's goal is to focus on QA testing, with the intention of getting as far as possible (11:32 - 11:35)
##### Issues & Next Steps
- Next steps include:
</details>

