import numpy as np

def getFreq(x, Fs):
  f_min = 10
  f_max = 5000
  spectrum = np.abs(np.fft.fft(x))
  N = len(spectrum)
  end_id = int(N/2)
  A_spc = spectrum[:end_id]
  A_spc[1:N] = 2*A_spc[1:N]
  ids = np.arange(end_id)
  f = Fs*ids/N
  ids = ids[f <= f_max]
  f = f[ids]
  ids = ids[f >= f_min]
  f = f[ids]
  A_spc = A_spc[ids]
  WaveLength = freq_to_WaveLength(f, f_min, f_max)
  RGB = WaveLength_to_RGB(WaveLength)

  mean_color = 255*color_mean(RGB, A_spc)

  return mean_color



def color_mean(RGB,A):

  mean = np.array([np.sum(RGB[:,0]*A), np.sum(RGB[:,1]*A), np.sum(RGB[:,2]*A)])
  mean /= np.sum(A)


  print((mean[0]+mean[1]+mean[2])/3)

  return mean



def freq_to_WaveLength(f, f_min, f_max):

  L_min = 380
  L_max = 780 

  L =  (f - f_min) / (f_max - f_min) * (L_max - L_min) + L_min

  return L


def WaveLength_to_RGB(WaveLength_array):

  RGB = np.zeros((len(WaveLength_array),3))

  for i, WaveLength in enumerate(WaveLength_array):

    assert(WaveLength >= 380.0 and WaveLength<= 780.0)
    
    if ((WaveLength >= 380.0) and (WaveLength <= 410.0)):
      R =0.6-0.41*(410.0-WaveLength)/30.0
      G = 0.0
      B = 0.39+0.6*(410.0-WaveLength)/30.0

    elif ((WaveLength >= 410.0) and (WaveLength <= 440.0)):
      R =0.19-0.19*(440.0-WaveLength)/30.0
      G = 0.0
      B = 1.0

    elif ((WaveLength >= 440.0) and (WaveLength<= 490.0)):
      R =0
      G = 1-(490.0-WaveLength)/50.0
      B = 1.0

    elif ((WaveLength >= 490.0) and (WaveLength <= 510.0)):
      R =0
      G = 1
      B = (510.0-WaveLength)/20.0

    elif ((WaveLength >= 510.0) and (WaveLength <= 580.0)):
      R =1-(580.0-WaveLength)/70.0
      G = 1
      B = 0
    elif ((WaveLength >= 580.0) and (WaveLength<= 640.0)):
      R =1
      G = (640.0-WaveLength)/60.0
      B = 0
    elif ((WaveLength >= 640.0) and (WaveLength <= 700.0)):
      R =1
      G = 0
      B = 0
    elif ((WaveLength >= 700.0) and (WaveLength<= 780.0)):
      R =0.35+0.65*(780.0-WaveLength)/80.0
      G = 0
      B = 0
    
    RGB[i][0] = R
    RGB[i][1] = G
    RGB[i][2] = B

  return RGB




def GetColorArray(x, T, Fs):
  len_for_one_color = int(T*Fs)


  n = int(len(x)/len_for_one_color)

  id_start = 0
  id_end = len_for_one_color

  step = len_for_one_color // 2
  N = int((len(x) - len_for_one_color) / step)
  color_array = np.zeros((N+1,3))

  for i in range(N):
    color_array[i,:] = getFreq(x[id_start:id_end], Fs)
    id_start += step
    id_end += step

  color_array[N,:] = getFreq(x[id_start:len(x)],Fs)

  return color_array








