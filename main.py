import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 40000
dur = 60
recording = sd.rec(int(dur * freq), samplerate=freq, channels=2)
print("Recording started:")
sd.wait()
print("Recording ended.")
wv.write("rec.wav",recording,freq,sampwidth=2)
