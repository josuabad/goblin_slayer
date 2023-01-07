import time


def Fun_mapa(menu_viaje):  # Función Mapa
    while hola == 1:
        if menu_viaje == 1:
            time.sleep(0.5)
            print("Vamos al pueblo")
            lugar_pueblo = int(input(f'¿A que lugar del pueblo quieres ir?\n1) Tienda\n2) Alcantarillas\n3) Taberna\n4) {player} cueva\n- Inserta el número: '))
            time.sleep(0.5)
            if lugar_pueblo == 1:
                print(f'Vamos a entrar a la tienda')
                time.sleep(1)
                from Fun_Tienda import Fun_Tienda

            elif lugar_pueblo == 2:
                print("Vamos a la alcantarilla")
                time.sleep(1)
                # insertar función de combate con ratas
            elif lugar_pueblo == 3:
                print(f'Genial, vamos a la Taberna')
                time.sleep(1)
                from Taberna import taberna

            elif lugar_pueblo == 4:
                print(f'Vale, vamos a tu cueva {player}')
                time.sleep(1)
                # insertar funcion de cueva del jugador

            else:
                print("Ese lugar no existe")
                time.sleep(1)
                continue

        elif menu_viaje == 2:
            print("Vamos a la cueva, ¡prepárate!")
            time.sleep(1)
            # insertar función de combate

        elif menu_viaje == 3:
            print("Vamos a la GUARIDA DEL OGRO, ¡prepárate!")
            time.sleep(1)
            # insertar función del combate con el Ogro

        else:
            print(f'Ese lugar no existe {player}, introduce otro.')
            time.sleep(1)
            continue


player = 'Isa'
hola = 1


print(Fun_mapa(int(input("############################\n           MAPA\nElige a donde quieres ir: "
                         "\n1)Pueblo\n2)Cuevas\n3)Guarida\nColoca el número de tu opción: "))))




