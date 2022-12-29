#Librerias de otros ficheros/archivos
from funcionesjueguito import *
#Variables globales de prueba Jugador (mochila y stats)
stats_player = {"vida":22,"destreza":11,"fuerza":11}
mochila = {"arma":{"puño":0}}

#Variables Globales de los enemigos
Combate = False
Ratas = False
Goblins = False
Ogro = False
Estafermo = False
turno_player = False
turno_enemigo = False
"""
Explicacion:
Por cada tipo de enemigo se crea una variable Booleana, al principio cada una de esas variables esta en False
osea no se activa nada.
Cuando la situacion lo requiera se elige el enemigo y la variable se cambia a True. Para posteriormente
llamar a la funcion combate(inv,stats,enemigo) donde en enemigo se introduce el enemigo con la variable en True

Ahí dentro de la funcion principal se comprueba que enemigo es al que nos enfrentamos, entonces una vez
comprobado la funcion combate llamara a otra (ej: combate_ratas, combate_goblins, etc.) donde se encontrara el
combate y la logica para cada uno de los enemigos en este primer caso solo lo he probado con el estafermo

Esta el la primera Version de la plantilla para los combates, faltaria que les dieran ustedes el visto bueno,
para empezar a implementar la logica a los otros enemigos, y ajustar unos pequeños detalles
"""

def combate_estafermo(inventario,player_stats):
    vida_estafermo = 50000 #Las variables por comodidad las he puesto así, pero se pondrian igual en un diccionario
    dam_estafermo = 0
    impacto_estafermo = 0 #Lo que debe sacar para impactar al enemigo
    golpe_estafermo = 0 #Lo que debe sacar el estafermo para impactar al jugador
    Combate = True #La variableCombate indica que una vez se hayan creado las variables que afectan al enemigo comienza
    while Combate == True:
        golpe_player = dados(20)
        print("Es tu turno Jugador")
        if golpe_player >= impacto_estafermo: #COmprueba si el jugador golpea al enemigo
            turno_player = True #Se activca el turno del jugador
        else:
            print("No has impactado") #El caso contrario, donde no impacta desde un principio
            turno_enemigo = True #Comienza el turno del enemigo


        while turno_player == True: #Bucle que representa el turno del jugador
            print("Has impactado")
            dam_player = (stats_player.get("destreza") - 10) + dados(4) # Calcula el daño del jugador en base al arma, que en este caso al ser el puño he puesto directamente en dados(4), pero deberia ser el valor del arma que lleve en ese momento
            vida_estafermo = vida_estafermo-dam_player #Se actualiza la vida del enemigo
            if vida_estafermo <= 0: #Si la vida esta por debajo de 0 se termina el combate
                print("El estafermo ha quedado destruido,has terminado el entrenamiento.")
                Combate,turno_player = False,False #Se cierra el turno y el combate al mismo tiempo para evitar problemas
                break
            print(f"El Estafermo tiene {vida_estafermo} de vida.")
            decision = input("¿Quieres seguir luchando?  SI||NO: ") #Pregunta al jugador despues de cada golpe si quiere seguir jugando
            decision = decision.upper()
            if decision == "NO":
                print("Bien, has decidido huir has terminado tu sesion de entrenamiento")
                Combate = False
                break
            else:
                pass
            turno_player,turno_enemigo = False,True #Al igual que antes el turno del jugador se desactiva y el del enemigo se activa al mismo instante para evitar problemas con los bucles

        while turno_enemigo == True:
            print("\nEs el turno del Estafermo")
            impacto_player = 12 + (stats_player.get("destreza")-10) #Deberemos calcular cuanto debe sacar el enemigo para impactar al jugador, esto en base a la estadistica de destreza
            golpe_estafermo = dados(20) #El enemigo tira un dado 20

            if golpe_estafermo >= impacto_player: #El enemigo golpea al jugador
                print("El estafermo ha impactado")
                vida_player = stats_player.get("vida") #Creamos una variable con el valor de vida que en ese momento tiene el jugador
                vida_player = vida_player - dam_estafermo #Actualizamos el valor de la vida del jugador
                stats_player.update({"vida":vida_player}) #Subimos, por asñi decirlo, el nuevo valor al diccionario del jugador
                print(f"El Estafermo te ha hecho {dam_estafermo} punto de daño tienes, {vida_player} puntos de vida") #Imprimimos detalles del combate como el daño y nuestra vida
                turno_player,turno_enemigo = True,False #Se activan y desactivan los turnos homogeneamente
            else: #El estafermo no ha impactado
                print("El Estafermo no ha impactado")
                turno_enemigo,turno_player = False,True


def combate(inventario, stats_player, enemigo_selec): #Esta funcion comprueba que combate debe activar
    enemigo = enemigo_selec #Enemigo es una variable que toma el valor de enemigo_selec
    if enemigo == (Ratas == True): #COmprueba uno por uno el tipo de enemigo
        print("ratas es True")
    elif enemigo == (Goblins == True):
        print("goblins")
    elif enemigo == (Ogro == True):
        print("ogro")
    elif enemigo == (Estafermo == True):
        print("estafermo") #una vez a encontrado ese enemigo, inicia su funcion de combate, en este caso el estafermo
        combate_estafermo(inventario,stats_player) #Este tomara las variables del inventario y las estadisticas
    else:
        print("No hay un combate disponible")

Estafermo = True #Para esta prueba pongo instantanemante antes que estafermo = True para iniciar su combate en concreto

combate(mochila,stats_player,Estafermo) #Llamamos a la funcion del combate











