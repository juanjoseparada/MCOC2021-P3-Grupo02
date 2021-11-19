# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 13:05:03 2021

@author: juanp
"""


import osmnx as ox
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gps 

zonas_gdf= gps.read_file("eod.json")
#print(f"{zonas_gdf.columns =}")

ox.config(use_cache=True, log_console=True)

north=-33.2
south= -33.7
east= -70.2
west=-70.9

G= ox.graph_from_bbox(north, south, east, west, 
                      network_type="drive",
                      custom_filter='["highway"~"motoroway|primary|construction|secondary|tertiary"]')

id_zonas_a_graficar=[599, 153, 146, 599, 683, 666, 677, 682,
                     306, 307, 287, 288, 289, 290, 291, 304,
                     266, 267, 434, 435, 281, 426, 283, 440,
                     278, 439, 471, 684]



# print (len(id_zonas_a_graficar))





# ACA SE DISCRETIZA N LAS ZONAS CON MAYOR DEMANDA PARA LOS VIAJES QUE ENTRAN Y SALES DE AVO


i=0
zona_all=[]
for i in id_zonas_a_graficar:
    zona_all.append(i)
# print (zona_all)


i=0
for wa in open('mod.csv'):
    sl = wa.split(',')
    o = int(sl[0])
    d = int(sl[1])
    dda = np.double(sl[2])
    # print (o)
    if o in id_zonas_a_graficar or d in id_zonas_a_graficar and dda > 100:
        zona_all.append(o)
        zona_all.append(d)
        i+=dda

print("")
print ("Viajes totales : ",i)
print("")
zona_oficial=[]

for i in zona_all:
    if i not in zona_oficial:
        zona_oficial.append(i)
    else:
        continue


#ACA SE VEN LAS ZONAS CON MAYO FLUJO QUE ESTRAN Y SALEN DE AVO
i=0

print("")
print ("Viajes con mayor demanda :")
print("")
for wa in open('mod.csv'):
    sl = wa.split(',')
    o = int(sl[0])
    d = int(sl[1])
    dda = np.double(sl[2])
    # print (o)
    if o in id_zonas_a_graficar or d in id_zonas_a_graficar:
        if dda > 1500:
            i+=dda
            # print(f(" Origen {o}" Destino))
            print (f" PAR OD [{o}, {d}]  con demanda {dda}")
        else:
            continue
               



zonas_seleccionadas= zonas_gdf[zonas_gdf["ID"].isin(zona_all)] 


fig, ax =plt.subplots(1, 1)
zonas_seleccionadas.plot(ax=ax, color="#CDCDCD")






gdf_nodes, gdf_edges= ox.graph_to_gdfs(G)

g_edges_clipeado = gps.clip(gdf_edges, zonas_seleccionadas)



g_edges_clipeado[g_edges_clipeado.highway=="primary"].plot(ax=ax, color = "yellow")
g_edges_clipeado[g_edges_clipeado.highway=="secondary"].plot(ax=ax, color = "green")
g_edges_clipeado[g_edges_clipeado.highway=="motorway"].plot(ax=ax, color = "orange")
g_edges_clipeado[g_edges_clipeado.highway=="tertiary"].plot(ax=ax, color = "blue")
g_edges_clipeado[g_edges_clipeado.highway=="construction"].plot(ax=ax, color = "red")
g_edges_clipeado[g_edges_clipeado.name=="Autopista Vespucio Oriente"].plot(ax=ax, color = "red")

plt.savefig("mapa.png")
plt.show()










