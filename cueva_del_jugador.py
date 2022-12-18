import time
from lib import fun_borrar_pantalla
from lib import fun_extraccion_dict


def cama(vida, tiempo):  # Para recuperar toda la vida hay que dormir 8 horas
    if tiempo > 8:
        return False, '¡No puedes dormir tanto!¡El pueblo te necesita!'  # False. Tiene que pedir desde el archivo un nuevo tiempo
    else:
        relacion_sueño = vida/8
        for horas in range(tiempo + 1):
            print(f'Has dormido {horas} horas')
            time.sleep(relacion_sueño)
            fun_borrar_pantalla.borrar()
        return relacion_sueño * tiempo  # Vida recuperada


def inventario(mochila, guardado):  # La mochila es una lista de cosas que lleva el personaje
    run1 = True
    if len(guardado) == 0:  # guardado == inventario. Si == 0; esta vacía, solo puede añadir
        while run1:
            print('Todavía no tienes nada guardado en el inventario')  # El inventario es una lista de cosas que se deja el personaje en su cueva
            nuevo_item = input('¿Deseas añadir algo? [s/n]: ')
            if nuevo_item.lower() == 's':
                fun_borrar_pantalla.borrar()
                num = int(input('¿Cuántos elementos distintos vas a añadir?: '))
                print(f'Acuerdate que tienes {len(mochila)} elementos distintos guardados en tu mochila:\n')
                fun_extraccion_dict.extraer(mochila, 'any', 'cantidad', False)
                for item in range(num):  # Para cada nuevo elemento distinto añadido...
                    run2 = True
                    while run2:
                        elemento = input(f'{item + 1}. ¿Qué elemento vas a añadir?: ')
                        if mochila.get(elemento) != None:  # Verificar que el elemento está en la mochila
                            cantidad = fun_extraccion_dict.extraer(mochila, elemento, 'cantidad')
                            if cantidad > 1:  # Está en la mochila. ¿Tienes más de 1, cuántos hay que guardar?
                                print(f'Tienes un total de {cantidad} {elemento}s guardad@s')
                                guardar = int(input('¿Cuánt@s quieres guardar?: '))
                                # GUARDAR TODOS LOS ATRIBUTOS
                                lista_keys = list(mochila.keys())
                                lista_values = list(mochila.values())
                            else:
                                pass
                        else:  # El caso contrario es que no lo este
                            print('Este elemento no existe.')
                            while True:
                                error1 = input('¿Desea volver a intentarlo o salir? [v/s]: ')
                                if error1.lower() == 'v':
                                    break
                                elif error1.lower() == 's':
                                    run2 = False
                                else:
                                    error1 = input('No te he entendido.')
                                    continue
                    # Pensando en que hay que usar diccionarios
            else:
                pass
    else:  # guardado no está vacía, puede elegir entre añadir o coger
        pass