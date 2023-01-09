import random

Combate = False
Ratas = 1
Goblins = 2
Ogro = 3
Estafermo = 4
NoEnemies = 0
turno_player = False
turno_enemigo = False
def dados(n): #La función en resumen crea una lista según el número de caras del dado y de ahi hace un random.choice
    dado_juego = []
    dado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for x in range(0, n):

        dado_juego.append(dado[x])

    res_dado = random.choice(dado_juego)
    return res_dado

def victoria(inventario):
    print("\nEnhorabuena Jugador, ahora que has derrotado al ogro, seras bienvenido como todo un héroe en el pueblo")
    print("*Viaje de regreso al pueblo*")
    print("\nMira jugador todo el pueblo te ha recibido entre aplausos y coros de victoria.")
    print("*Celebracion por todo lo alto*")
    print("*Más tarde*")
    print("\nVaya ha estado bien la celebracion, no?")
    print("Que es eso?...")
    print("Parece que alguien ha metido en tu mochila una llave y un papel con un 5 escrito sobre el. ")    #El numero es susceptible a cambios
    inventario.update({"Llave": True})
    print("\nNo tengo idea, de donde sera pero por su aspecto parece de un ostentoso cofre.")
    print("Debes estar atento, si deseas encontrar ese misterioso cofre.")
    print("Pero de momento no es prioritario, así que lo puedes dejar para más tarde")
    #mapa() llamar de nuevo al mapa

#Funcion general de los Combates
def combate(inventario, stats_player, enemigo_selec): #Esta funcion comprueba que combate debe activar
    enemigo = enemigo_selec #Enemigo es una variable que toma el valor de enemigo_selec
    if enemigo == NoEnemies:
        print("No hay un combate disponible")
    elif enemigo_selec == 1: #Comprueba uno por uno el tipo de enemigo
        print("ratas es True")
        combate_ratas(inventario,stats_player)
    elif enemigo_selec == 2:
        print("goblins")
    elif enemigo_selec == 3:
        print("ogro")
        combate_ogro(inventario,stats_player)
    elif enemigo_selec == 4:
        print("estafermo") #una vez a encontrado ese enemigo, inicia su funcion de combate, en este caso el estafermo
        combate_estafermo(inventario,stats_player) #Este tomara las variables del inventario y las estadisticas

#Funciones especificas de cada combate
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
            dam_player = (stats_player.get("fuerza") - 10) + dados(4) # Calcula el daño del jugador en base al arma, que en este caso al ser el puño he puesto directamente en dados(4), pero deberia ser el valor del arma que lleve en ese momento
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
        print("\nEs tu turno Jugador")
        if golpe_player >= impacto_rata:
            turno_player = True
        else:
            print("Vaya no has impactado")
            turno_enemigo = True

        while turno_player == True:
            print("Has impactado")
            dam_player = (stats_player.get("fuerza") - 10) + dados(4) # Calcula el daño del jugador en base al arma, que en este caso al ser el puño he puesto directamente en dados(4), pero deberia ser el valor del arma que lleve en ese momento
            vida_rata = vida_rata - dam_player
            if vida_rata <= 0:
                print("La rata ha muerto")
                print(f"Has ganado {xp_rata} de experiencia")
                decision = int(input("\n Quieres intentar huir SI||NO (1/0): "))
                if decision == 1:
                    int_huida = dados(20)
                    if int_huida >= huida:
                        print("Muy bien Jugador has logrado huir")
                        Combate,turno_player = False, False  # Se cierra el turno y el combate al mismo tiempo para evitar problemas

                    else:
                        print(f"Vaya has sacado un {int_huida}, no has logrado huir te toca seguir luchando.")
                        print("Por ahí viene otra rata")
                        combate_ratas(inventario,stats_player)
                else:
                    print("Muy bien vas a continuar luchando.")
                    print("Por ahí viene otra rata")
                    combate_ratas(inventario, stats_player)
            else:
                print(f"La rata tiene {vida_rata} de vida toca seguir luchando.")
                turno_player, turno_enemigo = False, True  # Al igual que antes el turno del jugador se desactiva y el del enemigo se activa al mismo instante para evitar problemas con los bucles
        while turno_enemigo == True:
            print("\nEs el turno de la rata")
            impacto_player = 12 + (stats_player.get("destreza")-10) #Deberemos calcular cuanto debe sacar el enemigo para impactar al jugador, esto en base a la estadistica de destreza
            golpe_rata = dados(20)

            if golpe_rata >= impacto_player: #El enemigo golpea al jugador
                print("La rata ha impactado")
                vida_player = stats_player.get("vida") #Creamos una variable con el valor de vida que en ese momento tiene el jugador
                vida_player = vida_player - dam_rata #Actualizamos el valor de la vida del jugador
                stats_player.update({"vida":vida_player}) #Subimos, por asñi decirlo, el nuevo valor al diccionario del jugador
                print(f"La rata te ha hecho {dam_rata} punto de daño tienes, {vida_player} puntos de vida") #Imprimimos detalles del combate como el daño y nuestra vida
                turno_player,turno_enemigo = True,False #Se activan y desactivan los turnos homogeneamente
            else: #El estafermo no ha impactado
                print("La rata no ha impactado")
                turno_enemigo,turno_player = False,True
def combate_ogro(inventario,stats_player):
    Combate, turno_player, turno_enemigo = False,False, False
    vida_ogro = 50
    dam_ogro = dados(12) + 2
    impacto_ogro = 16
    golpe_ogro = 0
    Combate = True

    while Combate == True:
        golpe_player = dados(20)
        print("\nEs tu turno Jugador")

        if golpe_player >= impacto_ogro:
            turno_player = True

        else:
            print("Vaya no has conseguido impactar.")
            turno_enemigo = True

        while turno_player == True:
            print("Has impactado")
            dam_player = (stats_player.get("fuerza") - 10) + dados(4) # Calcula el daño del jugador en base al arma, que en este caso al ser el puño he puesto directamente en dados(4), pero deberia ser el valor del arma que lleve en ese momento
            vida_ogro = vida_ogro - dam_player

            if vida_ogro <= 0:
                print("Muy bien, Jugador has conseguido derrotar el temible Jefe Ogro. ")
                print("Has ganado 500 puntos de experiencia, además te has llevado su botín de 200 monedas.")

                inventario.update({"Experiencia": inventario.get('Experiencia') + 500})
                inventario.update({"Monedas": inventario.get('Monedas') + 200})

                print("Ya has terminado tu labor ahora regresaras al pueblo")
                Combate, turno_player = False, False


            else:
                print(f"Tu golpe ha hecho {dam_player} puntos de daño, el Ogro tiene {vida_ogro} puntos de vida")
                turno_player, turno_enemigo = False, True

        while turno_enemigo == True:
            print("\n Es el turno del Ogro.")
            impacto_player = 12 + (stats_player.get("destreza")-10) #Deberemos calcular cuanto debe sacar el enemigo para impactar al jugador, esto en base a la estadistica de destreza
            golpe_ogro = dados(20)

            if golpe_ogro >= impacto_player:
                print("El Ogro ha impactado.")
                vida_player = stats_player.get("vida") #Creamos una variable con el valor de vida que en ese momento tiene el jugador
                vida_player = vida_player - dam_ogro
                stats_player.update({"vida":vida_player}) #Subimos, por asñi decirlo, el nuevo valor al diccionario del jugador
                print(f"El Ogro te ha hecho {dam_ogro} punto de daño tienes, {vida_player} puntos de vida") #Imprimimos detalles del combate como el daño y nuestra vida
                turno_player, turno_enemigo = True,False

            else:
                print("El ogro no ha impactado")
                turno_enemigo, turno_player = False, True









