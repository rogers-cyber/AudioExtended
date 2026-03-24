import sys
from pathlib import Path
import os

# ================= FFMPEG FIX =================
FFMPEG_DIR = r"C:\ffmpeg\bin"  # Update your path
os.environ["PATH"] = FFMPEG_DIR + os.pathsep + os.environ.get("PATH", "")

from pydub import AudioSegment

import subprocess  # ADD THIS

# 🔥 ADD THIS BLOCK
_original_popen = subprocess.Popen
def silent_popen(*args, **kwargs):
    kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
    return _original_popen(*args, **kwargs)
subprocess.Popen = silent_popen

AudioSegment.converter = os.path.join(FFMPEG_DIR, "ffmpeg.exe")
AudioSegment.ffprobe = os.path.join(FFMPEG_DIR, "ffprobe.exe")

# ================= IMPORTS =================
import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as tb
from ttkbootstrap.widgets.scrolled import ScrolledText
import threading
import math

import datetime

# ================= APP INFO =================
APP_NAME = "Audio Extended"
APP_VERSION = "1.1.0"
APP_AUTHOR = "MateTools"

# ================= APP =================
app = tk.Tk()
style = tb.Style(theme="superhero")

app.title(f"{APP_NAME} {APP_VERSION}")
app.geometry("950x600")

stop_event = threading.Event()

# ================= HELPERS =================
def ui(func, *args, **kwargs):
    app.after(0, lambda: func(*args, **kwargs))

def log_line(text):
    def _log():
        log.text.config(state="normal")
        log.text.insert("end", text + "\n")
        log.text.see("end")
        log.text.config(state="disabled")
    ui(_log)

def resource_path(file_name):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, file_name)

# ================= MENU =================
def show_about():
    messagebox.showinfo(
        f"About {APP_NAME}",
        f"""
📌 {APP_NAME} v{APP_VERSION}

🔊 Professional Audio Extension Tool
   - Extend audio to long durations (10 min → 12 hours)
   - Smart looping system for seamless playback
   - Supports MP3, WAV, FLAC, OGG formats

⚡ High Performance
   - Efficient looping engine
   - Handles very long audio generation
   - Smooth real-time progress updates

🎛 Flexible Output Options
   - Choose target duration easily
   - Select output format (MP3, WAV, FLAC, OGG)
   - Auto filename with date & time

🎚 Seamless Looping
   - Optional fade-in/out at loop points
   - Reduces harsh audio cuts
   - Ideal for ambient, music, podcasts

⏹ Stop Anytime
   - Safely cancel processing
   - No crashes or corruption

📊 Live Preview
   - Shows original audio length
   - Displays selected target duration

👨‍💻 Built by MateTools
   - Focused on performance and usability
   - Lightweight and fully offline

🌐 Website / Support
   - https://matetools.gumroad.com
"""
    )


def show_help():
    messagebox.showinfo(
        f"{APP_NAME} - User Guide",
        f"""
📘 {APP_NAME} - User Guide

1️⃣ Select Audio File
   - Click "Browse" to choose your file
   - Supports MP3, WAV, FLAC, OGG

2️⃣ Choose Output Folder
   - Select where extended audio will be saved

3️⃣ Configure Settings
   - Select target duration (10 min → 12 hours)
   - Set fade duration (optional, for smooth looping)
   - Choose output format
   - Set filename prefix

4️⃣ Start Processing
   - Click "Start"
   - Progress bar shows real-time status
   - Logs display progress

5️⃣ Stop Anytime
   - Click "Stop" to safely cancel

💡 Tips
   - Use fade (2–5 seconds) for smooth looping
   - Great for ambient, sleep, music loops
   - Longer targets may take more time

⚠ Notes
   - Requires FFmpeg installed
   - Do not move/delete file during processing
"""
    )


menubar = tb.Menu(app)

file_menu = tb.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=app.quit)

help_menu = tb.Menu(menubar, tearoff=0)
help_menu.add_command(label="User Guide", command=show_help)
help_menu.add_command(label="About", command=show_about)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Help", menu=help_menu)

app.config(menu=menubar)

try:
    app.iconbitmap(resource_path("logo.ico"))
except:
    pass

# ================= GUI =================
tb.Label(app, text=APP_NAME, font=("Segoe UI", 22, "bold")).pack(pady=(10, 2))
tb.Label(app, text="Extend/Loop Audio to Long Duration", font=("Segoe UI", 10, "italic"), foreground="#9ca3af").pack(pady=(0,10))

# Input
input_card = tb.Labelframe(app, text="Audio Input", padding=15)
input_card.pack(fill="x", padx=10, pady=10)
audio_path = tk.StringVar()
tb.Entry(input_card, textvariable=audio_path).pack(side="left", fill="x", expand=True, padx=5)
tb.Button(input_card, text="Browse", bootstyle="info", command=lambda: audio_path.set(filedialog.askopenfilename(filetypes=[("Audio","*.mp3 *.wav *.flac *.ogg")]))).pack(side="left", padx=5)

# Output
output_card = tb.Labelframe(app, text="Output Settings", padding=15)
output_card.pack(fill="x", padx=10, pady=10)
output_dir = tk.StringVar()
tb.Entry(output_card, textvariable=output_dir).pack(side="left", fill="x", expand=True, padx=5)
tb.Button(output_card, text="Browse", bootstyle="info", command=lambda: output_dir.set(filedialog.askdirectory())).pack(side="left", padx=5)

file_prefix = tk.StringVar(value="extended")
tb.Label(output_card, text="Prefix:").pack(side="left", padx=5)
tb.Entry(output_card, textvariable=file_prefix, width=15).pack(side="left")

# ================= Duration Presets =================
dur_presets = {
    "Select Duration": None,
    "10 minutes": 10*60,
    "30 minutes": 30*60,
    "1 hour": 60*60,
    "2 hours": 2*60*60,
    "3 hours": 3*60*60,
    "4 hours": 4*60*60,
    "5 hours": 5*60*60,
    "6 hours": 6*60*60,
    "7 hours": 7*60*60,
    "8 hours": 8*60*60,
    "9 hours": 9*60*60,
    "10 hours": 10*60*60,
    "11 hours": 11*60*60,
    "12 hours": 12*60*60
}

target_option = tk.StringVar(value="Select Duration")
target_duration = tk.IntVar(value=0)

def on_duration_change(choice):
    value = dur_presets.get(choice)

    if value is None:
        # Don't overwrite with invalid value
        target_duration.set(0)
        preview_label.config(text="Audio Duration: -- | Target: --")
    else:
        target_duration.set(value)
        update_preview()

tb.Label(output_card, text="Target Duration:").pack(side="left", padx=5)

tb.OptionMenu(
    output_card,
    target_option,
    *dur_presets.keys(),
    command=on_duration_change
).pack(side="left")

# Fade Option
fade_var = tk.IntVar(value=3)  # default 3 seconds fade
tb.Label(output_card, text="Fade at Loop (seconds):").pack(side="left", padx=5)
tb.Entry(output_card, textvariable=fade_var, width=5).pack(side="left")

# Log
log_card = tb.Labelframe(app, text="Live Output", padding=15)
log_card.pack(fill="both", expand=True, padx=10, pady=10)
log = ScrolledText(log_card, height=10)
log.pack(fill="both", expand=True)
log.text.config(state="disabled")

# Progress
progress = tb.Progressbar(app, maximum=100)
progress.pack(fill="x", padx=10, pady=5)

# ================= PREVIEW =================
def format_time(seconds):
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h}h {m}m {s}s" if h else f"{m}m {s}s"

preview_label = tb.Label(output_card, text="Audio Duration: -- | Target: --")
preview_label.pack(side="left", padx=10)

def update_preview(*args):
    try:
        audio = AudioSegment.from_file(audio_path.get())
        duration = len(audio)/1000
        preview_label.config(text=f"Audio: {format_time(duration)} | Target: {format_time(target_duration.get())}")
    except:
        preview_label.config(text="Audio Duration: -- | Target: --")

audio_path.trace_add("write", lambda *args: update_preview())
target_duration.trace_add("write", lambda *args: update_preview())

# ================= EXTEND AUDIO WITH FADE =================
def extend_audio():
    if not audio_path.get() or not output_dir.get():
        messagebox.showerror("Error", "Select input and output")
        return

    if target_duration.get() == 0:
        messagebox.showerror("Error", "Please select a valid duration")
        return

    stop_event.clear()
    ui(progress.configure, value=0)

    audio = AudioSegment.from_file(audio_path.get())
    target_ms = target_duration.get() * 1000
    fade_ms = int(fade_var.get() * 1000)
    orig_len = len(audio)

    # Apply fade-in/out to the original audio for smooth looping
    if fade_ms > 0 and fade_ms * 2 < orig_len:
        audio = audio.fade_in(fade_ms).fade_out(fade_ms)

    loops_needed = math.ceil(target_ms / orig_len)
    extended_audio = AudioSegment.empty()

    # Use small increments (e.g., 1 second chunks) to update progress smoothly
    chunk_ms = 1000  # 1 second increments
    total_chunks = math.ceil(target_ms / chunk_ms)
    current_ms = 0

    while current_ms < target_ms:
        if stop_event.is_set():
            log_line("⏹ Stopped by user")
            break

        # Determine which slice of original audio to append
        start = current_ms % orig_len
        end = min(start + chunk_ms, orig_len)
        extended_audio += audio[start:end]
        current_ms += (end - start)

        # Update progress
        progress_value = min(current_ms / target_ms * 100, 100)
        ui(progress.configure, value=progress_value)

    # Trim to exact target length
    extended_audio = extended_audio[:target_ms]

    # Save with date-time in filename
    import datetime
    out_format = "mp3"  # can later connect to dropdown
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = os.path.join(output_dir.get(), f"{file_prefix.get()}_{timestamp}.{out_format}")

    extended_audio.export(out_file, format=out_format)
    ui(progress.configure, value=100)
    log_line(f"Saved extended audio: {out_file}")
    messagebox.showinfo("Done", f"Audio extended to {format_time(target_duration.get())}")

# ================= BUTTONS =================
bar = tb.Frame(app)
bar.pack(fill="x", padx=10, pady=5)
tb.Button(bar, text="Start", bootstyle="success", command=lambda: threading.Thread(target=extend_audio, daemon=True).start()).pack(side="left", padx=5)
tb.Button(bar, text="Stop", bootstyle="danger", command=lambda: stop_event.set()).pack(side="left", padx=5)

# ================= START =================
app.mainloop()