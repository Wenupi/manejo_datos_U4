import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties

path = '/Users/javier/Documents/University/'\
       '5th_semester/Experimental physics/Unidad4_MovBrowniano/Videos/datos_mov_browniano.xlsx'
DF = pd.read_excel(path)

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

font = FontProperties()
font.set_family('serif')
fig1, ax1 = plt.subplots(figsize=(4.0, 3.2))
ax1.scatter(np.arange(1,31,1), valores_coeficientes_dif, color='black', marker="D", s=20)
#ax1.plot(np.arange(1,31,1), promedio_coeficientes, color='#217a00')
ax1.axhline(y=promedio_coeficientes, color='#217a00', linestyle='--',
            label='D='+str('%.3f' %(promedio_coeficientes)))
ax1.legend()
ax1.set_xlim([0, 31])
ax1.set_ylim([0, 6])
ax1.set_xlabel('Número del video', fontproperties=font)
ax1.set_ylabel(r'Coef. de difusión [$mm^2/s$]', fontproperties=font)
ax1.set_title('Coeficientes de difusión', fontproperties=font)
fig1.tight_layout()    
fig1.savefig("coefs_difusion")

fig2, ax2 = plt.subplots(figsize=(4.0, 3.2))
ax2.plot(t_30, r_30, color='black')
ax2.set_xlabel('Tiempo [t]', fontproperties=font)
ax2.set_ylabel('Distancia [mm]', fontproperties=font)
ax2.set_title('Desplazamiento de la partícula', fontproperties=font)
ax2.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax2.xaxis.set_tick_params(labelsize=7)
ax2.yaxis.set_tick_params(labelsize=7)
fig2.tight_layout()    
fig2.savefig("desplazamiento_30_video")
