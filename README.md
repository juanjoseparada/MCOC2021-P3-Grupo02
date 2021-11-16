# MCOC2021-P3-Grupo02

Integrantes:
Juan José Parada Pinilla
José Tomás Weirauch




.                                                            ENTREGA 2
                                                                 

ENTREGA 2
-----------------------------------------------------

Para este trabajo se analiso la siguiente red de flujo con el fin de lograr obtener 
las rutas optimas segun el tiempo minimo de recorrido


                                                                 
.                        ![fig1](https://user-images.githubusercontent.com/88350743/141019547-a7c0e56e-ebe8-4402-9a39-e2755e69b7af.png)

.                                  Figura 1: Mapa de Principal
                                             

Segun los distintos arcos nodos y los arcos que los unen respectivamente, se muestran
a continuacion las rutas mas omptimas para los viajes (O=0, D=9), (O=4, D=5) y (O=0, D=4)    

.                         ![fig2](https://user-images.githubusercontent.com/88350743/141019549-62bfc4e9-74f6-4eef-b4fe-dafe4ce413b7.png)

.                                  Figura 2: Mapa para camino optimo de 0 a 9.


                                            
                                            
.                         ![fig3](https://user-images.githubusercontent.com/88350743/141019550-71c62ae0-3f76-4c87-925c-bb911462552a.png)

.                                  Figura 3: Mapa para camino optimo de 4 a 5.
                                            
                                            
.                         ![fig4](https://user-images.githubusercontent.com/88350743/141019551-7a65e826-0ebf-4120-ac6c-8384c463603b.png)
   
.                                  Figura 4: Mapa para camino optimo de 0 a 4.



.                                                     ENTREGA 3

Imagen Juan José Parada:


![Figure_1](https://user-images.githubusercontent.com/88350743/141524621-c9bd59ca-7948-4ae5-b9b3-5b6f77fd5940.png)


                            Figura 1: JUAN JOSÉ PARADA


Imagen José Tomás Weihrauch Varela:

![Captura de pantalla 2021-11-12 a la(s) 22 13 50](https://user-images.githubusercontent.com/88339852/141600194-1800d54d-a3a3-4b38-8a82-303f217cae7f.png)

                            Figura 2: JOSÉ TOMÁS WEIHRAUCH VARELA
                            
.                                                     ENTREGA 4

Se obtuvieron 3 tipos de funciones distintas las cuales fueron asignadas a 9 tramos distintos. Donde gracias a la ayuda de la clase se pudo obtener el codigo para poder establecer el equilibrio de Wardrop para diferentes rutas, las cuales podían tomar varios tramos con sus diferentes combinaciones.



"""
    
    incrementos = [0.1]*9 + [0.01]*9 + [0.001]*10 

    for i in incrementos:    
        se_asigno_demanda=False
    
    for key  in OD:
    
        origen=key[0]
        destino=key[1]
        demanda_actual=OD[key]
        demanda_objetivo=OD_target[key]
        
        if demanda_actual>0:
       
            path=nx.dijkstra_path(G,origen,destino,weight=costo)
            
            Nparadas = len(path)
          
            for i_parada in range(Nparadas-1):
                o=path[i_parada]
                d=path[i_parada+1]
                
                G.edges[o,d]["flujo"] += (i*demanda_objetivo)
                
            
            OD[key]-=(i*demanda_objetivo)
            se_asigno_demanda=True              
"""

En el codigo anterior se ingresa un incremento, el cual fue multiplicado a las demandas para así trabajar de una manera mas precisa, donde despues buscando en la matriz origen destino (OD) donde dentro ya de OD se busca Key[0] (ORIGEN) y Key[1] (DESTINO). Y ya con los nodos y posibles caminos se pudieron obtener las mejores rutas gracias a """path=nx.dijkstra_path(G,origen,destino,weight=costo)""".

"""

    for ni,nf in G.edges:
        arco=G.edges[ni,nf]
        funcosto_arco = arco["fcosto"]
        flujo_arco=arco["flujo"]
        arco["costo"]=funcosto_arco(flujo_arco)
        
"""

Tambien se buscaron los flujos y costos por arcos, mediante estas funciones, las cuales se puede ver en las imagenes siguientes:

![Costos_arcos](https://user-images.githubusercontent.com/88350743/142061055-63ca99a4-c8bc-41ab-a649-a9d0ec134bbd.png)

                             Figura 4.2: Grafo de Costo por arco

![Funciones](https://user-images.githubusercontent.com/88350743/142061093-4399f4ee-405e-4fab-8a51-1db0789eb3ba.png)

                              Figura 4.1: Grafo de funciones

![Flujos](https://user-images.githubusercontent.com/88350743/142061070-a8e6cb87-39b0-4b2a-aebd-962d5a847bf3.png)

                             Figura 4.2: Grafo de Flujo por arco
                             
Despues se verifico el equilibrio y se puede notar en la siguiente imagen estas comparaciones, donde se notan en amarillo las rutas que fueron elegidas ya que las que no estan marcadas tienen un costo mucho mayor a las otras.

![WhatsApp Image 2021-11-16 at 17 22 12 (2)](https://user-images.githubusercontent.com/88350743/142065008-df5e903e-c78f-4758-92ba-f7df7c41162c.jpeg)
                                                      
                                       
![WhatsApp Image 2021-11-16 at 17 57 51](https://user-images.githubusercontent.com/88350743/142065012-b68f9044-9a59-43cf-af1a-fe26c80dbde4.jpeg)

