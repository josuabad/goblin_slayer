from lib.articulos import *
import time


def cueva_jugador(inventario, bolsillo, stats_player, armario):
    print("Muy bien jugador has llegado a tu cueva, aquí podrás descansar y guardar los objetos que más te interesen.")
    dormir = 0
    cueva = True
    armario_est = False
    cama = False
    while cueva == True:
        decision = int(input("Que deseas hacer. 1) Descansar  2) Guardar Objetos   3) Salir.  Elige: "))
        if decision == 1:
            print(
                "Has decidido Descansar, esta funcion te permite recuperar 1 punto de vida por cada 10 segundos que duermas, acumulando hasta 4 puntos de vida o hasta que se te llene la vida.")
            time.sleep(1)
            cama = True

            while cama == True:

                if dormir == 4:
                    print(
                        "Vaya parece que no puedes seguir durmiendo, has dormido bastante por ahora, volveras al menú.")
                    time.sleep(1)
                    cama = False

                elif stats_player.get("vida") >= ((stats_player.get("const")) * 2 + 20):
                    print("Parece que tiene la vida al máximo ahora no puedes dormir, volveras al menu.")
                    time.sleep(1)
                    cama = False

                else:

                    while dormir <= 4:
                        print("durmiendo.")
                        time.sleep(1)
                        print("durmiendo..")
                        time.sleep(2)
                        print("durmiendo...")
                        time.sleep(3)
                        print("durmiendo....")
                        time.sleep(4)

                        dormir += 1
                        stats_player.update({"vida": stats_player.get("vida") + 1})
                        break
                    print(f"Tu vida actual es de {stats_player.get('vida')} puntos.")
                    decision_1 = int(input("Deseas seguir durmiendo o salir.  1) Dormir  2) Salir  Elige: "))

                    if decision_1 == 1:
                        print("vas a seguir durmiendo")
                        continue

                    elif decision_1 == 2:
                        print("Vas a dejar de dormir.")
                        cama = False

        elif decision == 2:
            guardar_objetos = True

            while guardar_objetos:
                eleccion_inventario = int(
                    input("De que donde quieres guardar objetos 1) Mochila  2) Bolsillo  Elige: "))

                if eleccion_inventario == 1:
                    print("\nEstos son tus objetos:")
                    contador = 1
                    for objetos in inventario:
                        print(f"{contador})", objetos)
                        contador += 1

                    try:
                        eleccion = input("\nQue objeto deseas guardar: ")
                        print(inventario[eleccion]['cantidad'])

                    except KeyError:
                        print("El objeto introducido no se encuentra en la mochila, introduce otro")
                        continue
                    while guardar_objetos:
                        try:
                            # Revisar Hacha dos manos ya que salta un error
                            cantidad = int(input(f"\nQue cantidad de {eleccion} quieres guardar: "))
                            if cantidad > 0:
                                if cantidad <= inventario[eleccion]['cantidad']:
                                    inventario[eleccion]['cantidad'] -= cantidad
                                    armario.update(arma(eleccion))
                                    armario[eleccion]['cantidad'] = cantidad
                                    break

                                else:
                                    raise TypeError
                            else:
                                raise TypeError

                        except TypeError:
                            print("\nLa cantidad introducida es incorrecta, o mayor a la posible, introduce otro dato")
                            continue
                    print(inventario)
                    print(armario)

                elif eleccion_inventario == 2:
                    print("\nEstos son tus objetos:")
                    contador = 1

                    for objetos in bolsillo:
                        print(f"{contador})", objetos)
                        contador += 1
                    while guardar_objetos:
                        try:
                            eleccion = input("\nQue objeto deseas guardar: ")
                            if eleccion == 'Monedas':
                                while guardar_objetos:
                                    print("Las monedas no se pueden guardar elige otro objeto")
                                    break
                                continue
                            else:

                                while guardar_objetos:

                                    try:
                                        print(bolsillo[eleccion]['cantidad'])
                                        # Revisar Hacha dos manos ya que salta un error
                                        cantidad = int(input(f"\nQue cantidad de {eleccion} quieres guardar: "))
                                        if cantidad > 0:
                                            if cantidad <= inventario[eleccion]['cantidad']:
                                                inventario[eleccion]['cantidad'] -= cantidad
                                                armario.update(arma(eleccion))
                                                armario[eleccion]['cantidad'] = cantidad
                                                break

                                            else:
                                                raise TypeError
                                        else:
                                            raise TypeError

                                    except TypeError:
                                        print(
                                            "\nLa cantidad introducida es incorrecta, o mayor a la posible, introduce otro dato")
                                        continue
                                print(inventario)
                                print(armario)

                        except KeyError:
                            print("El objeto introducido no se encuentra en la mochila, introduce otro")
                            continue

                eleccion = int(input("\nQuieres seguir guardando objetos (1) o deseas salir (0): "))

                if eleccion == 1:
                    continue

                elif eleccion == 0:
                    print("\nVas a salir del menu del armario. ")
                    guardar_objetos = False

        elif decision == 3:
            print("Muy bien has decidido salir de la cueva")
            cueva = False
            # mapa(inv,mochila), aqui llamariamos de nuevo a la funcion del mapa para que el jugador eliga un sitio a donde ir

        else:
            print("La opción introducida no es correcta intentalo de nuevo, jugador.")
            continue
    print("*Vuelves al poblado*")
    return inventario, bolsillo, stats_player, armario

