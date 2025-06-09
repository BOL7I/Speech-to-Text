import tkinter as tk
from tkinter import filedialog, messagebox
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment
import threading

def convert_and_transcribe(mp4_path):
    if not mp4_path.lower().endswith(".mp4"):
        messagebox.showerror("Invalid File", "Please select a valid MP4 file.")
        return

    wav_path = os.path.splitext(mp4_path)[0] + "_converted.wav"
    transcript_path = os.path.splitext(mp4_path)[0] + "_transcript.txt"

    try:
        log_text.set("Converting video to audio...")
        root.update()
        clip = VideoFileClip(mp4_path)
        clip.audio.write_audiofile(wav_path)

        audio = AudioSegment.from_file(wav_path)
        audio = audio.set_frame_rate(16000).set_channels(1)
        audio.export(wav_path, format="wav")
        log_text.set("Audio converted. Starting transcription...")
        root.update()

        recognizer = sr.Recognizer()
        full_text = ""
        with sr.AudioFile(wav_path) as source:
            duration = source.DURATION
            if duration > 60:
                chunk_size = 30
                audio_seg = AudioSegment.from_wav(wav_path)
                for i in range(0, int(duration), chunk_size):
                    chunk = audio_seg[i * 1000: (i + chunk_size) * 1000]
                    chunk_file = f"chunk_{i}.wav"
                    chunk.export(chunk_file, format="wav")
                    with sr.AudioFile(chunk_file) as chunk_source:
                        audio_chunk = recognizer.record(chunk_source)
                        try:
                            text = recognizer.recognize_google(audio_chunk)
                            full_text += text + " "
                        except:
                            pass
                    os.remove(chunk_file)
            else:
                audio_data = recognizer.record(source)
                full_text = recognizer.recognize_google(audio_data)

        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(full_text)
        log_text.set("Transcription complete! Transcript saved.")
        messagebox.showinfo("Success", f"Transcript saved to:\n{transcript_path}")

    except Exception as e:
        log_text.set("Error occurred.")
        messagebox.showerror("Error", str(e))

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        threading.Thread(target=convert_and_transcribe, args=(file_path,)).start()

# GUI setup
root = tk.Tk()
root.title("MP4 to Transcript Converter")
root.geometry("400x200")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Select an MP4 file to convert and transcribe:")
label.pack(pady=10)

select_button = tk.Button(frame, text="Browse MP4", command=browse_file)
select_button.pack()

log_text = tk.StringVar()
log_label = tk.Label(root, textvariable=log_text, wraplength=380, justify="center", fg="blue")
log_label.pack(pady=10)

root.mainloop()
