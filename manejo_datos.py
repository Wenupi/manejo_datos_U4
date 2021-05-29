import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties

path = 'datos_mov_browniano.xlsx'
path_plots = 'datos_mov_browniano_plots.xlsx'
DF = pd.read_excel(path, engine='openpyxl')
DF_plots = pd.read_excel(path_plots, engine='openpyxl')

"""
Funciones para calcular el promedio de los desplazamientos
al cuadrado, y para calcular el coef. de difusión ocupando
esta función.
"""
def promedio_desplazamiento_cuadratico(r):
    return np.mean(r**2)

def coef_difusion(r, t):
    return promedio_desplazamiento_cuadratico(r)/(4*t)

# Valores del tiempo y desplazamiento del video 30
t_30 = DF['t30']
r_30 = DF['r30']*1000
t_17 = DF['t17']
r_17 = DF['r17']*1000
t_25 = DF['t25']
r_25 = DF['r25']*1000
t_2 = DF['t2']
r_2 = DF['r2']*1000
x_path_30 = DF['x_path_30']*1000
y_path_30 = DF['y_path_30']*1000
t_path_30 = DF['t_path_30']
#x_path_17 = DF['x_path_30']*1000
#y_path_17 = DF['y_path_30']*1000
#t_path_17 = DF['t_path_30']

# Arreglo con 0s para guardar los valores de los coefs.
valores_coeficientes_dif = np.zeros(int((len(DF.columns)-3)/2))

for i in range(1, int((len(DF.columns)-3)/2)+1):
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
plt.rcParams.update({"font.size": 7, "font.family": "serif"})
font = FontProperties()
font.set_family('serif')
font.set_size(9)
fig1, ax1 = plt.subplots(figsize=(3.25, 3.25))
ax1.plot(np.arange(1, 31), valores_coeficientes_dif, c='black', ls="", marker="x", markersize=5)
ax1.axhline(y=promedio_coeficientes, color='black', linestyle='--', linewidth=1)
plt.text(25, promedio_coeficientes+0.1, r"$D=$"+str(round(promedio_coeficientes, 3)), fontsize=9,
                     ha='center', va='center')
ax1.set_xlim([0, 31])

ax1.set_xlabel('Número del video', fontproperties=font)
ax1.set_ylabel(r'Coeficiente de difusión [mm$^2$/s]', fontproperties=font)
ax1.tick_params(direction="in")
ax1.xaxis.set_tick_params(labelsize=9)
ax1.yaxis.set_tick_params(labelsize=9)
ax1.yaxis.set_tick_params(rotation=90)
ax1.tick_params(direction="in", top=True, right=True)
fig1.tight_layout()    
fig1.savefig("img/diffcoeff.pdf")

fig2, ax2 = plt.subplots(figsize=(3.25, 3.25))
ax2.plot(t_30, r_30, c="red", linewidth=1)
ax2.set_xlabel('Tiempo [s]', fontproperties=font)
ax2.set_ylabel('Distancia al origen [mm]', fontproperties=font)
ax2.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax2.xaxis.set_tick_params(labelsize=9)
ax2.yaxis.set_tick_params(labelsize=9)
ax2.yaxis.set_tick_params(rotation=90)
ax2.tick_params(direction="in", top=True, right=True)
fig2.tight_layout()    
fig2.savefig("img/desplazamiento30.pdf")

fig3, ax3 = plt.subplots(figsize=(3.25, 3.25))
ax3.plot(x_path_30, y_path_30, c="red", linewidth=1)
ax3.set_xlabel('Posición x [mm]', fontproperties=font)
ax3.set_ylabel('Posición y [mm]', fontproperties=font)
ax3.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax3.xaxis.set_tick_params(labelsize=9)
ax3.yaxis.set_tick_params(labelsize=9)
ax3.yaxis.set_tick_params(rotation=90)
ax3.tick_params(direction="in", top=True, right=True)
fig3.tight_layout()    
fig3.savefig("img/camino30.pdf")

fig4, ax4 = plt.subplots(figsize=(3.25, 3.25))
ax4.plot(t_2, r_2, c="red", linewidth=1)
ax4.set_xlabel('Tiempo [s]', fontproperties=font)
ax4.set_ylabel('Distancia al origen [mm]', fontproperties=font)
ax4.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax4.xaxis.set_tick_params(labelsize=9)
ax4.yaxis.set_tick_params(labelsize=9)
ax4.yaxis.set_tick_params(rotation=90)
ax4.tick_params(direction="in", top=True, right=True)
fig4.tight_layout()    
fig4.savefig("img/desplazamiento2.pdf")

fig5, ax5 = plt.subplots(figsize=(3.25, 3.25))
ax5.plot(DF_plots['t_path_2'], DF_plots['r2']*1000, c="red", linewidth=1)
ax5.set_xlabel('Tiempo [s]', fontproperties=font)
ax5.set_ylabel('Distancia al origen [mm]', fontproperties=font)
#ax5.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax5.xaxis.set_tick_params(labelsize=9)
ax5.yaxis.set_tick_params(labelsize=9)
ax5.yaxis.set_tick_params(rotation=90)
ax5.tick_params(direction="in", top=True, right=True)
fig5.tight_layout()    
fig5.savefig("img/desplazamiento2_analizar.pdf")

fig6, ax6 = plt.subplots(figsize=(3.25, 3.25))
ax6.plot(DF_plots['x_path_2']*1000, DF_plots['y_path_2']*1000, c="red", linewidth=1)
#ax6.scatter(DF_plots['x_path_2']*1000, DF_plots['y_path_2']*1000, marker='x', linewidths=0.3, color="#ad0303", alpha=1, zorder=2)
ax6.set_xlabel('Coordenada $x$ [mm]', fontproperties=font)
ax6.set_ylabel('Coordenada $y$ [mm]', fontproperties=font)
#ax6.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax6.xaxis.set_tick_params(labelsize=9)
ax6.yaxis.set_tick_params(labelsize=9)
ax6.yaxis.set_tick_params(rotation=90)
ax6.grid(True)
ax6.tick_params(direction="in", top=True, right=True)
fig6.tight_layout()    
fig6.savefig("img/camino2_analizar.pdf")

fig7, ax7 = plt.subplots(figsize=(3.25, 3.25))
ax7.plot(DF_plots['x_path_2']*1000, DF_plots['y_path_2']*1000, c="blue", linewidth=1, label='Video 2')
ax7.plot(DF_plots['x_path_17']*1000, DF_plots['y_path_17']*1000, c="green", linewidth=1, label='Video 17')
ax7.plot(DF['x_path_30']*1000, DF['y_path_30']*1000, c="red", linewidth=1, label='Video 30')
#ax7.scatter(DF_plots['x_path_2']*1000, DF_plots['y_path_2']*1000, marker='x', linewidths=0.3, color="#ad0303", alpha=1, zorder=2)
ax7.set_xlabel('Coordenada $x$ [mm]', fontproperties=font)
ax7.set_ylabel('Coordenada $y$ [mm]', fontproperties=font)
#ax7.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax7.xaxis.set_tick_params(labelsize=9)
ax7.yaxis.set_tick_params(labelsize=9)
ax7.yaxis.set_tick_params(rotation=90)
ax7.legend()
ax7.grid(True)
ax7.tick_params(direction="in", top=True, right=True)
fig7.tight_layout()    
fig7.savefig("img/camino_varios.pdf")

fig8, ax8 = plt.subplots(figsize=(3.25, 3.25))
ax8.plot(DF_plots['t_path_2'], DF_plots['r2']*1000, c="blue", linewidth=1, label='Video 2')
ax8.plot(DF_plots['t_path_17'], DF_plots['r17']*1000, c="green", linewidth=1, label='Video 17')
ax8.plot(DF['t30'], DF['r30']*1000, c="red", linewidth=1, label='Video 30')
ax8.set_xlabel('Tiempo [s]', fontproperties=font)
ax8.set_ylabel('Distancia al origen [mm]', fontproperties=font)
#ax8.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax8.xaxis.set_tick_params(labelsize=9)
ax8.yaxis.set_tick_params(labelsize=9)
ax8.yaxis.set_tick_params(rotation=90)
ax8.legend()
ax8.tick_params(direction="in", top=True, right=True)
fig8.tight_layout()    
fig8.savefig("img/desplazamiento_varios.pdf")

#t_30 = DF['t30']
#r_30 = DF['r30']*1000

#t_2 = DF['t2']
#r_2 = DF['r2']*1000
#x_path_30 = DF['x_path_30']*1000
#y_path_30 = DF['y_path_30']*1000
#t_path_30 = DF['t_path_30']

#fig5, ax5 = plt.subplots(figsize=(3.25, 3.25))
#ax5.plot(x_path_17, y_path_17, c="red", linewidth=1)
#ax5.set_xlabel('Posición x [mm]', fontproperties=font)
#ax5.set_ylabel('Posición y [mm]', fontproperties=font)
#ax5.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
#ax5.xaxis.set_tick_params(labelsize=9)
#ax5.yaxis.set_tick_params(labelsize=9)
#ax5.yaxis.set_tick_params(rotation=90)
#ax5.tick_params(direction="in", top=True, right=True)
#fig5.tight_layout()    
#fig5.savefig("img/camino30.pdf")