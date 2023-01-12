from lib import features
from modulos import Taberna, fun_tienda, Easter_Egg, Cueva_Jugador, funcionesjueguito


def fun_mapa(player, inventario, bolsillo, stats_player, habilidad, puntos, armario):  # Función Mapa
    while True:
        features.borrar_pantalla()
        menu_viaje = input("============================\n           "
                               "MAPA\n"
                               "============================\n"
                               "Elige a donde quieres ir:"
                               "\n1)Pueblo\n2)Cueva de los Goblins\n3)Cueva del Ogro\n"
                               "Coloca el número de tu opción: ")
        try:
            menu_viaje = int(menu_viaje)
        except:
            print('Algo ha ido mal, repita el proceso por favor')
            input('Presiona ENTER para continuar...')
            continue
        if menu_viaje == 1:
            features.borrar_pantalla()
            print("Vamos al pueblo")
            input('Presiona ENTER para continuar...')
            lugar_pueblo = input(f'¿A que lugar del pueblo quieres ir?\n1) Tienda\n2) Alcantarillas\n3) Taberna\n'
                                     f'4) {player} cueva\n5) Salir del pueblo\n - Inserta el número: ')
            try:
                lugar_pueblo = int(lugar_pueblo)
            except:
                print('Algo ha ido mal, repita el proceso por favor')
                input('Presiona ENTER para continuar...')
                continue
            if lugar_pueblo == 1:
                features.borrar_pantalla()
                print(f'Vamos a entrar a la tienda')
                input('Presiona ENTER para continuar...')
                fun_tienda.fun_tienda(inventario, bolsillo, habilidad, puntos)  # Ir a la tienda
            elif lugar_pueblo == 2:
                features.borrar_pantalla()
                print("Vamos a la alcantarilla")
                input('Presiona ENTER para continuar...')
                funcionesjueguito.combate(inventario, stats_player, 1, habilidad, bolsillo)  # Ir a la cueva de las ratas
            elif lugar_pueblo == 3:
                features.borrar_pantalla()
                print(f'Genial, vamos a la Taberna')
                input('Presiona ENTER para continuar...')
                Taberna.taberna(inventario, stats_player,habilidad,bolsillo)  # Ir a la taberna
            elif lugar_pueblo == 4:
                features.borrar_pantalla()
                print(f'Vale, vamos a tu cueva {player}')
                input('Presiona ENTER para continuar...')
                Cueva_Jugador.cueva_jugador(inventario, bolsillo, stats_player,habilidad, armario)  # Ir a tu cueva o casa
            elif lugar_pueblo == 5:
                print("Regresemos...")
                input('Presiona ENTER para continuar...')
                continue  # Regresamos al menú
            else:
                print("Ese lugar no existe")
                input('Presiona ENTER para continuar...')  # Por si el usuario mete una opción no válida
                continue
        elif menu_viaje == 2:
            features.borrar_pantalla()
            print("Vamos a la Cueva de los Goblins, ¡prepárate!")
            input('Presiona ENTER para continuar...')
            funcionesjueguito.combate(inventario, stats_player, 2, habilidad, bolsillo)  # Ir a la cueva de los goblins
        elif menu_viaje == 3:
            features.borrar_pantalla()
            print("Vamos a la CUEVA DEL OGRO, ¡prepárate!")
            input('Presiona ENTER para continuar...')
            funcionesjueguito.cueva_ogro(inventario,bolsillo,stats_player,habilidad)  # Ir a la cueva del ogro
        elif menu_viaje == 4:
            Easter_Egg.EasterEgg(bolsillo, stats_player,)
        else:
            print(f'Ese lugar no existe {player}, introduce otro.')
            input('Presiona ENTER para continuar...')
            continue
