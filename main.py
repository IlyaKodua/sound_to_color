import numpy as np
from scipy.io import wavfile
from sound import*


wav_fname = 'example/ws.wav'

T = 0.1

Fs, x = wavfile.read(wav_fname)



lm = getFreq(x[:,0], Fs)

print("end")



