# Audio Extended – Professional Audio Extension & Looping Tool v1.1.0

Audio Extended v1.1.0 is a professional desktop application designed to extend audio files seamlessly to long durations, ranging from 10 minutes up to 12 hours. Ideal for ambient tracks, podcasts, or music loops, it provides smooth looping with optional fade-in/out and real-time progress feedback.

Built for musicians, content creators, audio engineers, and hobbyists, Audio Extended emphasizes high performance, ease of use, and stability for generating long audio files from short clips.

------------------------------------------------------------
WINDOWS DOWNLOAD (EXE)
------------------------------------------------------------

Download the latest Windows executable from GitHub Releases:

https://github.com/matetools/AudioExtended/releases

- No Python installation required
- Standalone executable for Windows
- Ready-to-run out of the box
- Optimized for long audio processing

------------------------------------------------------------
DISTRIBUTION
------------------------------------------------------------

Audio Extended is a paid/commercial desktop utility.

This repository/documentation may include:

- Production-ready Python source code
- Compiled desktop executables (Windows)
- Commercial licensing terms (see LICENSE / sales page)

Python is only required for running the source code version.

------------------------------------------------------------
FEATURES
------------------------------------------------------------

CORE CAPABILITIES

- 🔊 Extend audio files to long durations (10 min → 12 hours)
- 🎛 Supports MP3, WAV, FLAC, OGG formats
- ⏹ Stop processing anytime safely
- ⚡ High-performance looping engine
- 🧠 Optional fade-in/out for smooth seamless loops
- 📊 Real-time progress updates and logs
- 🗂 Auto filename with timestamp for organization

DURATION PRESETS

Audio Extended provides quick presets:

- 10 min → 12 hours selectable
- Custom duration support

EXTENDED AUDIO SYSTEM

- Efficient looping of short audio to target length
- Smooth fade-in/out prevents harsh audio cuts
- Handles very long audio efficiently
- Supports incremental progress updates for smooth UI

USER INTERFACE

- Modern UI with ttkbootstrap
- Input/output selection panels
- Fade duration and target duration options
- Live preview of audio and target duration
- Scrollable logs and progress bar
- Start/Stop control buttons

------------------------------------------------------------
INSTALLATION (SOURCE CODE)
------------------------------------------------------------

1. Clone the repository:

git clone https://github.com/matetools/AudioExtended.git
cd AudioExtended

2. Install required dependencies:

pip install pydub ttkbootstrap

Ensure FFmpeg is installed and `ffmpeg.exe` / `ffprobe.exe` paths are correctly set in the script.

3. Run the application:

python AudioExtended.py

------------------------------------------------------------
BUILD WINDOWS EXECUTABLE
------------------------------------------------------------

You can create a standalone Windows executable using PyInstaller.

1. Install PyInstaller:

pip install pyinstaller

2. Build the application:

pyinstaller --onefile --windowed --name "AudioExtended" --icon=logo.ico AudioExtended.py

The compiled executable will appear in:

dist/AudioExtended.exe

------------------------------------------------------------
USAGE GUIDE
------------------------------------------------------------

1. Select Audio File  
Click "Browse" → choose your audio file (`.mp3`, `.wav`, `.flac`, `.ogg`).

2. Choose Output Folder  
Click "Browse" → select where the extended audio will be saved.

3. Configure Settings  
- Choose target duration from presets  
- Set fade at loop duration (optional)  
- Select filename prefix  

4. Start Processing  
Click "Start" → monitor progress via progress bar and logs.

5. Stop Anytime  
Click "Stop" → safely cancels processing.

6. Preview  
Audio duration and target duration are displayed live.

------------------------------------------------------------
LOGGING & ERROR HANDLING
------------------------------------------------------------

Audio Extended maintains real-time logs:  

- Displays progress, audio slices appended  
- Handles exceptions safely  
- Stops gracefully on user cancellation  
- Ensures no corrupted audio output  

------------------------------------------------------------
REPOSITORY STRUCTURE
------------------------------------------------------------

AudioExtended/

├── AudioExtended.py  
├── logo.ico  
├── README.md  
├── LICENSE  

Generated at runtime:

├── Extended audio files (output folder)  

------------------------------------------------------------
DEPENDENCIES
------------------------------------------------------------

Python 3.10+

Libraries used:

- pydub  
- ttkbootstrap  
- tkinter  
- threading  
- math  
- datetime  
- os  
- sys  
- subprocess  

Ensure FFmpeg (`ffmpeg.exe` and `ffprobe.exe`) is installed for audio conversion.

------------------------------------------------------------
INTENDED USE
------------------------------------------------------------

Audio Extended is ideal for:

- Extending short audio loops to long durations  
- Creating seamless ambient tracks  
- Generating background music for podcasts or events  
- Audio experimentation and creative workflows  

Optimized for stability, smooth performance, and offline usage.

------------------------------------------------------------
ABOUT
------------------------------------------------------------

Audio Extended is developed by MateTools, focused on building professional offline productivity and creative tools for Windows users.

Website:

https://matetools.gumroad.com

© 2026 MateTools  
All rights reserved.

------------------------------------------------------------
LICENSE
------------------------------------------------------------

Audio Extended is commercial software.

License terms:

- Distributed as commercial source code  
- Personal and commercial use allowed  
- Redistribution or resale as a competing product is prohibited  
- Rebranding or repackaging for resale is prohibited  
- Compiled executable usage allowed under commercial license  
- Modification for private internal use permitted  

For commercial licensing or enterprise deployment, contact the developer.