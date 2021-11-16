# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 22:10:54 2021

@author: juanp
"""
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

f1=lambda f: 10. + f/120.
f2=lambda f: 14. + f/80.
f3=lambda f: 10. + f/240.

funr= "r: 10 + f/120"
funv= "v: 10 + f/120"
funz= "z: 10 + f/120"
funs= "s: 14 + f/80"
funy= "y: 14 + f/80"
funu= "u: 14 + f/80"
funw= "w: 14 + f/80"
funt= "t: 10 + f/240"
funx= "x: 10 + f/240"

#Matriz origen-destino
OD = {
      ("A","C"): 1100.,
      ("A","D"): 1110.,
      ("A","E"):1020,("B","C"):1140,
      ("B","D"):1160,
      ("D","C"):350,
      ("C","E"):1170,
      ("C","G"):1180,
      ("D","E"):1190,
      ("D","G"):1200
      }

#Copia OD
OD_target=OD.copy()


G=nx.DiGraph()

G.add_node("A",pos=(0,6))
G.add_node("B",pos=(0,4))
G.add_node("C",pos=(2,4))
G.add_node("D",pos=(2,2))
G.add_node("E",pos=(4,6))
G.add_node("G",pos=(4,4))



G.add_edge("A","B",fcosto=f1,flujo=0.,costo=0.,fun=funr, ruta="r")     #r
G.add_edge("A","C",fcosto=f2,flujo=0.,costo=0.,fun=funs, ruta="s")     #s
G.add_edge("B","C",fcosto=f3,flujo=0.,costo=0.,fun=funt, ruta="t")     #t
G.add_edge("B","D",fcosto=f2,flujo=0.,costo=0.,fun=funu, ruta="u")     #u
G.add_edge("D","C",fcosto=f1,flujo=0.,costo=0.,fun=funv, ruta="v")     #v
G.add_edge("D","G",fcosto=f2,flujo=0.,costo=0.,fun=funy, ruta="y")     #y
G.add_edge("C","G",fcosto=f3,flujo=0.,costo=0.,fun=funx, ruta="x")     #x
G.add_edge("C","E",fcosto=f2,flujo=0.,costo=0.,fun=funw, ruta="w")     #w
G.add_edge("G","E",fcosto=f1,flujo=0.,costo=0.,fun=funz, ruta="z")     #z



def costo(ni,nf,attr):
    
    #print(f"ni = {ni} nf = {nf} attr={attr}")
    funcosto_arco=attr["fcosto"]
    flujo_arco=attr["flujo"]
    a= funcosto_arco(flujo_arco)
    return a




# incrementos = [0.1*9 , 0.01*9 , 0.001*9 , 0.0001*9 , 0.00001*9 , 0.000001*9 ,0.0000001*10]
# incrementos = 0.1*9 + 0.01*9 + 0.001*9 + 0.0001*9 + 0.00001*9 + 0.000001*9 + 0.0000001*10
incrementos = [0.1]*9 + [0.01]*9 + [0.001]*10 #+[0.0001]*10# [0.0001]*9 #+ [0.00001]*9 + [0.000001]*9+[0.0000001]*9 + [0.00000001]*10
# demanda=1000
# while True:#demanda > 0:

# demanda_total =0    
for i in incrementos:    
    se_asigno_demanda=False
    
    # demanda_total =0
    for key  in OD:
    
        origen=key[0]
        destino=key[1]
        demanda_actual=OD[key]
        demanda_objetivo=OD_target[key]
        # print (demanda_actual)
        # demanda_total.append(demanda_actual)
        # demanda_total+=demanda_actual
    
        
        if demanda_actual>0:
            #Ruta minima
            path=nx.dijkstra_path(G,origen,destino,weight=costo)
            
            #Para usar grafo grande usar astar_path
            
            
            #Incrementar flujo en ruta minima
            Nparadas = len(path)
            # demanda_total+=demanda_actual
        
            for i_parada in range(Nparadas-1):
                o=path[i_parada]
                d=path[i_parada+1]
                
                G.edges[o,d]["flujo"] += (i*demanda_objetivo)
                
            #print(f"{origen} - {destino}: demanda {demanda_actual} {path}")
            OD[key]-=(i*demanda_objetivo)
            se_asigno_demanda=True
        
   # if not se_asigno_demanda:
    #        break

for ni,nf in G.edges:
    arco=G.edges[ni,nf]
    funcosto_arco = arco["fcosto"]
    flujo_arco=arco["flujo"]
    arco["costo"]=funcosto_arco(flujo_arco)
 

#REDONDEAMOS PARA GRAFICAR       
for Key, value in G.edges.items():
        G.edges[Key]['flujo'] = round(G.edges[Key]['flujo'],3)
        G.edges[Key]['costo'] = round(G.edges[Key]['costo'],3)

plt.figure(1)
ax1=plt.subplot(111)
pos=nx.get_node_attributes(G,"pos")
nx.draw(G,pos,with_labels=True, font_weight="bold")
labels=nx.get_edge_attributes(G,"flujo")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("Flujos.png")
plt.show()


plt.figure(2)
plt.title(f"Andate por {path}")
ax1=plt.subplot(111)
pos=nx.get_node_attributes(G,"pos")
nx.draw(G,pos,with_labels=True, font_weight="bold")
labels=nx.get_edge_attributes(G,"costo")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("Costos_arcos.png")
plt.show()

# plt.title(f"Andate por {path}")
plt.figure(3)
ax1=plt.subplot(111)
pos=nx.get_node_attributes(G,"pos")
nx.draw(G,pos,with_labels=True, font_weight="bold")
labels=nx.get_edge_attributes(G, "fun")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("Funciones.png")
plt.show()

#print ("---------------------------------------------------------------------------------------------------------")
#print("|  ORIGEN-DESTINO  |  PATH SELECCIONADO                                    |    COSTO    |  ERROR COSTO   ")
#print ("---------------------------------------------------------------------------------------------------------")
#print ("---------------------------------------------------------------------------------------------------------")
