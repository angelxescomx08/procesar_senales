import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import operaciones
import scipy

# archivo = input('archivo de sonido:' )
archivo = 'campana.wav'
muestreo, sonido = waves.read(archivo)

# rango de observación en segundos
inicia = 0
termina = 3
# observación en número de muestra
a = int(inicia*muestreo)
b = int(termina*muestreo)
parte = sonido[a:b]

parte = operaciones.desplazamiento(parte,100)

# Salida # Archivo de audio.wav
print('archivo de parte[] grabado...')
#waves.write('parte01.wav', muestreo, parte)

# Gráfica
plt.plot(parte)
plt.show()

plt.plot(sonido)
plt.show()