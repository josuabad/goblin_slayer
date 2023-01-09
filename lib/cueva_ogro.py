from funcionesjueguito import *

stats_player = {"vida": 22,"const":1,"destreza":11,"fuerza":11,}
mochila = {"Armas": {"puño": 0, "espada": 3, "Escudo": 4, "Espada_Magica": 1}, "objetos":{"Pociones":3, "Hidromiel": 0, "Monedas": 4, "Llave": True, } , "Experiencia" : 12}

cueva_final = True
def cueva_ogro(inventario,stats_player):
    print("Has llegado a la cueva del ogro Jugador.")
    print("A partir de aquí no hay marcha atrás, asegurate de estar bien equipado.")
    while cueva_final == True:
        decision = int(input("Deseas entrar  1) SI   2) NO  Elige: "))

        if decision == 1:
            print("Muy bien, vas a comenzar el combate contra el Jefe Ogro")
            combate(inventario,stats_player,3)

        elif decision == 2:
            print("Muy bien, vuelve cuando quieras, o cuando estes preparado.")

        else:
            print("Eso no es un dato válido intentalo de nuevo. ")
            continue


cueva_ogro(mochila,stats_player)

""""
IMPORTANTISIMO EN TODOS LOS COMBATES PONER EL CASO DE CUANDO EL JUGADOR MUERE
"""