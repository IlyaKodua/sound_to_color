import numpy as np
from scipy.io import wavfile
from sound import*
import matplotlib.pyplot as plt

wav_fname = 'example/ws.wav'

T = 0.1

Fs, x = wavfile.read(wav_fname)


x = x[:,0]





color_array = GetColorArray(x, T, Fs)



