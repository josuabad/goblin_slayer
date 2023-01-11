# Módulos
from lib import features


# Funciones
def nuevo_punto(diccionario: dict, habilidad: str, num_puntos: int, puntos: int):
    # Explicación:
    # Introducir el diccionario, la habilidad a modificar, el número de puntos que se vaya a usar y la cantidad total
    # El num_puntos son los puntos que se van a usar
    # La variable puntos (total) van a ser los puntos restantes, quitando num_puntos al total del que se disponen
    # Desarrollo:
    for punto in range(num_puntos):
        if habilidad == 'fuerza':
            if diccionario[habilidad] < 14:
                diccionario[habilidad] += 1
                puntos -= 1
            else:
                print(f'Recuerda que solo puedes añadir hasta 4 puntos en fuerza. Tienes {diccionario[habilidad]}')
                input('Presiona ENTER para continuar...')
                return diccionario, puntos
        elif habilidad == 'destreza':
            diccionario[habilidad] += 1
            puntos -= 1
        elif habilidad == 'constitucion':
            diccionario[habilidad] += 1
            puntos -= 1
    return diccionario, puntos


def habilidades(dict_habilidades: dict, puntos: int):
    # Explicación
    # En base al las habilidades del personaje y los puntos de habilidades que tenga
    # La función se encarga se repartir los puntos que quiera, siempre y cuando los tenga disponibles
    # Desarrollo:
    if puntos == 0:
        print('No tienes puntos de habilidad disponibles')
        print('Sigue jugando para conseguir mejoras y subir de nivel')
        input('Presiona ENTER para continuar...')
        features.borrar_pantalla()
        return dict_habilidades, puntos
    else:
        features.borrar_pantalla()
        while True:
            print(f'Tienes {puntos} puntos disponibles para tus habilidades (fuerza/destreza/constitución)')
            decision_1 = input('¿Deseas repartirlos? [s/n]: ')
            if decision_1.lower() == 's':
                while True:
                    mis_habilidades = input('¿Qué habilidad vas a mejorar? [f/d/c]: ')
                    num_puntos = input('¿Cuántos puntos vas a utilizar?: ')
                    try:
                        num_puntos = int(num_puntos)
                    except:
                        features.borrar_pantalla()
                        print('Algo ha ido mal, repita el proceso por favor')
                        continue
                    if mis_habilidades.lower() == 'f' and puntos >= 0 and num_puntos <= puntos:
                        reparto = nuevo_punto(dict_habilidades, 'fuerza', num_puntos, puntos)
                        puntos = reparto[1]
                        return dict_habilidades, puntos
                    elif mis_habilidades.lower() == 'd' and puntos >= 0 and num_puntos <= puntos:
                        reparto = nuevo_punto(dict_habilidades, 'destreza', num_puntos, puntos)
                        puntos = reparto[1]
                        return dict_habilidades, puntos
                    elif mis_habilidades.lower() == 'c' and puntos >= 0 and num_puntos <= puntos:
                        reparto = nuevo_punto(dict_habilidades, 'constitucion', num_puntos, puntos)
                        puntos = reparto[1]
                        return dict_habilidades, puntos
                    elif num_puntos > puntos or num_puntos < puntos:
                        if num_puntos > puntos:
                            print('No puedes usar más puntos de los que tienes')
                        else:
                            pass
                        print('Por favor, repita el proceso con una cantidad coherente')
                        continue
                    else:
                        features.borrar_pantalla()
                        print('Algo ha ido mal, repita el proceso por favor')
                        continue
            elif decision_1.lower() == 'n':
                return dict_habilidades, puntos
            else:  # Soporte de errores
                features.borrar_pantalla()
                print('Algo ha ido mal, repita el proceso por favor')
                continue


def especificas_personaje(dict_habilidades, dict_especificas):
    # Explicación:
    # Permite la relación entre las habilidades generales del personaje (fz/dt/cn) y las específicas (do/df/vd)
    # Desarrollo:
    dano = dict_habilidades['fuerza'] - 10
    dict_especificas['daño'] = dano
    defensa = 12 + (dict_habilidades['destreza'] - 10)
    dict_especificas['defensa'] = defensa
    vida = 20 + (2 * (dict_habilidades['constitucion'] - 10))
    dict_especificas['vida'] = vida
    return dict_especificas
