# Función puntos de experiencia
import random
import time
import config_habilidades


def experiencia(personaje, habilidad):
    if 250 <= personaje.get('experiencia') < 500:
        personaje.update({"level": personaje.get("level") + 1})
        print('¡Enhorabuena! Has llegado al Nivel 1')
        puntos = random.randint(1, 8)
        config_habilidades.nuevo_punto(habilidad, 'constitucion', puntos, 0)
        personaje['vida'] = 20
        config_habilidades.especificas_personaje(habilidad, personaje)
        print(f'Te obsequiamos {puntos} puntos de vida permanentes')
        print(f'Tus habilidades se quedan de la siguiente manera:\n'
              f'{personaje}')
        return personaje, habilidad

    elif 500 <= personaje.get('experiencia') < 1000:
        personaje.update({"level": personaje.get("level") + 1})
        print('¡Enhorabuena! Has llegado al Nivel 2')
        puntos = random.randint(1, 8)
        config_habilidades.nuevo_punto(habilidad, 'constitucion', puntos, 0)
        personaje['vida'] = 20
        config_habilidades.especificas_personaje(habilidad, personaje)
        print(f'Te obsequiamos {puntos} puntos de vida permanentes')
        print(f'Tus habilidades se quedan de la siguiente manera:\n'
              f'{personaje}')
        return personaje, habilidad

    elif 1000 <= personaje.get('experiencia') < 10000:
        personaje.update({"level": personaje.get("level") + 1})
        print('¡Enhorabuena! Has llegado al Nivel 3')
        puntos = random.randint(1, 8)
        config_habilidades.nuevo_punto(habilidad, 'constitucion', puntos, 0)
        personaje['vida'] = 20
        config_habilidades.especificas_personaje(habilidad, personaje)
        print(f'Te obsequiamos {puntos} puntos de vida permanentes')
        print(f'Tus habilidades se quedan de la siguiente manera:\n'
              f'{personaje}')
        punto_extra = str(input('¡También te obsequiamos 1 punto en cualquiera de tus habilidades!\n'
                                '--> Fuerza\n'
                                '--> Destreza\n'
                                '--> Constitución\n'
                                '¿Dónde te gustaría repartir tu punto [f/d/c] ?: '))
        if punto_extra.lower() == 'f':
            personaje.update({'fuerza': personaje.get('fuerza') + 1})
            print(f'GENIAL\n'
                  'Has escogido Fuerza')
            time.sleep(0.5)
            print('Tus habilidades se quedan de la siguiente manera:\n'
                  f'{personaje}')
        elif punto_extra.lower() == 'd':
            personaje.update({'destreza': personaje.get('destreza') + 1})
            print(f'GENIAL\n'
                  'Has escogido Destreza')
            time.sleep(0.5)
            print('Tus habilidades se quedan de la siguiente manera:\n'
                  f'{personaje}')
        elif punto_extra.lower() == 'c':
            personaje.update({'constitucion': personaje.get('constitucion') + 1})
            print(f'GENIAL\n'
                  'Has escogido Constitución')
            time.sleep(0.5)
            print('Tus habilidades se quedan de la siguiente manera:\n'
                  f'{personaje}')
        return personaje, habilidad


personaje_habilidades = {'fuerza': 10, 'destreza': 10, 'constitucion': 10}
personaje_especificas = {'daño': 0, 'defensa': 0, 'vida': 0, 'experiencia': 1000, 'level': 0}
experiencia(personaje_especificas, personaje_habilidades)
print(personaje_habilidades)
print(personaje_especificas)
