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

                             Figura 4.1: Grafo de Costo por arco

![Funciones](https://user-images.githubusercontent.com/88350743/142061093-4399f4ee-405e-4fab-8a51-1db0789eb3ba.png)

                              Figura 4.2: Grafo de funciones
                              
                              
                             

![Flujos](https://user-images.githubusercontent.com/88350743/142061070-a8e6cb87-39b0-4b2a-aebd-962d5a847bf3.png)

                             Figura 4.3: Grafo de Flujo por arco
                             
En esta imagen se pueden apreciar los porcentajes de error para los flujos y costos por cada arco.

![WhatsApp Image 2021-11-16 at 17 22 12 (2)](https://user-images.githubusercontent.com/88350743/142065008-df5e903e-c78f-4758-92ba-f7df7c41162c.jpeg)
                                                      
                               Figura 4.4 Costos y flujos por arcos
                               
Para la validacion de los resultados se utilizo excel, herramienta que nos permitio llevar a cabo el trabajo de una manera clara, comoda y ordenada.        
En la primera figura se puede observar el costo total por ruta para cada uno de los OD dados por la matriz OD, en donde se discriminaron los costos menores para cada una de estas y se calculan sus respectivos porcentajes de error.                               
                                       
![WhatsApp Image 2021-11-16 at 17 57 51](https://user-images.githubusercontent.com/88350743/142065012-b68f9044-9a59-43cf-af1a-fe26c80dbde4.jpeg)

                              Figura 4.4 Variacion Costos totales por ruta


   .                                                      Entrega 5
   
   
¿Cómo seleccionó las zonas a incluir?

Las zonas a incluir se seleccionaron mediante la siguiente parte del código:

        wou =[]
        i=0
        zona_all=[]
        for i in id_zonas_a_graficar:
            zona_all.append(i)

        for wa in open('mod.csv'):
            sl = wa.split(',')
            o = int(sl[0])
            d = int(sl[1])
            dda = np.double(sl[2])
            # print (o)
            if o in id_zonas_a_graficar or d in id_zonas_a_graficar and dda > 100:
                zona_all.append(o)
                zona_all.append(d)

Donde dentro del archivo Excel que contenía los origenes y destinos con sus demandas respectivas se buscó las que ocupaban AVO y tuvieran una demanda mayor a 100.



¿Cuántas zonas quedaron seleccionadas son?

[599, 153, 146, 683, 666, 677, 682, 306, 307, 287, 288, 289, 290, 291, 304, 266, 267, 434, 435, 281, 426, 283, 440, 278, 439, 471, 684, 79, 112, 143, 150, 581, 297, 497, 537, 314, 500, 160, 0, 163, 220, 201, 193, 232, 206, 200, 292, 235, 490, 498, 18, 496, 369, 279, 274, 374, 167, 509, 478, 286, 516, 512, 277, 284, 425, 265, 476, 442, 511, 218, 485, 46, 491, 508, 445, 303, 20, 268, 280, 47, 300, 1, 312, 295, 276, 668, 506, 548, 505, 305, 302, 667, 49, 330, 732, 12, 675, 513, 299, 319, 296, 293, 298, 495, 294, 23, 739, 320, 448, 504, 13, 614, 627, 325, 148, 313, 514, 309, 327, 301, 673, 671, 672, 547, 308, 328, 332, 333, 331, 681, 680, 370, 364, 371, 386, 388, 407, 578, 433, 438, 424, 443, 36, 773, 430, 431, 760, 444, 642, 502, 510, 696, 725, 685, 695, 724, 543, 577, 580, 763, 2, 310, 670, 315]

Que suman un total de 164 zonas.



¿Cuántos viajes deberá asignar?





¿Cuales son los pares OD que espera Ud. que generen mayor flujo en AVO?

Los pares OD que se esperan que tengan mayor flujo en AVO son los que quedan aledaños a este mismo tramo, ya que los viajes entre estas zonas utilizarían casi siempre este tramo de AVO. Esto se pudo comprobar mediante el siguiente código, el cual busca los pares con un flujo mayor de lo normal y que ocupe el tramo de AVO.

    if o in id_zonas_a_graficar or d in id_zonas_a_graficar:
            if dda > 1500:
                zona_alto_flujo.append(wa)
                zona_alto_flujo.append(o)
                zona_alto_flujo.append(d)
                i+=dda
                # print(f(" Origen {o}" Destino))
                print (f" PAR OD [{o}, {d}]  con demanda {dda}")
            else:
                continue


Con lo cual estos serían los pares OD con mayor flujo:

![WhatsApp Image 2021-11-19 at 19 08 13](https://user-images.githubusercontent.com/88350743/142697926-2574b739-3a57-4b59-a2fa-0800bc9ffd33.jpeg)




