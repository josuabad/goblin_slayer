import time
from lib import fun_borrar_pantalla
from lib import fun_dict


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
    inventariado = dict(guardado)
    run1 = True
    if len(guardado) == 0:  # guardado == inventario. Si == 0; esta vacía, solo puede añadir
        while run1:
            print('Todavía no tienes nada guardado en el inventario')  # El inventario es una lista de cosas que se deja el personaje en su cueva
            nuevo_item = input('¿Deseas añadir algo? [s/n]: ')
            if nuevo_item.lower() == 's':
                fun_borrar_pantalla.borrar()
                num = int(input('¿Cuántos elementos distintos vas a añadir?: '))
                print(f'Acuerdate que tienes {len(mochila)} elementos distintos guardados en tu mochila:\n')
                fun_dict.extraer(mochila, 'any', 'cantidad', False)
                for item in range(num):  # Para cada nuevo elemento distinto añadido...
                    run2 = True
                    while run2:
                        elemento = input(f'{item + 1}. ¿Qué elemento vas a añadir?: ')
                        if mochila.get(elemento) != None:  # Verificar que el elemento está en la mochila
                            cantidad = fun_dict.extraer(mochila, elemento, 'cantidad')
                            if cantidad > 1:  # Está en la mochila. ¿Tienes más de 1, cuántos hay que guardar?
                                print(f'Tienes un total de {cantidad} {elemento}s guardad@s')
                                guardar = int(input('¿Cuánt@s quieres guardar?: '))
                                # Extracción de elementos
                                """
                                Existen 3 casos:
                                1. Guardas parte de los elementos
                                2. Guardas todos los elementos
                                3. Te equivocas y decides guardar una cantidad que no existe; ya sea un número superior, negativo/=0, o sea una letra (ValueError)
                                """
                                # Quiero saber los atributos de un elemento que no se dónde se encuentra.
                                mochila_view_keys = list(mochila.keys())
                                mochila_view_values = list(mochila.values())
                                # Tengo que saber dónde está para preguntarle cositas
                                donde_encontrar = mochila_view_keys.index(elemento)
                                # Ahora quiero saber los atributos del elemento.
                                donde_buscar = list(mochila_view_values[donde_encontrar].keys())
                                # Pero no se donde tengo que cambiar
                                donde_cambiar = donde_buscar.index('cantidad')
                                # Y, como los quiero manipular, pongo como una lista los valores que tengo que cambiar
                                que_cambiar = list(mochila_view_values[donde_encontrar].values())
                                # Desarrollo
                                if guardar < cantidad and guardar > 0:  # Caso 1
                                    inventariado.update({mochila_view_keys[donde_encontrar]: {donde_buscar[donde_cambiar]: guardar}})  # 1º Metes en el inventario todo lo que quieres guardar
                                    # Pasar todos los atributos restantes del elemento
                                    donde_buscar.pop(donde_cambiar)
                                    que_cambiar.pop(donde_cambiar)
                                    for elmnt in donde_buscar:
                                        inventariado[mochila_view_keys[donde_encontrar]][elmnt] = que_cambiar[donde_buscar.index(elmnt)]
                                    # Borrar el sobrante de la mochila
                                    # cantidad_original = fun_extraccion_dict.extraer(mochila, 'espada', 'cantidad')
                                    # mochila[mochila_view_keys[donde_encontrar]]['cantidad'] = cantidad_original - guardar
                                elif guardar == cantidad:  # Caso 2
                                    inventariado.update({mochila_view_keys[donde_encontrar]: {donde_buscar[donde_cambiar]: guardar}})  # 1º Metes en el inventario todo lo que quieres guardar
                                else:  # Caso 3. Se podría usar un try/except
                                    pass
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
            else:
                pass
    else:  # guardado no está vacía, puede elegir entre añadir o coger elementos
        pass

# Line 66:67
# Este código no soporta todos los errores de valor