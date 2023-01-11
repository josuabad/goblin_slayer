def taberna(inventario, stats_player):
    print("Muy bien Jugador has decidido entrar a la Taberna. Aquí podrás recuperar un poco de vida tomando Hidromiel")
    Taberna = True
    while Taberna:
        try:
            print(f"\nActuamente tienes {inventario.get('Monedas')} Monedas")
            decision = int(input("""
¿Que vas ha hacer?
1.) Tomar Hidromiel (3 Monedas)
2.) Salir
: """))
            if decision == 1:
                print("Muy bien vas a tomar una racion de Hidromiel")
                compra = int(input("Confirmar compra SI||No (1//0): "))
                dinero = inventario.get("Monedas")

                if compra == 1 and dinero >= 3:
                    stats_player.update({"vida": stats_player.get("vida") + 3})
                    inventario.update({"Monedas": inventario.get("Monedas") - 3})

                    if stats_player.get("vida") > ((stats_player.get("const") * 2) + 20):
                        stats_player.update({"vida": (stats_player.get("const") * 2) + 20})

                    elif stats_player.get("vida") == ((stats_player.get("const") * 2) + 20):
                        print("No puedes tomar la Hidromiel ya que tienes la vida al máximo")
                        continue

                    print("Has tomado una racion de hidromiel")
                    print(f"Tu vida ahora es de {stats_player.get('vida')} puntos")
                    continue

                elif compra == 1 and dinero < 3:
                    print("No tienes suficiente dinero")
                    print(f"Actualmente tienes {inventario.get('Monedas')} monedas. Vuelve más tarde")
                    continue

                elif compra == 0:
                    print("Vale, has cancelado la compra, vas a volver al menú de la Taberna")
                    continue

            elif decision == 2:
                print("Has decidido salir de la Taberna. Puedes regresar aqui cuando quieras")
                Taberna = False
            else:
                raise ValueError
        except ValueError:
            print("Eso es un valor erroneo intentalo de nuevo.")
    return inventario, stats_player
