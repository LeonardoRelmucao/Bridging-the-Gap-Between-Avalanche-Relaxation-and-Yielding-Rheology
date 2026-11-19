import matplotlib.pyplot as plt
import pandas as pd
import os
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# obtener el path actual
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

################
#### STYLES ####

simbols = ['D', 'v', '^', '<', '>', 'p', 'h', '8', '1', '2', '3', '4', 'x', '+', 'D', '|', '_'] # simbolos para las lineas
colors  = ['#E63946', '#2A9D8F', '#E9C46A', '#457B9D', '#F4A261', '#00B4D8', '#9D4EDD', '#FF6F91', '#6A994E', '#6D6875'] # colores para las lineas

axes_limits_x =       {'VL': [0.0006, 60], 'CG': [0.005, 30], 'SD': [-0.1, 7.3]} # limites de los ejes x
axes_limits_x_inset = {'VL': [10, 100000], 'CG': [2, 10000],  'SD': [-0.1, 58]} # limites de los ejes x del inset

axes_limits_y =       {'VL': [0.75, 100], 'CG': [0.75, 100], 'SD': [0.05, 1.05]} # limites de los ejes y
axes_limits_y_inset = {'VL': [0.75, 100], 'CG': [0.75, 100], 'SD': [0.05, 1.05]} # limites de los ejes y del inset

plot_size = (7.5, 6) # tamaño de la figura
linewidth = 5 # grosor de las lineas
markersize = 15 # tamaño de los marcadores

inset_position = (0.46, -0.02, 7.5/6, 6/6) # posicion del inset
linewidth_inset = 4 # grosor de las lineas del inset
markersize_inset = 12 # tamaño de los marcadores del inset

legend_fontsize = 20 # tamaño de la leyenda
legend_position = (0.03, 0.37) # posicion de la leyenda

line_width = 3 # grosor de las lineas en los ejes
label_fontsize = 22 # tamaño de las etiquetas de los ejes

line_width_inset = 2 # grosor de las lineas del inset en los ejes
label_fontsize_inset = 16 # tamaño de las etiquetas de los ejes del inset

################
################

exp     = {'VL': 1.9, 'CG': 1.3, 'SD': 1.9} # exponente z

limit   = {'VL': [11, 11, 11, 11, 11, 11],
           'CG': [34, 34, 34, 34, 34, 34, 34],
           'SD': [34, 34, 34, 34, 34, 34, 34, 34]}

T_r = ["114.4", "397.6", "1379.2", "4776.8"]
#T_r = ["114", "397", "1379", "4776"]


################
################

def plot_lambdaF(T, relaxation):
     # Crear una figura y un subplot principal
    fig, ax1 = plt.subplots(figsize=plot_size)

    # Crear un inset (ax1) dentro de ax2
    ax2 = inset_axes(ax1, width="40%", height="40%", loc='upper left', bbox_to_anchor=inset_position, bbox_transform=ax1.transAxes)  # Ajustar el tamaño y la posición del inset

    for i in range(0, T):
        current_N = 1024 * 2**i
        tr = T_r[i]


        #lambdaF = pd.read_csv('/Users/Usuario/Desktop/Investigacion_Doctorado/draft_graficos_formato_final/draft_graficos_formato_final/correlacion/SRF_SD/correl_SRF_%s_%s.csv' % (relaxation, tr), sep=';')

        lambdaF = pd.read_csv('/home/leonardo/Escritorio/Investigacion_doctorado/correlation/SRF_SD/correl_SRF_%s_%s.csv' % (relaxation, tr), sep=';')



        #lambdaF = pd.read_csv("/home/leonardo/Escritorio/draft_graficos_formato_final/draft_graficos_formato_final/correlacion/SRF_SD" + '/correl_SRF_%s_%s.csv' % (relaxation, tr), sep=';')

        lambdaF = lambdaF.head(limit[relaxation][i])
        x = lambdaF['x']
        x_colaps = lambdaF['x_colaps']
        correl = lambdaF['correl']
        #print(x)

        tr_val = float(T_r[i])
        scientific_label = r"{:.1e}".format(tr_val).replace("e+0", "e+").replace("e+", r" \times 10^{") + "}"

        # Graficar en el subplot principal (ax1)
        ax1.plot(x_colaps, correl, '--'+simbols[i], label=r'$t_r = %s$' % scientific_label, linewidth=linewidth, markersize=markersize, color=colors[i])

        # Graficar en el inset (ax2)
        ax2.plot(x, correl, '--'+simbols[i], label=r'$t_r = %s$' % scientific_label, color=colors[i], linewidth=linewidth_inset, markersize=markersize_inset)

    # Configurar el inset (ax1)
    ax1.set_yscale('log')
    #ax1.set_xscale('log')
    ax1.tick_params(axis='both', which='major', labelsize=label_fontsize, width=line_width, length=6)  # Aumentar el tamaño de los números de los ejes del inset
    ax1.tick_params(axis='both', which='minor', labelsize=label_fontsize, width=line_width, length=3)  # Aumentar el tamaño de los números de los ejes del inset
    for spine in ax1.spines.values():
        spine.set_linewidth(line_width)  # Aumentar el grosor de las líneas de los bordes del inset
    ax1.legend(fontsize=legend_fontsize, loc='upper left', bbox_to_anchor=legend_position, borderaxespad=0.)
    ax1.set_ylim(axes_limits_y[relaxation])
    ax1.set_xlim(axes_limits_x[relaxation] )


    # Configurar el subplot principal (ax2)
    ax2.set_yscale('log')
    #ax2.set_xscale('log')
    ax2.tick_params(axis='both', which='major', labelsize=label_fontsize_inset, width=line_width_inset, length=4.5)  # Aumentar el tamaño de los números de los ejes del inset
    ax2.tick_params(axis='both', which='minor', labelsize=label_fontsize_inset, width=line_width_inset, length=2.5)  # Aumentar el tamaño de los números de los ejes del inset
    for spine in ax2.spines.values():
        spine.set_linewidth(line_width_inset)  # Aumentar el grosor de las líneas de los bordes del inset
    ax2.set_ylim(axes_limits_y_inset[relaxation])
    ax2.set_xlim(axes_limits_x_inset[relaxation] )

    plt.tight_layout()  # Ajustar el diseño para que no se superpongan los elementos

    # Guardar la figura




    #fig.savefig("/Users/Usuario/Desktop/Investigacion_Doctorado/draft_graficos_formato_final/draft_graficos_formato_final/correlacion/SRF_SD" + '/correl_%s.png' % (relaxation), dpi=900)
    #fig.savefig("/home/leonardo/Escritorio/draft_graficos_formato_final/draft_graficos_formato_final/correlacion/SRF_SD" + '/correl_%s.png' % (relaxation), dpi=900)
    fig.savefig("/home/leonardo/Escritorio/Investigacion_doctorado/correlation/SRF_SD" + '/correl_%s.png' % (relaxation), dpi=900)

    # cerrar la figura
    plt.close(fig)


if __name__ == '__main__':
    #plot_lambdaF(7, 'CG')
    plot_lambdaF(4, 'SD')
