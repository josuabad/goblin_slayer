import time
import fun_tienda
import features
import Taberna
import funcionesjueguito


def fun_mapa(player, mochi, bolsa, inventario, stats_player):  # Función Mapa
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
                fun_tienda.fun_tienda(mochi, bolsa)  # Ir a la tienda
            elif lugar_pueblo == 2:
                print("Vamos a la alcantarilla")
                input('Presiona ENTER para continuar...')
                funcionesjueguito.combate(inventario, stats_player, 1)  # Ir a la cueva de las ratas
            elif lugar_pueblo == 3:
                print(f'Genial, vamos a la Taberna')
                input('Presiona ENTER para continuar...')
                Taberna.taberna(inventario, stats_player)  # Ir a la taberna
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
            funcionesjueguito.cueva_ogro(inventario, stats_player)
            # insertar función del combate con el Ogro
        else:
            print(f'Ese lugar no existe {player}, introduce otro.')
            input('Presiona ENTER para continuar...')
            continue


inventario = 0
stats_player = {"vida": 13, "const": 1, "destreza": 11, "fuerza": 11, }
mochila = {"arma": {"puño": 0}, "Monedas": 4, "Hidromiel": 0}
bolsillo = {'espada goblin': {'daño': 6, 'precio': None, 'venta': 5, 'manos': 1, 'arma': True, 'cantidad': 3},
            'escudo goblin': {'precio': None, 'venta': 5, 'destreza': 1, 'protección': True, 'cantidad': 1}}
mochi = {'escudo': {'precio': 10, 'venta': 10 * 0.8, 'destreza': 1, 'protección': True, 'cantidad': 0},
         'espada': {'daño': 8, 'precio': 10, 'venta': 10 * 0.8, 'manos': 1, 'arma': True, 'cantidad': 1},
         'espada magica': {'daño': 6, 'precio': 200, 'venta': 200 * 0.5, 'manos': 1, 'arma': True, 'cantidad': 0},
         'hacha dos manos': {'daño': 12, 'precio': 30, 'venta': 30 * 0.5, 'manos': 2, 'arma': True, 'cantidad': 0},
         'armadura nivel 1': {'precio': 30, 'venta': 30 * 0.5, 'destreza': 2, 'protección': True, 'cantidad': 0},
         'armadura nivel 2': {'precio': 40, 'venta': 40 * 0.5, 'destreza': 3, 'protección': True, 'cantidad': 0},
         'armadura nivel 3': {'precio': 50, 'venta': 50 * 0.5, 'destreza': 4, 'protección': True, 'cantidad': 0},
         'pocion de vida': {'precio': 20, 'venta': 20 * 0.5, 'vida': 2, 'pocion': True, 'cantidad': 0}, 'monedas': 1000
         }

fun_mapa('isa', mochi, bolsillo, inventario, stats_player)
