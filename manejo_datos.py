import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties

path = 'datos_mov_browniano.xlsx'
DF = pd.read_excel(path, engine='openpyxl')

"""
Funciones para calcular el promedio de los desplazamientos
al cuadrado, y para calcular el coef. de difusión ocupando
esta función.
"""
def promedio_desplazamiento_cuadratico(r):
    return np.mean(r**2)

def coef_difusion(r, t):
    return promedio_desplazamiento_cuadratico(r)/(2*t)

# Valores del tiempo y desplazamiento del video 30
t_30 = DF['t30']
r_30 = DF['r30']*1000

# Arreglo con 0s para guardar los valores de los coefs.
valores_coeficientes_dif = np.zeros(int(len(DF.columns)/2))

for i in range(1, int(len(DF.columns)/2)+1):
    # Este bucle toma el tiempo que duró la grabación, para poder calcular
    # el coef. de difusión para cada video
    t_max = np.max(DF['t'+str(i)])
    valores_coeficientes_dif[i-1] = coef_difusion(DF['r'+str(i)]*1000, t_max)

# Cálculo del promedio y desv. estándar
promedio_coeficientes = np.mean(valores_coeficientes_dif)
desv_estandar_coeficientes = np.std(valores_coeficientes_dif)

print('El valor del coeficiente de difusión es {:f} +- {:f}'
      .format(promedio_coeficientes, desv_estandar_coeficientes))

plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = "#cccccc"
font = FontProperties()
font.set_family('serif')
font.set_size(10)
fig1, ax1 = plt.subplots(figsize=(3.25, 3.25))
ax1.plot(np.arange(1, 31), valores_coeficientes_dif, c='r', ls="", marker="x", markersize=5)
ax1.axhline(y=promedio_coeficientes, color='black', linestyle='--')
plt.text(25, promedio_coeficientes+0.15, r"$D=$"+str(round(promedio_coeficientes, 3)), fontsize=10,
                     ha='center', va='center')
ax1.set_xlim([0, 31])
ax1.set_ylim([0, 6])
ax1.set_xlabel('Número del video', fontproperties=font)
ax1.set_ylabel(r'Coeficiente de difusión [mm$^2$/s]', fontproperties=font)
ax1.tick_params(direction="in")
ax1.xaxis.set_tick_params(labelsize=10)
ax1.yaxis.set_tick_params(labelsize=10)
ax1.yaxis.set_tick_params(rotation=90)
ax1.tick_params(direction="in", top=True, right=True)
fig1.tight_layout()    
fig1.savefig("img/diffcoeff.pdf")

fig2, ax2 = plt.subplots(figsize=(3.25, 3.25))
ax2.plot(t_30, r_30, drawstyle="steps-mid", c="red", linewidth=1)
ax2.set_xlabel('Tiempo [s]', fontproperties=font)
ax2.set_ylabel('Distancia al origen [mm]', fontproperties=font)
ax2.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax2.xaxis.set_tick_params(labelsize=10)
ax2.yaxis.set_tick_params(labelsize=10)
ax2.yaxis.set_tick_params(rotation=90)
ax2.tick_params(direction="in", top=True, right=True)
fig2.tight_layout()    
fig2.savefig("img/desplazamiento30.pdf")
