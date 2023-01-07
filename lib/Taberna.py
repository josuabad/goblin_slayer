# Variables globales de prueba Jugador (mochila y stats)


def taberna(inventario,stats_player):
    print("Muy bien Jugador has decidido entrar a la Taberna. Aquí podrás recuperar un poco de vida tomando Hidromiel")
    # print("Pero ten cuidado puede que te encuentres a algún guerrero que quiera combatir contra ti. ")
    Taberna = True

    while Taberna == True:
        try:
            print(f"\nActuamente tienes {mochila.get('Monedas')} Monedas")
            decision = int(input("¿Que vas ha hacer? \n1.) Tomar Hidromiel (3 Monedas)\n2.) Comprar Hidromiel del "
                                 "Viajero (5 Monedas)\n3.) Salir: "))

            if decision == 1:
                print("Muy bien vas a tomar una racion de Hidromiel")
                compra = int(input("Confirmar compra SI||No (1//0): "))
                dinero = mochila.get("Monedas")

                if compra == 1 and dinero >= 3:
                    stats_player.update({"vida":stats_player.get("vida") + 3})
                    mochila.update({"Monedas": mochila.get("Monedas") - 3})

                    if stats_player.get("vida") > ((stats_player.get("const")*2) + 20):
                        stats_player.update({"vida": (stats_player.get("const")*2) + 20})

                    elif stats_player.get("vida") == ((stats_player.get("const")*2) + 20):
                        print("No puedes tomar la Hidromiel ya que tienes la vida al máximo")
                        continue

                    print("Has tomado una racion de hidromiel")
                    print(f"Tu vida ahora es de {stats_player.get('vida')} puntos")
                    continue

                elif compra == 1 and dinero < 3:
                    print("No tienes suficiente dinero")
                    print(f"Actualmente tienes {mochila.get('Monedas')} monedas. Vuelve más tarde")
                    continue

                elif compra == 0:
                    print("Vale, has cancelado la compra, vas a volver al menú de la Taberna")
                    continue

            elif decision == 2:
                print("Muy bien la Hidromiel que vas a comprar se puede tomar en cualquier momento. Esta bebida te "
                      "otorga una restaruacion de 3 puntos de vida al tomartela")
                compra = int(input("Confirmar compra SI||No (1//0): "))
                if compra == 1:
                    if mochila.get("Monedas") >= 5:
                        mochila.update({"Monedas": mochila.get("Monedas") - 5})
                        mochila.update({"Hidromiel": mochila.get("Hidromiel") + 1})
                        print("Muy bien has comprando hidromiel.")
                        print(f"Actualmente tienes {mochila.get('Hidromiel')} frascos de Hidromiel")
                        continue
                    else:
                        print("Vaya parece que no tienes suficientes monedas, vuelve cuando tengas el minimo")
                        continue
            elif decision == 3:
                print("Has decidido salir de la Taberna. Puedes regresar aqui cuando quieras")
                Taberna = False
            else:
                raise ValueError
        except ValueError:
           print("Eso es un valor erroneo intentalo de nuevo")


inventario = 0
stats_player = {"vida": 13,"const":1,"destreza":11,"fuerza":11,}
mochila = {"arma":{"puño":0},"Monedas":4,"Hidromiel": 0}

print(taberna(inventario, stats_player))