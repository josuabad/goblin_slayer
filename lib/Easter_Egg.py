from funcionesjueguito import *

easterEgg = True

stats_player = {"vida": 13,"const":1,"destreza":11,"fuerza":11,}
mochila = {"arma":{"puño":0},"Monedas":4,"Hidromiel": 0,"Llave":True}

def EasterEgg(inventario,stats_player,variable): #Se introduce la variable booleana de EasterEgg para que solo se pueda hacer una vez
    print("Vaya parece que explorando has encontrado un camino secreto")
    while variable == True:
        decision = int(input("Quieres continuar por este camino SI||NO  (1/0): "))

        if decision == 1:
            print("Vale, has decidido continuar por el camino secreto")
            print("Continuas avanzando...")
            print("Vaya parece que has encontrado un cofre misterioso, parece que se requiere de una llave para poder acceder a él")

            if mochila.get("Llave") == True:
                print("Al parecer tienes en tu inventario una llave misteriosa, deseas usarla")
                decision = int(input("SI||NO (1/0): "))

                if decision == 1:
                    print("Vale has decidido usar la llave")
                    mochila.update({"Llave": False})
                    print("Vaya sorpresa, en el cofre se encontraban 100 monedas y una Espada Igneá")
                    mochila.update({"arma":mochila.get("arma") | {"Espada ignea":5}}), mochila.update({"Monedas": mochila.get("Monedas") + 100}) #Esta solucion es de genio ;), el operador '|' fusiona 2 diccionario
                    print("Cuidado Jugador parece que la Tierra ha empezado a temblar.")
                    print("Tienes que huir, y volver por donde has venido.")
                    print("*Vuelves corriendo por donde has venido, mientras todo se derrumba*")
                    easterEgg == False
                    print("Has conseguido huir pero parece que ya no podras volver por aquí.")
                    break

                elif decision == 0:
                    print("Muy bien puedes volver cuando quieras.")
                    print("*Vuelves por donde has venido*")
                    break

                else:
                    print("Parece que el dato introducido es erroneo, intentalo de nuevo.")
                    continue

            else:
                print("Al parecer todavia no tienes este objeto en tu inventario, intenta avanzar en tu aventarura, y volver más tarde")
                print("*Vuelves por donde has venido*")
                break

        elif decision == 0:
            print("De acuerdo, mas tarde podras volver por aqui, que no se te olvide Jugador.")
            break
        else:
            print("No es una opcion valida, intentalo de nuevo")
            continue
    else:
        print("Vaya parece que el camino esta bloqueado")


localizacion = int(input("A donde quieres ir 1) Cueva  2) Pueblo 3) Cuevas 4) Ogro.  Elige: "))

if localizacion == 5:
    print("Eyy... eso no esta en el mapa")
    EasterEgg(mochila,stats_player,easterEgg)
else:
    print("Vale vas a ir a esa ubicacion.")


"""a = mochila.get("arma")
print(a)
print(mochila)
mochila.update({"arma":mochila.get("arma") | {"Espada ignea":5}}) #Esta solucion es de GENIO ;), el operador '|' fusiona 2 diccionario 

print(mochila)
"""