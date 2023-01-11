def EasterEgg(bolsillo,stats_player): #Se introduce la variable booleana de EasterEgg para que solo se pueda hacer una vez
    print("Vaya parece que explorando has encontrado un camino secreto")
    while bolsillo['Llave'] == True:
        decision = int(input("Quieres continuar por este camino SI||NO  (1/0): "))

        if decision == 1:
            print("Vale, has decidido continuar por el camino secreto")
            print("Continuas avanzando...")
            print("Vaya parece que has encontrado un cofre misterioso, parece que se requiere de una llave para poder acceder a él")

            if bolsillo.get("Llave") == True:
                print("Al parecer tienes en tu inventario una llave misteriosa, deseas usarla")
                decision = int(input("SI||NO (1/0): "))

                if decision == 1:
                    print("Vale has decidido usar la llave")
                    bolsillo.update({"Llave": False})
                    print("Vaya sorpresa, en el cofre se encontraban 100 monedas y parece que has ganado 100 de experiencia")
                    bolsillo['monedas'] = bolsillo['monedas'] + 100
                    stats_player['experiencia'] = stats_player['experiencia'] + 100
                    print("Cuidado Jugador parece que la Tierra ha empezado a temblar.")
                    print("Tienes que huir, y volver por donde has venido.")
                    print("*Vuelves corriendo por donde has venido, mientras todo se derrumba*")
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
    return bolsillo, stats_player

