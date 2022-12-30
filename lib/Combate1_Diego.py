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


def combate_estafermo(inventario,player_stats):
    vida_estafermo = 50000
    dam_estafermo = 0
    impacto_estafermo = 0 #Lo que debe sacar para impactar al enemigo
    golpe_estafermo = 0 #Lo que debe sacar el estafermo para impactar al jugador
    Combate = True
    while Combate == True:
        golpe_player = dados(20)
        print("Es tu turno Jugador")
        if golpe_player >= impacto_estafermo:
            turno_player = True
        else:
            print("No has impactado")
            turno_enemigo = True


        while turno_player == True:
            print("Has impactado")
            dam_player = (stats_player.get("destreza") - 10) + dados(4)
            vida_estafermo = vida_estafermo-dam_player
            if vida_estafermo <= 0:
                print("El estafermo ha quedado destruido,has terminado el entrenamiento.")
                Combate,turno_player = False,False
                break
            print(f"El Estafermo tiene {vida_estafermo} de vida.")
            decision = input("¿Quieres seguir luchando?  SI||NO: ")
            decision = decision.upper()
            if decision == "NO":
                print("Bien, has decidido huir has terminado tu sesion de entrenamiento")
                Combate = False
                break
            else:
                pass
            turno_player,turno_enemigo = False,True

        while turno_enemigo == True:
            print("\nEs el turno del Estafermo")
            impacto_player = 12 + (stats_player.get("destreza")-10)
            golpe_estafermo = dados(20)

            if golpe_estafermo >= impacto_player:
                print("El estafermo ha impactado")
                vida_player = stats_player.get("vida")
                vida_player = vida_player - dam_estafermo
                stats_player.update({"vida":vida_player})
                print(f"El Estafermo te ha hecho {dam_estafermo} punto de daño tienes, {vida_player} puntos de vida")
                turno_player,turno_enemigo = True,False
            else:
                print("El Estafermo no ha impactado")
                turno_enemigo,turno_player = False,True


def combate(inventario, stats_player, enemigo_selec):
    enemigo = enemigo_selec
    if enemigo == (Ratas == True):
        print("ratas es True")
    elif enemigo == (Goblins == True):
        print("goblins")
    elif enemigo == (Ogro == True):
        print("ogro")
    elif enemigo == (Estafermo == True):
        print("estaferno")
        combate_estafermo(inventario,stats_player)

Estafermo = False

combate(mochila,stats_player,Estafermo)











