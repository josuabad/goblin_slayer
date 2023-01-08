import time
import fun_tienda
import features


def fun_mapa(player, mochila, bolsa):  # Función Mapa
    while True:
        menu_viaje = int(input("############################\n           "
                               "MAPA\n"
                               "Elige a donde quieres ir:"
                               "\n1)Pueblo\n2)Cuevas\n3)Guarida\n"
                               "Coloca el número de tu opción: "))
        if menu_viaje == 1:
            features.borrar_pantalla()
            print("Vamos al pueblo")
            input('Presiona ENTER para continuar...')
            lugar_pueblo = int(input(f'¿A que lugar del pueblo quieres ir?\n1) Tienda\n2) Alcantarillas\n3) Taberna\n'
                                     f'4) {player} cueva\n5) Salir del pueblo\n - Inserta el número: '))
            if lugar_pueblo == 1:
                print(f'Vamos a entrar a la tienda')
                input('Presiona ENTER para continuar...')
                fun_tienda.fun_tienda(mochila, bolsa)
                # Ir a la tienda
            elif lugar_pueblo == 2:
                print("Vamos a la alcantarilla")
                input('Presiona ENTER para continuar...')
                # Ir a la cueva de las ratas
            elif lugar_pueblo == 3:
                print(f'Genial, vamos a la Taberna')
                input('Presiona ENTER para continuar...')
                # Ir a la taberna
            elif lugar_pueblo == 4:
                print(f'Vale, vamos a tu cueva {player}')
                input('Presiona ENTER para continuar...')
                # insertar funcion de cueva del jugador
            elif lugar_pueblo == 5:
                print("Regresemos...")
                input('Presiona ENTER para continuar...')
                continue  # Regresamos al menú
            else:
                print("Ese lugar no existe")
                input('Presiona ENTER para continuar...')
                continue
        elif menu_viaje == 2:
            print("Vamos a la cueva, ¡prepárate!")
            input('Presiona ENTER para continuar...')
            # insertar función de combate
        elif menu_viaje == 3:
            print("Vamos a la GUARIDA DEL OGRO, ¡prepárate!")
            input('Presiona ENTER para continuar...')
            # insertar función del combate con el Ogro
        else:
            print(f'Ese lugar no existe {player}, introduce otro.')
            input('Presiona ENTER para continuar...')
            continue


mochi = {'espada': {'daño': 8, 'precio': 10, 'venta': 8, 'manos': 1, 'arma': True, 'cantidad': 1}}
bolsillo = {'espada goblin': {'daño': 6, 'precio': None, 'venta': 5, 'manos': 1, 'arma': True, 'cantidad': 1}}

fun_mapa('isa', mochi, bolsillo)
