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
        print('¡También te obsequiamos 1 punto en cualquiera de tus habilidades!')
        config_habilidades.habilidades(personaje_habilidades, 1)
        return personaje, habilidad


personaje_habilidades = {'fuerza': 10, 'destreza': 10, 'constitucion': 10}
personaje_especificas = {'daño': 0, 'defensa': 0, 'vida': 0, 'experiencia': 1000, 'level': 0}
experiencia(personaje_especificas, personaje_habilidades)
print(personaje_habilidades)
print(personaje_especificas)
