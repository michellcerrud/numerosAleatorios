#Numeros aleatorios Normal
import numpy as np
mu, sigma = 0, 0.1
#Creamos nuestras variables de media y desviacion
s = np.random.normal(mu, sigma, 32000)
#Utilizamos random normal en ves de uniforma, genero 32,000 numeros aleatorios
abs(mu - np.mean(s)) < 0.01

abs(sigma - np.std(s, ddof=1)) < 0.01

s

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 30, normed=True)
#cuento los elementos que hay
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
#mando a graficarlo
plt.show()
