<div align="center">
<img width="893" height="431" alt="image" src="https://github.com/user-attachments/assets/6ae80b50-cdd3-44c0-a6de-35c35e0aaddc" />

<div align="center">

  # 🏆 AudioForge

  ### **Your Pythonic Gateway to Pristine Sound Recording.**
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Audio%20Engine-SoundDevice-ff69b4?style=for-the-badge" />
    <img src="https://img.shields.io/badge/Wave%20Writer-Wavio-blueviolet?style=for-the-badge" />
    <img src="https://img.shields.io/badge/Data%20Handling-NumPy-orange?style=for-the-badge&logo=numpy&logoColor=white" />
  </p>

  <p>
    <a href="#-the-essence">The Essence</a> •
    <a href="#-quick-start">Quick Start</a> •
    <a href="#-mastering-sound-settings">Mastering Sound Settings</a> •
    <a href="#-usage-examples">Usage Examples</a>
  </p>

</div>

---

## 🚀 The Essence

**AudioForge** streamlines the process of capturing high-quality audio directly from your microphone using Python. By combining `sounddevice` for efficient hardware interaction and `wavio` for robust WAV file writing, it offers a clean, reliable, and highly configurable solution. Say goodbye to complex audio APIs and hello to crystal-clear recordings with just a few lines of code! 🎧✨

## ⭐ Features

* **⚡ High-Performance Capture:** Utilizes `sounddevice` for low-latency, real-time audio input.
* **📊 NumPy Integration:** Records audio directly into NumPy arrays, making post-processing a breeze.
* **💾 Flawless WAV Export:** `wavio` ensures your recordings are saved with perfect fidelity and metadata.
* **🎚️ Customizable Settings:** Full control over sample rate, duration, channels, and bit depth.
* **✅ Cross-Platform:** Works seamlessly on Windows, macOS, and Linux.

---

## 🧠 How It Works

At its heart, AudioForge translates the analog world of sound into the digital realm with precision:

1.  **Microphone Input:** `sounddevice` acts as the intermediary, opening a stream to your selected microphone.
2.  **Analog-to-Digital Conversion (ADC):** Your sound card's ADC converts the continuous electrical signal from your mic into discrete numerical samples.
3.  **NumPy Array Formation:** These samples are streamed directly into a NumPy array, creating a digital representation of your sound wave.
4.  **WAV File Encoding:** `wavio` then takes this NumPy array, applies the chosen bit depth, and writes it into a standard `.wav` file, adding all necessary headers for playback.

---

## 🛠️ Installation

First, ensure you have the core Python libraries installed:

```bash
pip install sounddevice wavio numpy scipy
```

**Linux Specifics:** On many Linux distributions (like Ubuntu/Debian), you'll also need `PortAudio` development files:

```bash
sudo apt-get install libportaudio2 libportaudio-dev
```

---

## ⚙️ Mastering Sound Settings: Frequency, Duration, & Channels

Understanding these parameters is key to capturing the audio quality you need:

### ⏱️ Duration (in seconds)
This is straightforward: how long do you want to record?
* `duration = 5` (Records for 5 seconds)
* `duration = 60` (Records for 1 minute)

### 🔊 Sample Rate (`fs` - Frequency in Hz)
The sample rate defines how many "snapshots" of the sound wave are taken per second. A higher sample rate captures more detail, resulting in higher fidelity audio but also larger file sizes.

* **Common Sample Rates:**
    * `8000 Hz`: Good for speech (telephony quality).
    * `16000 Hz`: Improved speech quality, suitable for voice assistants.
    * `22050 Hz`: Radio quality, common for older multimedia.
    * `44100 Hz`: **CD Quality** (standard for music, podcasts, general recordings). This is the most common and recommended default.
    * `48000 Hz`: **DVD Quality** (often used in video production).
    * `96000 Hz` / `192000 Hz`: High-resolution audio, used in professional studios for ultimate detail.

    **Recommendation:** For most general-purpose recordings, `44100 Hz` or `48000 Hz` is ideal.

### 🎧 Channels
This refers to the number of independent audio streams.
* `channels = 1`: **Mono** (single-channel recording, common for voice).
* `channels = 2`: **Stereo** (two-channel recording, provides a sense of spatial audio, standard for music).

### 📏 Sample Width (`sampwidth`)
Determines the **bit depth** or the number of bits used to represent each audio sample. Higher bit depth means a larger dynamic range (difference between quietest and loudest sounds) and less quantization noise.

* `sampwidth = 2` (16-bit): Standard for CD audio. Good balance of quality and file size.
* `sampwidth = 3` (24-bit): Professional audio quality, larger dynamic range, less noise. Recommended for critical recordings.
* `sampwidth = 4` (32-bit float): Highest precision, often used in processing as it avoids clipping. Files are larger.

---

## ▶️ Usage Examples

Here's how to harness AudioForge for your recording needs:

```python
import sounddevice as sd
import wavio
import numpy as np

```
---

## 🤝 Contributing

Got ideas for a real-time visualizer, a pause function, or MP3 export? We welcome contributions\!

1.  Fork this repository. 🍴
2.  Create your feature branch (`git checkout -b feature/new-fancy-thing`). ✨
3.  Commit your changes (`git commit -am 'Add an awesome new feature'`). 💬
4.  Push to the branch (`git push origin feature/new-fancy-thing`). ⬆️
5.  Open a Pull Request\! 💖


---

<div align="center">
  <sub>Capturing the world, one sound wave at a time. 🌍🎤</sub>
