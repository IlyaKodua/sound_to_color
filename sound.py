import numpy as np
import matplotlib.pyplot as plt 

def getFreq(x, Fs):
  f_min = 130.81
  f_max = 1975
  spectrum = np.abs(np.fft.fft(x))
  N = len(spectrum)
  end_id = int(N/2)
  A_spc = spectrum[:end_id]
  A_spc[1:N] = 2*A_spc[1:N]
  ids = np.arange(end_id)
  f = Fs*ids/N

  plt.plot(f, A_spc, 'r')
  plt.show()
  ids = ids[f <= f_max]
  f = f[ids]
  ids = ids[f >= f_min]
  f = f[ids]
  A_spc = A_spc[ids]
  lamb = np.sum(freq_to_lambd(f, f_min, f_max) * A_spc)/np.sum(A_spc)

  return lamb






def freq_to_lambd(f, f_min, f_max):

  L_min = 380
  L_max = 770 

  L =  (f - f_min) / (f_max - f_min) * (L_max - L_min) + L_min

  return L



