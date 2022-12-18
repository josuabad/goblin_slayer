import time
import fun_borrar_pantalla
import fun_extraccion_dict


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

"""
def inventario(mochila, mochila_sin_uso):  # La mochila es una lista de cosas que lleva el personaje
    run1 = True
    if len(mochila_sin_uso) == 0:  # mochila_sin_uso == inventario. Si == 0; esta vacía, solo puede añadir
        while run1:
            print('Todavía no tienes nada guardado en el inventario')  # El inventario es una lista de cosas que se deja el personaje en su cueva
            nuevo_item = input('¿Deseas añadir algo? [s/n]: ')
            if nuevo_item.lower() == 's':
                fun_borrar_pantalla.borrar_pantalla()
                num = int(input('¿Cuantas cosas vas a añadir?: '))
                print(f'Acuerdate que tienes {len(mochila)} guardadas en tu mochila:\n')
                fun_extraccion_dict.extraccion_dict(mochila, 'cantidad')
                for item in range(num):  # Para cada nuevo elemento añadido...
                    objeto_clase = input(f'{item + 1}. ¿Qué clase de objeto vas a añadir?:\n'  # Especificar 4 opciones: clase (arma, escudo...), nombre (espada mágica, escudo básico...), característica (cantidad, daño...), valor (de cada característica)
                    f'1. Arma\n'
                    f'2. Escudo\n'
                    f'3. Poción\n'
                    f'Tu elección [1/2/3]: ')
                    # Pensando en que hay que usar diccionarios
            else:
                pass
    else:  # mochila_sin_uso no está vacía, puede elegir entre añadir o coger
        pass
    """
    """
    if len(mochila_sin_uso) == 0:  # mochila_sin_uso == inventario. Si == 0; esta vacía

            
                for item in range(num):  # Desarrolla inventario y mochila personal
                    nuevo_objeto_tipo = input(f'{item}. Introduce el nombre del objeto deseado: ')
                    if mochila.get(nuevo_objeto_tipo.lower()) > 1:
                        while True:
                            nuevo_objeto_numero = input(f'¿Cuántos elementos de este tipo quieres meter? Tienes {mochila.get(nuevo_objeto_tipo.lower())}')
                            try:
                                nuevo_objeto_numero = int(nuevo_objeto_numero)
                                if nuevo_objeto_numero > mochila.get(nuevo_objeto_tipo.lower()):
                                    print('No tienes esa cantidad disponible. Por favor vuelve a intentarlo')
                                    continue
                                else:  # Actualiza inventario y mochila personal
                                    mochila_sin_uso.update({nuevo_objeto_tipo: nuevo_objeto_numero})
                                    restante = mochila.get(nuevo_objeto_tipo) - mochila_sin_uso.get(nuevo_objeto_tipo)
                                    if restante == 0:
                                        del mochila[nuevo_objeto_tipo]
                                    else:
                                        mochila.update({nuevo_objeto_tipo: restante})
                            except:
                                print('Opción no válida. Por favor vuelve a intentarlo')
                                continue
                    else:
                        pass
            elif nuevo.lower() == 'n':
                return mochila_sin_uso  # Sale del inventario. No tienes nada
            else:
                print('Opción incorrecta')
                error = input('¿Quieres salir o seguir en el inventario? [S/I]: ')
                if error.lower() == 's':
                    seguir = False
                elif error.lower() == 'i':
                    break
                else:
                    print('Opción no encontrada')
                    continue
    else:
        print(f'Tienes {len(mochila_sin_uso)} guardadas:\n')
        for cosas in range(len(mochila_sin_uso)):
            print(f'{cosas + 1}. {mochila_sin_uso[cosas]}\n')
        seguir = True
        while seguir:
            nuevo = input('¿Deseas añadir o coger algo? [A/C]: ')
            if nuevo.lower() == 'a':
                fun_borrar_pantalla.borrar_pantalla()
                num = int(input('¿Cuantas cosas vas a añadir?: '))
                print(f'Acuerdate que tienes {len(mochila)} guardadas en tu mochila:\n')
                for cosas in range(len(mochila)):
                    print(f'{cosas + 1}. {mochila[cosas]}\n')
                for item in range(num):
                    nuevo_objeto_tipo = input(f'{item}. Introduce el nombre del objeto deseado: ')
                    # lista_de_intercambio.append(nuevo_objeto_tipo)
            elif nuevo.lower() == 'c':
                pass  # Modificar
            else:
                print('Opción incorrecta')
                error = input('¿Quieres salir o seguir en el inventario? [S/I]: ')
                if error.lower() == 's':
                    seguir = False
                elif error.lower() == 'i':
                    break
                else:
                    print('Opción no encontrada')
                    continue
"""

# Corregir Line 79
# Line 30: variable
