import tkinter as tk
import threading
import winsound

bg_running = False

# Background hum made with Windows beep (not real music, but relaxing enough)
def play_background_hum():
    global bg_running
    if bg_running:
        return
    bg_running = True

    def hum_loop():
        while bg_running:
            # frequency (Hz), duration (ms)
            winsound.Beep(200, 300)   # low tone
            winsound.Beep(180, 300)   # lower tone
            winsound.Beep(220, 300)   # smooth blend
    threading.Thread(target=hum_loop, daemon=True).start()

def stop_background_hum():
    global bg_running
    bg_running = False

# Meditation audio
def play_audio(file):
    threading.Thread(target=lambda: winsound.PlaySound(file, winsound.SND_FILENAME)).start()

def stop_audio():
    winsound.PlaySound(None, winsound.SND_PURGE)

# UI
root = tk.Tk()
root.title("Meditation App")
root.geometry("350x400")
root.configure(bg="#1a1a1a")

title = tk.Label(root, text="Meditation Sessions",
                 font=("Arial", 18, "bold"), fg="white", bg="#1a1a1a")
title.pack(pady=20)

btn1 = tk.Button(root, text="Breathing Meditation",
                 width=25, height=2, command=lambda: play_audio("med1.wav"))
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Calming Meditation",
                 width=25, height=2, command=lambda: play_audio("med2.wav"))
btn2.pack(pady=10)

btn_bg = tk.Button(root, text="Start Background Hum",
                   width=25, height=2, command=play_background_hum)
btn_bg.pack(pady=10)

btn_bg_stop = tk.Button(root, text="Stop Background Hum",
                        width=25, height=2, command=stop_background_hum)
btn_bg_stop.pack(pady=10)

btn_stop = tk.Button(root, text="Stop All Audio",
                     width=25, height=2, fg="white", bg="red",
                     command=lambda: [stop_audio(), stop_background_hum()])
btn_stop.pack(pady=30)

root.mainloop()
