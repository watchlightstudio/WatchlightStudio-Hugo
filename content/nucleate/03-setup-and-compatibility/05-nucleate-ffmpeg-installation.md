---
linkTitle: "FFmpeg/FFprobe"
type: docs
weight: 5
slug: "ffmpeg-ffprobe"
url: "/nucleate/setup-and-compatibility/ffmpeg-ffprobe"
---
## Installing FFmpeg for Nucleate

### Prerequisites
- **Operating System:** Windows or macOS 
- **Administrator privileges** to install binaries and update your PATH  
- Optional but recommended: verify that your machine meets the [hardware requirements](/nucleate/setup-and-compatibility/hardware) for local transcription & summarization.

### Auto installation
On both Windows and macOS, Nucleate will attempt to automatically install Ollama and FFmpeg during first time startup. The installation process is pretty quiet on Windows, but macOS has a few special notes.  Do not be afraid!

{{< callout type="info" >}}
macOS requires an admin account to install FFmpeg. The recommended approach is to install via Nucleate startup sequence. During startup, Nucleate will launch a terminal window with "sudo" request to install [Homebrew](https://brew.sh/). Homebrew is a package manager for macOS, like "pip" for Python. Once installed, Nucleate will automatically grab Ollama (if not already installed) and FFmpeg.
{{< /callout >}}

### Manual installation Instructions
#### Windows
1. Download the latest FFmpeg static build for Windows from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).  
2. Extract the ZIP to a folder of your choice (e.g., `C:\ffmpeg`).  
3. Add the `bin` folder to your system `PATH`:
   4. Open **Start → Search “Environment Variables” → Edit the system environment variables**.  
   5. Click **Environment Variables…**  
   6. Under **System variables**, select **Path → Edit → New**  
   7. Add the full path to the `bin` folder (e.g., `C:\ffmpeg\bin`)  
   8. Click OK to save changes.  
9. Open a new Command Prompt and run:
```bash
ffmpeg -version
ffprobe -version
```

#### macOS (recommended)
1. Open Terminal
2. Install via Homebrew (recommended):
```
# Install Homebrew if not already installed (skip if you have it)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installing Homebrew may require sudo and your password. Follow the terminal prompts.

# Install FFmpeg
brew install ffmpeg

# Verify installation
ffmpeg -version
ffprobe -version

# Optional: confirm PATH detection
which ffmpeg
which ffprobe
```

#### macOS (manual installation)
1. If you prefer not to use Homebrew, download a static build of FFmpeg for your CPU architecture:
2. **Apple Silicon (arm64 / M1/M2):** https://www.osxexperts.net/
3. **Intel macOS (x86_64):** https://evermeet.cx/ffmpeg/ (legacy, not supported)
4. Download the ZIPs for both ffmpeg and ffprobe and extract them.
5. Move the ffmpeg and ffprobe binaries to a folder on your PATH (.e.g., /usr/local/bin). You may need sudo:
```
sudo mv ffmpeg ffprobe /usr/local/bin/
sudo chmod +x /usr/local/bin/ffmpeg /usr/local/bin/ffprobe
```
6. Open a new Terminal and verify:
```
ffmpeg -version
ffprobe -version
```

{{< callout type="info" >}}
If FFmpeg is installed correctly, Nucleate will detect it automatically — no app restart or configuration required.
{{< /callout >}}