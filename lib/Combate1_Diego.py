#Librerias de otros ficheros/archivos
from funcionesjueguito import *
#Variables globales de prueba Jugador (mochila y stats)
stats_player = {"vida":22,"destreza":11,"fuerza":11}
mochila = {"arma":{"puño":0}}

#Variables Globales de los enemigos
Combate = False
Ratas = 1
Goblins = 2
Ogro = 3
Estafermo = 4
NoEnemies = 0
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



def combate(inventario, stats_player, enemigo_selec): #Esta funcion comprueba que combate debe activar
    enemigo = enemigo_selec #Enemigo es una variable que toma el valor de enemigo_selec
    if enemigo == NoEnemies:
        print("No hay un combate disponible")
    elif enemigo_selec == 1: #COmprueba uno por uno el tipo de enemigo
        print("ratas es True")
    elif enemigo_selec == 2:
        print("goblins")
    elif enemigo_selec == 3:
        print("ogro")
    elif enemigo_selec == 4:
        print("estafermo") #una vez a encontrado ese enemigo, inicia su funcion de combate, en este caso el estafermo
        combate_estafermo(inventario,stats_player) #Este tomará las variables del inventario y las estadisticas


 #Para esta prueba pongo instantanemante antes que estafermo = True para iniciar su combate en concreto

combate(mochila,stats_player,4) #Llamamos a la funcion del combate
                            

def combate_ratas(inventario,stats_player):
    Combate, turno_player = False, False  # Se cierra el turno y el combate al mismo tiempo para evitar problemas
    huida = 8
    vida_rata = dados(4)
    dam_rata = dados(4)
    impacto_rata = 10 #Lo que debe sacar para impactar al enemigo
    golpe_rata = 0 #Lo que debe sacar para impactar al jugador
    xp_rata = 10
    Combate = True
    while Combate == True:
        golpe_player = dados(20)
        print("Es tu turno Jugador")
        if golpe_player >= impacto_rata:
            turno_player = True
        else:
            turno_enemigo = True

        while turno_player == True:
            print("Has impactado")
            dam_player = (stats_player.get("destreza") - 10) + dados(4) # Calcula el daño del jugador en base al arma, que en este caso al ser el puño he puesto directamente en dados(4), pero deberia ser el valor del arma que lleve en ese momento
            vida_rata = vida_rata - dam_player
            if vida_rata <= 0:
                print("La rata ha muerto")
                print(f"Has ganado {xp_rata} de experiencia")
                decision = int(input("\n Quieres intentar huir SI||NO (1/0)"))
                if decision == 1:
                    int_huida = dados(20)
                    if int_huida >= huida:
                        print("Muy bien Jugador has logrado huir")
                        Combate, turno_player = False, False  # Se cierra el turno y el combate al mismo tiempo para evitar problemas

                    else:
                        print(f"Vaya has sacado un {int_huida}, no has logrado huir te toca seguir luchando.")
                        print("Por ahí viene otra rata")
                        combate_ratas(inventario,stats_player)
                else:
                    print("Muy bien vas a continuar luchando.")
            else:
                print(f"La rata tiene {vida_rata} de vida toca seguir luchando.")
                turno_player, turno_enemigo = False, True  # Al igual que antes el turno del jugador se desactiva y el del enemigo se activa al mismo instante para evitar problemas con los bucles
        while turno_enemigo == True:
            print("\nEs el turno de la rata")
            impacto_player = 12 + (stats_player.get("destreza")-10) #Deberemos calcular cuanto debe sacar el enemigo para impactar al jugador, esto en base a la estadistica de destreza
            golpe_rata = dados(20)

            if golpe_rata >= impacto_player: #El enemigo golpea al jugador
                print("El estafermo ha impactado")
                vida_player = stats_player.get("vida") #Creamos una variable con el valor de vida que en ese momento tiene el jugador
                vida_player = vida_player - dam_rata #Actualizamos el valor de la vida del jugador
                stats_player.update({"vida":vida_player}) #Subimos, por asñi decirlo, el nuevo valor al diccionario del jugador
                print(f"El Estafermo te ha hecho {dam_rata} punto de daño tienes, {vida_player} puntos de vida") #Imprimimos detalles del combate como el daño y nuestra vida
                turno_player,turno_enemigo = True,False #Se activan y desactivan los turnos homogeneamente
            else: #El estafermo no ha impactado
                print("El Estafermo no ha impactado")
                turno_enemigo,turno_player = False,True








