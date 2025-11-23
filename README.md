# Meditation App

A simple meditation app built with Python and Tkinter that plays meditation audio sessions with optional background sound.

## Features

- Play different meditation audio tracks (`med1.wav` and `med2.wav`)
- Play calming background sound (ocean waves, hum, or custom `.wav` file)
- Start and stop meditation audio and background sounds independently
- Simple and clean GUI with Tkinter

## Requirements

- Python 3.x
- For basic audio playback with winsound (Windows only, no extra installs needed)
- Optional: `numpy`, `sounddevice`, `pygame` for advanced background sound generation and audio playback (if you use enhanced versions)

## Installation

1. Clone or download the repository.
2. Place your meditation audio files (`med1.wav` and `med2.wav`) in the project folder.
3. (Optional) Place your background sound file (`ocean_wave.wav` or any `.wav`) in the project folder.

If you want to generate calm ocean waves sound (optional), run:

```bash
pip install numpy
python make_ocean.py
