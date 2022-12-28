# Versión oficial
import random
from lib import features
from lib import fun_puntos


# Desarrollo
# Bienvenida al juego
features.borrar_pantalla()
print('Inicia sesión: ')
nombre = input('Usuario: ')
features.pantalla_de_carga()
print(f'¡Bienvenido {nombre}!')

# Habilidades del personaje
personaje_habilidades = {'fuerza': 10, 'destreza': 10, 'constitucion': 10}
dano = personaje_habilidades['fuerza'] - 10
defensa = personaje_habilidades['destreza'] - 10
vida = 20 + (2 * (personaje_habilidades['constitucion'] - 10))
puntos_habilidades = 3

# Creación del personaje
run_1 = True
while run_1:
    print(f'Tienes {puntos_habilidades} puntos disponibles para tus habilidades (fuerza/destreza/constitución)')
    decision_1 = input('¿Deseas repartirlos? [s/n]: ')
    if decision_1.lower() == 's':
        run_2 = True
        while run_2:
            habilidad = input('¿Qué habilidad vas a mejorar? [f/d/c]: ')
            puntos = int(input('¿Cuántos puntos vas a utilizar?: '))
            if habilidad.lower() == 'f' and puntos >= 0 and puntos <= puntos_habilidades:
                reparto = fun_puntos.nuevo_punto(personaje_habilidades, 'fuerza', puntos)
                personaje_habilidades = reparto[0]
                puntos_habilidades = reparto[1]
                run_1, run_2 = False, False
            elif habilidad.lower() == 'd' and puntos >= 0 and puntos <= puntos_habilidades:
                reparto = fun_puntos.nuevo_punto(personaje_habilidades, 'destreza', puntos)
                personaje_habilidades = reparto[0]
                puntos_habilidades = reparto[1]
                run_1, run_2 = False, False
            elif habilidad.lower() == 'c' and puntos >= 0 and puntos <= puntos_habilidades:
                reparto = fun_puntos.nuevo_punto(personaje_habilidades, 'constitucion', puntos)
                personaje_habilidades = reparto[0]
                puntos_habilidades = reparto[1]
                run_1, run_2 = False, False
            else:
                features.borrar_pantalla()
                print('Algo ha ido mal, repita el proceso por favor')
                continue
    elif decision_1.lower() == 'n':
        run_1 = False
    else:  # Corrección de posible error
        features.borrar_pantalla
        print('Algo ha ido mal, repita el proceso por favor')
        continue