import random

def dados(n): #La función en resumen crea una lista según el número de caras del dado y de ahi hace un random.choice
    dado_juego = []
    dado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for x in range(0, n):

        dado_juego.append(dado[x])

    res_dado = random.choice(dado_juego)
    return res_dado

def combate_estafermo(inventario,stats_player):
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




"""
try:
    eleccion_huida = input(" SI|NO : ")
    eleccion_huida = eleccion_huida.upper()

except ValueError:
    print("Has introducido un valor erroneo. Intentalo de nuevo") #Arreglar introduccion dato de eleccion

if eleccion_huida == "SI" or "1":
    print("Muy bien has decidido huir, vamos a probar suerte.")
    huida = dados(10)
    if huida > 6:
        print(f"Has sacado un {huida}.")
        print("Muy bien has logrado huir ")
    else:
        print(f"Has sacado un {huida}.")
        print("ooohh..... no, no has logrado huir te va a tocar luchar")
"""









