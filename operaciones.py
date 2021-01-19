from math import e,pi
import numpy as np
from scipy import signal
import wave,audioop
from pydub import AudioSegment
import soundfile as sf

def amplificar_audio(amplitud):
    with wave.open('campana.wav', 'rb') as wav:
        p = wav.getparams()
        with wave.open('parte01.wav', 'wb') as audio:
            audio.setparams(p)
            frames = wav.readframes(p.nframes)
            audio.writeframesraw( audioop.mul(frames, p.sampwidth, amplitud))

def sumar_audio(volumen):
    audio_file = "campana.wav"
    song = AudioSegment.from_mp3(audio_file)
    new = song.low_pass_filter(1000)
    new1 = new.high_pass_filter(1000)
    audio = new1 + volumen
    audio.export("parte01.wav", "wav")

def reflejo(audio):
    return np.flip(audio)

def desplazamiento(senal,h):
    nuevo = np.array(np.append(np.zeros(h*128),senal))
    return nuevo

def fft(a):
    n = len(a)
    if(n == 1):
        return a
    wn = e**((2*pi*1j)/n)
    w = 1

    a0 = []
    a1 = []
    for i in range(len(a)):
        if i%2==0:
            a0.append(a[i])
        else:
            a1.append(a[i])
    
    y0 = fft(a0)
    y1 = fft(a1)

    y = [0 for i in range(n)]
    for k in range(0,(n//2)):
        y[k] = y0[k] + w*y1[k]
        y[k+(n//2)] = y0[k] - w*y1[k]
        w = w*wn
    return y

def convolucion(a, b):
    Na = len(a)
    Nb = len(b)

    y = [0 for x in range(0,Na+Nb-1)]
    Ny = len(y)

    #Sumatoria de convolución
    for n in range(0,Ny):
        k = n; f = 1;
        while k >= 0:
            if n >= Na:   #Este if es para cuando el vector que va recorriendo se sale del indice de a[k]
                k = Na-f; f += 1;
                
            y[n] += a[k]*b[n-k] #Ecuación de la convolución
            k -= 1
            if (n-k) >= Nb:
                break
    return np.array(y)

def convolucion_audio(audio1,audio2):#para el audio porque el otro algoritmo tarda mucho
    return signal.convolve(audio1,audio2)

        