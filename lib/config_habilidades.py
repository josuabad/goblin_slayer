import time
import features
import fun_puntos


def habilidades(habilidades, puntos):
    if puntos == 0:
        print('No tienes puntos de habilidad disponibles')
        print('Sigue jugando para conseguir mejoras y subir de nivel')
        time.sleep(3)
        features.borrar_pantalla
        return habilidades, puntos
    else:
        while True:
            print(f'Tienes {puntos} puntos disponibles para tus habilidades (fuerza/destreza/constitución)')
            decision_1 = input('¿Deseas repartirlos? [s/n]: ')
            if decision_1.lower() == 's':
                while True:
                    habilidad = input('¿Qué habilidad vas a mejorar? [f/d/c]: ')
                    num_puntos = int(input('¿Cuántos puntos vas a utilizar?: '))
                    if habilidad.lower() == 'f' and puntos >= 0 and num_puntos <= puntos:
                        reparto = fun_puntos.nuevo_punto(habilidades, 'fuerza', num_puntos, puntos)
                        puntos = reparto[1]
                        return habilidades, puntos
                    elif habilidad.lower() == 'd' and puntos >= 0 and num_puntos <= puntos:
                        reparto = fun_puntos.nuevo_punto(habilidades, 'destreza', num_puntos, puntos)
                        puntos = reparto[1]
                        return habilidades, puntos
                    elif habilidad.lower() == 'c' and puntos >= 0 and num_puntos <= puntos:
                        reparto = fun_puntos.nuevo_punto(habilidades, 'constitucion', num_puntos, puntos)
                        puntos = reparto[1]
                        return habilidades, puntos
                    elif num_puntos > puntos:
                        print('No puedes usar más puntos de los que tienes')
                        print('Por favor, repita el proceso con una cantidad coherente')
                    else:
                        features.borrar_pantalla()
                        print('Algo ha ido mal, repita el proceso por favor')
                        continue
            elif decision_1.lower() == 'n':
                return habilidades, puntos
            else:  # Soporte de errores
                features.borrar_pantalla
                print('Algo ha ido mal, repita el proceso por favor')
                continue


def especificas_personaje(personaje_habilidades):
    dano = personaje_habilidades['fuerza'] - 10
    defensa = personaje_habilidades['destreza'] - 10
    vida = 20 + (2 * (personaje_habilidades['constitucion'] - 10))
    return dano, defensa, vida