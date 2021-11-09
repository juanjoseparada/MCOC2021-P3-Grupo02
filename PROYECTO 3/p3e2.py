

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import dijkstra_path





G = nx.Graph()

# AGREGAR NODOS
G.add_node("0", pos=(1,2))
G.add_node("1", pos=(4,3))
G.add_node("2", pos=(1,6))
G.add_node("3", pos=(7,3))
G.add_node("4", pos=(10,1))
G.add_node("5", pos=(0,10))
G.add_node("6", pos=(4,0))
G.add_node("7", pos=(5,8))
G.add_node("8", pos=(9,7))
G.add_node("9", pos=(8,10))

# COLORES




# AGREGAR ARCOS     
G.add_edge("0","1", tiempo = (((1-4)**2+(2-3)**2)**0.5/40))
G.add_edge("0","2", tiempo = (((1-1)**2+(2-6)**2)**0.5/120))
G.add_edge("0","6", tiempo = (((1-4)**2+(2-0)**2)**0.5/120))
G.add_edge("1","2", tiempo = (((4-1)**2+(3-6)**2)**0.5/40))
G.add_edge("1","3", tiempo = (((4-7)**2+(3-3)**2)**0.5/60))
G.add_edge("1","7", tiempo = (((4-5)**2+(3-8)**2)**0.5/40))
G.add_edge("2","5", tiempo = (((1-0)**2+(6-10)**2)**0.5/40))
G.add_edge("3","4", tiempo = (((7-10)**2+(3-1)**2)**0.5/60))
G.add_edge("3","6", tiempo = (((7-4)**2+(3-0)**2)**0.5/40))
G.add_edge("3","7", tiempo = (((7-5)**2+(3-8)**2)**0.5/60))
G.add_edge("3","8", tiempo = (((7-9)**2+(3-7)**2)**0.5/40))
G.add_edge("4","6", tiempo = (((10-4)**2+(1-0)**2)**0.5/120))
G.add_edge("4","8", tiempo = (((10-9)**2+(1-7)**2)**0.5/120))
G.add_edge("5","7", tiempo = (((0-5)**2+(10-8)**2)**0.5/120))
G.add_edge("7","9", tiempo = (((5-8)**2+(8-10)**2)**0.5/60))
G.add_edge("8","9", tiempo = (((9-8)**2+(7-10)**2)**0.5/60))

# Posicion de los nodos

pos = nx.get_node_attributes(G, "pos")  




eje_y = [0,1,2,3,4,5,6,7,8,9,10]
eje_x=[0,1,2,3,4,5,6,7,8,9,10]






# LISTA ARCOS
arcos = []
for ni, nf in G.edges:
    arcos.append((ni,nf))



###################################################### GRAFICO PRINCIPAL #########################################################
# COLORES
rgb= lambda h: tuple(int(h[i:i+2], 16) /256. for i in (0,2,4))
GRIS = rgb("7C7C7C")
CAFE = rgb("6C4E09")
VERDE = rgb("00701A")
# AGREGAR ARCOS     
G.add_edge('0','1',v = 40, color = CAFE   , t = ((((4-1)**2)+ (3-2)**2)**0.5)/40)
G.add_edge('0','2',v = 120, color = GRIS, t = ((((1-1)**2)+ (6-2)**2)**0.5)/120)
G.add_edge('0','6',v = 120, color = GRIS, t = ((((4-1)**2)+ (0-2)**2)**0.5)/40)
G.add_edge('1','2',v = 40, color = CAFE, t = ((((4-1)**2)+ (3-6)**2)**0.5)/40)
G.add_edge('1','3',v = 60, color = VERDE, t = ((((4-7)**2)+ (3-3)**2)**0.5)/60)
G.add_edge('1','7',v = 40, color = CAFE, t = ((((4-5)**2)+ (3-8)**2)**0.5)/40)
G.add_edge('2','5',v = 40, color = CAFE, t = ((((0-1)**2)+ (10-6)**2)**0.5)/40)
G.add_edge('3','4',v = 60, color = VERDE, t = ((((7-10)**2)+ (3-1)**2)**0.5)/40)
G.add_edge('3','6',v = 40, color = CAFE, t = ((((4-7)**2)+ (0-3)**2)**0.5)/40)
G.add_edge('3','7',v = 60, color = VERDE, t = ((((5-7)**2)+ (8-3)**2)**0.5)/40)
G.add_edge('3','8',v = 40, color = CAFE, t = ((((9-7)**2)+ (3-7)**2)**0.5)/40)
G.add_edge('4','8',v = 120, color = GRIS, t = ((((10-9)**2)+ (7-1)**2)**0.5)/40)
G.add_edge('4','6',v = 120, color = GRIS, t = ((((4-10)**2)+ (0-1)**2)**0.5)/40)
G.add_edge('5','7',v = 120, color = GRIS, t = ((((0-5)**2)+ (10-8)**2)**0.5)/40)
G.add_edge('7','9',v = 60, color = VERDE, t = ((((8-5)**2)+ (10-8)**2)**0.5)/40)
G.add_edge('8','9',v = 60, color = VERDE, t = ((((8-9)**2)+ (10-7)**2)**0.5)/40)


 # iterar los arcos
 
  

ejey_name =[0,1,2,3,4,5,6,7,8,9,10]
eje_y = [0,1,2,3,4,5,6,7,8,9,10]
eje_x=[0,1,2,3,4,5,6,7,8,9,10]
ejex_name= [0,1,2,3,4,5,6,7,8,9,10]

# GRAFICA
pos=nx.get_node_attributes(G,"pos")
colors = nx.get_edge_attributes(G,'color').values()
fig, ax = plt.subplots()

nx.draw(G,pos = pos, edge_color = colors, with_labels=True)
nx.draw_networkx_edges(G, pos, arco= arcos , edge_color =colors , width = 3, ax=ax)
limits=plt.axis('on')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

plt.grid()
plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.yticks(eje_y,ejey_name)
plt.xticks(eje_x, ejex_name)

plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.savefig("fig1")
plt.show()


# Con dijkstra  encontramos las rutas con menor tiempo
camino09 = dijkstra_path(G, source="0", target="9", weight="tiempo")
camino45 = dijkstra_path(G, source="4", target="5", weight="tiempo")
camino04 = dijkstra_path(G, source="0", target="4", weight="tiempo")
######################################################   RUTA 0 -- 9 ####################################################


# COLOR SEGUN RUTA OPTIMA
color09 = []
for ni, nf in G.edges:
    if ni in camino09 and nf in camino09:
        color09.append("r")

    else:
        color09.append(rgb("7C7C7C"))

    
# GROSOR SEGUN RUTA OPTIMA
grosor09 = []
for ni, nf in G.edges:
    if ni in camino09 and nf in camino09:
        grosor09.append(4)
    else:
        grosor09.append(2)
    

    

# Calculamos el tiempo total de la ruta
tiempo= 0
for i in range(len(camino09)-1):
    o= camino09[i]
    d= camino09[i+1]
    tiempo_tramo = G.edges[[o,d]]["tiempo"]
    tiempo +=tiempo_tramo
    
    
# Graficamos
fig, ax = plt.subplots()
nx.draw(G, pos = pos, with_labels=True)
nx.draw_networkx_edges(G, pos, arco =arcos, edge_color =color09, width = grosor09, ax=ax)
ax.grid()
ax.set_axisbelow(True)
limits=plt.axis('on')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
ax.set_xlabel("X [km]")
ax.set_ylabel("Y [km]")
plt.xticks(eje_x, eje_x)
plt.yticks(eje_y, eje_y)
plt.suptitle(f"Tiempo de Viaje Ruta 0-9 = {round(tiempo, 2)} [hrs] = {round(tiempo*60, 2)} [min]")
plt.savefig("fig2", bbox_inches = 'tight')
plt.show()
######################################################   RUTA 4 -- 5 ####################################################


# COLOR SEGUN RUTA OPTIMA
color45 = []
for ni, nf in G.edges:
    if ni in camino45 and nf in camino45:
        color45.append("r")

    else:
        color45.append(rgb("7C7C7C"))

    
# GROSOR SEGUN RUTA OPTIMA
grosor45 = []
for ni, nf in G.edges:
    if ni in camino45 and nf in camino45:
        grosor45.append(4)
    else:
        grosor45.append(2)
    

    

# Calculamos el tiempo total de la ruta
tiempo= 0
for i in range(len(camino45)-1):
    o= camino45[i]
    d= camino45[i+1]
    tiempo_tramo = G.edges[[o,d]]["tiempo"]
    tiempo +=tiempo_tramo
    
    
# Graficamos
fig, ax = plt.subplots()
nx.draw(G, pos = pos, with_labels=True)
nx.draw_networkx_edges(G, pos, arco =arcos, edge_color =color45, width = grosor45, ax=ax)
ax.grid()
ax.set_axisbelow(True)
limits=plt.axis('on')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
ax.set_xlabel("X [km]")
ax.set_ylabel("Y [km]")
plt.xticks(eje_x, eje_x)
plt.yticks(eje_y, eje_y)
plt.suptitle(f"Tiempo de Viaje Ruta 4-5 = {round(tiempo, 2)} [hrs] = {round(tiempo*60, 2)} [min]")
plt.savefig("fig3", bbox_inches = 'tight')
plt.show()

######################################################   RUTA 0 -- 4 ####################################################


# COLOR SEGUN RUTA OPTIMA
color04 = []
for ni, nf in G.edges:
    if ni in camino04 and nf in camino04:
        color04.append("r")

    else:
        color04.append(rgb("7C7C7C"))

    
# GROSOR SEGUN RUTA OPTIMA
grosor04 = []
for ni, nf in G.edges:
    if ni in camino04 and nf in camino04:
        grosor04.append(4)
    else:
        grosor04.append(2)
    

    

# Calculamos el tiempo total de la ruta
tiempo= 0
for i in range(len(camino04)-1):
    o= camino04[i]
    d= camino04[i+1]
    tiempo_tramo = G.edges[[o,d]]["tiempo"]
    tiempo +=tiempo_tramo
    
    
# Graficamos
fig, ax = plt.subplots()
nx.draw(G, pos = pos, with_labels=True)
nx.draw_networkx_edges(G, pos, arco =arcos, edge_color =color04, width = grosor04, ax=ax)
ax.grid()
ax.set_axisbelow(True)
limits=plt.axis('on')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
ax.set_xlabel("X [km]")
ax.set_ylabel("Y [km]")
plt.xticks(eje_x, eje_x)
plt.yticks(eje_y, eje_y)
plt.suptitle(f"Tiempo de Viaje Ruta 0-4 = {round(tiempo, 2)} [hrs] = {round(tiempo*60, 2)} [min]")
plt.savefig("fig4", bbox_inches = 'tight')
plt.show()




























