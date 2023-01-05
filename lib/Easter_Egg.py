from funcionesjueguito import *

easterEgg = True

stats_player = {"vida": 13,"const":1,"destreza":11,"fuerza":11,}
mochila = {"arma":{"puño":0},"Monedas":4,"Hidromiel": 0}

def EasterEgg(inventario,stats_player,variable): #Se introduce la variable booleana de EasterEgg para que solo se pueda hacer una vez
    print("Vaya parece que explorando has encontrado un camino secreto")
    while variable == True:
        decision = int(input("Quieres continuar por este camino SI||NO  (1/0): "))
        if decision == 1:
            print("Vale, has decidido continuar por el camino secreto")

        elif decision == 0:
            print("De acuerdo, mas tarde podras volver por aqui, que no se te olvide")
        else:
            print("No es una opcion valida, intentalo de nuevo")
            continue
    else:
        print("Vaya parece que el camino esta bloqueado")


EasterEgg(mochila,stats_player,easterEgg)

