from funcionesjueguito import *

stats_player = {"vida": 22,"const":1,"destreza":11,"fuerza":11,}
mochila = {"Armas": {"puño": 0, "espada": 3, "Escudo": 4, "Espada_Magica": 1}, "objetos":{"Pociones":3, "Hidromiel": 0,  }, "Experiencia" : 12, "Monedas": 4, "Llave": False}

cueva_final = True
def cueva_ogro(inventario,stats_player):
    print("Has llegado a la cueva del ogro Jugador.")
    print("A partir de aquí no hay marcha atrás, asegurate de estar bien equipado.")
    while cueva_final == True:
        decision = int(input("Deseas entrar  1) SI   2) NO  Elige: "))

        if decision == 1:
            print("Muy bien, vas a comenzar el combate contra el Jefe Ogro")
            combate(inventario,stats_player,3)
            break
        elif decision == 2:
            print("Muy bien, vuelve cuando quieras, o cuando estes preparado.")

        else:
            print("Eso no es un dato válido intentalo de nuevo. ")
            continue

    victoria(inventario)


cueva_ogro(mochila,stats_player)





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


""""
IMPORTANTISIMO EN TODOS LOS COMBATES PONER EL CASO DE CUANDO EL JUGADOR MUERE
"""