"""Esto está listo, lo que falta es:
- Llamar las funciones en cada uno de los apartados.
- Crear una variable o lista que guarde donde está el personaje, de manera que cuando te salga el menú, te diga donde
está el personaje en ese momento. """

import random
import time


def mapa():
    if menu_viaje == 1:
        print("Vamos al pueblo")
        lugar_pueblo = str(input("Quieres ir a la tienda o a las alcantarillas: "))
        if lugar_pueblo == 'tienda':
            print(f'Vamos a entrar a la tienda, ¿que te apetece comprar?\n{Tienda}')
            # insertar función de Tienda = " Fun_Tienda() "

        elif lugar_pueblo == 'alcantarillas':
            print("Vamos a la alcantarilla")
            # insertar función de combate con ratas

        else:
            print("Ese lugar no existe")

    elif menu_viaje == 2:
        print("Vamos a la cueva, ¡prepárate!")
        # insertar función de combate

    elif menu_viaje == 3:
        print("Vamos a la GUARIDA DEL OGRO, ¡prepárate!")
        # insertar función del combate con el Ogro

    else:
        print("Ese lugar no existe.")


menu_viaje = int(input("############################\n           MAPA\nElige a donde quieres ir: "
                       "\n1)Pueblo\n2)Cuevas\n3)Guarida\nColoca el número de tu opción: "))

Tienda = ['armas', 'destreza_player', 'fuerza_player', 'constitucion_player', 'pocion', ]
posicion_player = ''  # guarda donde está el personaje
print(mapa())

#       NOTAS       #

" (T) Tienda "

"""
La tienda la hago en una funcion, y luego puras listas en ella
Una lista para armas.
 """