import time
import fun_borrar_pantalla


def cama(vida, tiempo):  # Para recuperar toda la vida hay que dormir 8 horas
    if tiempo > 8:
        return False, '¡No puedes dormir tanto!¡El pueblo te necesita!'  # False. Tiene que pedir desde el archivo un nuevo tiempo
    else:
        relacion_sueño = vida/8
        for horas in range(tiempo + 1):
            print(f'Has dormido {horas} horas')
            time.sleep(relacion_sueño)
            fun_borrar_pantalla.borrar_pantalla()
        return relacion_sueño * tiempo  # Vida recuperada


def inventario(mochila, mochila_sin_uso=0):  # La mochila es una lista de cosas que lleva el personaje
    if mochila_sin_uso == 0:
        mochila_sin_uso = []  # Lista de cosas que se deja el personaje en su cueva
    else:
        print(f'Tienes {len(mochila_sin_uso)} guardas:\n')
        for cosas in range(len(mochila_sin_uso)):
            print(f'{cosas + 1}. {mochila_sin_uso[cosas]}')
    
    # ¿Deseas añadir algo? ...
    # Que sí: cuantas cosas, cuales cosas (desde la mochila), las añades, devuelve nuevas cosas guardadas.
    # Que no: te vas a ir a la puerta de tu cueva a ver qué haces, devuelve False.
