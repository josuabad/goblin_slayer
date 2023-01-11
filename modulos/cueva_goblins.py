# Módulos
import time
import random
from lib import features
from lib import articulos
from lib import config_habilidades


# Funciones
def huir(num, inicio=True):
    # Teniendo en cuenta el numero de goblins y el momento del combate, indica si puedes huir o no
    # Devuelve True o False
    dado = random.randint(0, 20)
    if inicio:
        if dado >= 5:
            return True
        else:
            return False
    else:
        if dado >= 10 + num:
            return True
        else:
            return False


def monedas():
    # Calcula la posibilidad de recoger monedas
    # Devuelve la cantidad de monedas o False si no hubo posibilidad
    is_moneda = random.randint(1, 10)
    if is_moneda >= 4:
        cantidad = random.randint(1, 6)
        return cantidad
    else:
        return False


def recuperar_extras(goblin):
    # Teniendo en cuenta el tipo de goblin, calcula la posibilidad de recoger recompensas después de haberlo eliminado
    # Devuelve la recompensa recogida o False si no hubo posibilidad
    is_recuperar = random.randint(1, 10)
    if is_recuperar >= 4:
        if goblin == 'espada':
            return articulos.arma('espada goblin')
        else:
            return articulos.proteccion('escudo goblin')
    else:
        return False


def muerte_goblin(personaje, bolsillo, tipo, num, total=False):
    # En el caso de que muera un goblin, toma las variables del personaje, su bolsillo...
    # El tipo de goblin eliminado, el numero de goblins en la cueva y el si ya no quedan goblins
    # Devuelve las variables personaje con el aumento de experiencia, y el bolsillo con las nuevas recompensas y monedas
    espacio = features.medidor_de_bolsillos(bolsillo)
    if espacio:
        if tipo == 'espada':
            nuevo = recuperar_extras('espada')
        if nuevo:
            try:
                bolsillo['espada goblin']['cantidad'] += 1
            except KeyError:
                bolsillo.update(nuevo)
        else:
            nuevo = recuperar_extras('escudo')
            if nuevo:
                try:
                    bolsillo['escudo goblin']['cantidad'] += 1
                except KeyError:
                    bolsillo.update(nuevo)
        moneda = monedas()
        if moneda:
            try:
                bolsillo['monedas'] += moneda
            except KeyError:
                bolsillo.update({'monedas': moneda})
        if total:
            bonus = 2 * num
            personaje['experiencia'] += bonus
            return personaje, bolsillo
        personaje['experiencia'] += 20
        return personaje, bolsillo
    else:
        pass  # No devuelve nada


def pre_combate(mochila, habilidades, personaje):
    # Equipa el arma y escudo que el jugador quiera y pueda para antes de los combates
    # Además de añadir todas las pociones que tenga el personaje dentro de la mochila
    armas = []
    escudos = []
    pociones = 0
    en_uso = {}
    num = 0
    features.borrar_pantalla()
    print('Armas disponibles')
    for item in mochila:  # Desplegable de todas armas
        try:
            mochila[item]['arma']
            num_manos = mochila[item]['manos']
            num += 1
            print(f'  {num}. {item} | {num_manos} manos')
            armas.append(item)
        except KeyError:  # No hace falta el desplegable de los escudos, nada más se puede llevar uno
            try:
                mochila[item]['proteccion']
                escudos.append(item)
            except KeyError:  # Tampoco hace falta de las pociones, solo hay que guardar en número de pociones que tiene
                pociones = mochila[item]['cantidad']
    input('Presiona ENTER para continuar...')
    while True:  # Saber qué arma coger y si me quedan las manos libres para usar mi escudo
        arma_eleccion = int(input('Introduce el número del arma que quieres coger: '))
        if arma_eleccion < 1 or arma_eleccion > len(armas) or type(arma_eleccion) != int:  # No existe la selección
            features.borrar_pantalla()
            print('Algo ha ido mal, repita el proceso por favor')
            continue
        else:
            en_uso.update(articulos.arma(armas[arma_eleccion - 1]))
            print(f'Has escogido: {armas[arma_eleccion - 1]}')
            input('Presiona ENTER para continuar...')
            break
    manos = 2 - en_uso[armas[arma_eleccion - 1]]['manos']
    while True:
        if manos == 1 and len(escudos) != 0:
            print('Tienes una mano libre con la que puedes coger un escudo')
            usar_escudo = input('¿Quieres equiparte tu escudo?: [s/n]: ')
            if usar_escudo.lower() == 's':
                en_uso.update(articulos.proteccion(escudos[0]))
                # Calcular las nuevas habilidades
                habilidades['destreza'] += 1
                config_habilidades.especificas_personaje(habilidades, personaje)
                break
            elif usar_escudo.lower() == 'n':
                break
            else:
                features.borrar_pantalla()
                print('Algo ha ido mal, repita el proceso por favor')
                continue
        else:
            break  # Comienza el combate
    if pociones > 0:
        en_uso.update(articulos.pocion('pocion de vida'))
        en_uso['poción de vida']['cantidad'] = pociones
    return en_uso, habilidades, personaje  # Recoger variable en_uso, no está preddefinida


def combate(personaje, equipo, bolsillo, tipo_goblin: list):
    # Acción propia del combate entre jugador y goblin espada/escudo
    features.borrar_pantalla()
    print('¡Acabas de entrar en la cueva!')
    conteo_goblins = len(tipo_goblin)  # Número de goblins dentro de la cueva
    for goblin in range(conteo_goblins):
        goblin_escudo = {'vida': 8, 'daño': 8, 'defensa': 13}  # Características de goblin escudo
        goblin_espada = {'vida': 8, 'daño': 6, 'defensa': 12}  # Características de goblin espada
        if goblin == 0:  # No puedes huir porque es el primer goblin
            if tipo_goblin[goblin] == 'espada':
                print(f'El primer enemigo es un goblin con espada. Tiene {goblin_espada["vida"]} puntos de vida')
                input('Presiona ENTER para continuar... ')
                while goblin_espada['vida'] > 0 or personaje['vida'] > 0:  # Mientras que ninguno de los 2 muera...
                    # Consumición de la poción de vida
                    try:
                        is_pocion = equipo['poción de vida']['cantidad']
                        if is_pocion > 0:
                            run = True
                            while run:
                                print(f'Tienes {personaje["vida"]} puntos de vida y {is_pocion} pociones guardadas')
                                usar_pocion = input('¿Quieres consumir una de tus pociones? [s/n]: ')
                                if usar_pocion.lower() == 's':
                                    print(f'Ten en cuenta que la poción de vida regenera {equipo["poción de vida"]["vida"]} puntos de vida como mínimo')
                                    while True:
                                        cantidad = int(input('¿Cuántas quieres consumir?: '))
                                        if 0 <= cantidad <= is_pocion:
                                            for veces in range(cantidad):
                                                posible_vida = random.randint(0, 6)
                                                personaje['vida'] += posible_vida + equipo['poción de vida']['vida']
                                            equipo['poción de vida']['cantidad'] -= cantidad
                                            run = False
                                            break
                                        else:
                                            features.borrar_pantalla()
                                            print('Algo ha ido mal, repita el proceso por favor')
                                            continue
                                elif usar_pocion.lower() == 'n':
                                    break
                                else:
                                    features.borrar_pantalla()
                                    print('Algo ha ido mal, repita el proceso por favor')
                                    continue
                    except KeyError:
                        pass
                    # Intenta atacar el jugador
                    is_impacto_jugador = random.randint(0, 20)
                    if goblin_espada['vida'] <= 0:
                        conteo_goblins -= 1  # Goblin muerto, uno menos
                        print(f'¡Enhorabuena, has acabado con un goblin con espada! Faltan {conteo_goblins}')
                        input('Presiona ENTER para continuar... ')
                        # Loot de goblin muerto
                        muerte_goblin(personaje, bolsillo, 'espada', conteo_goblins)
                        break  # Termina después de regresar el loot correspondiente
                    elif personaje['vida'] <= 0:
                        features.borrar_pantalla()
                        print('Te has muerto')
                        time.sleep(3)
                        exit()
                    elif is_impacto_jugador >= goblin_espada['defensa']:  # Consigue el ataque
                        time.sleep(3)
                        print('¡Perfecto! Has conseguido impactar')
                        for item in equipo:  # Identificar el arma que va a usar
                            try:
                                equipo[item]['arma']
                                impacto_final = random.randint(1, equipo[item]['daño']) + personaje['daño']
                                goblin_espada['vida'] -= impacto_final
                            except KeyError:  # Si al principio no encuentra un arma, vuelve a ver cuál es
                                pass
                        print(f'Has causado un daño de -{impacto_final}')
                        input('Presiona ENTER para continuar... ')
                        features.borrar_pantalla()
                        print(f'Vidas:')
                        print(f'Goblin: {goblin_espada["vida"]}')
                        print(f'Personaje (tú): {personaje["vida"]}')
                        input('Presiona ENTER para continuar... ')
                    else:  # Ataque goblin espada
                        print(f'No has podido atacar, has sacado un {is_impacto_jugador}')
                        is_impacto_goblin = random.randint(0, 20)
                        if is_impacto_goblin >= personaje['defensa'] or is_impacto_goblin == 20:  # Consigue el ataque
                            impacto_final = random.randint(1, goblin_espada['daño'])
                            personaje['vida'] -= impacto_final
                            print('¡Prepárate! El goblin te va a atacar')
                            time.sleep(1)
                            print(f'Te ha causado un daño de -{impacto_final}')
                            input('Presiona ENTER para continuar... ')
                            features.borrar_pantalla()
                            print(f'Vidas:')
                            print(f'Goblin: {goblin_espada["vida"]}')
                            print(f'Personaje (tú): {personaje["vida"]}')
                            input('Presiona ENTER para continuar... ')
                        else:
                            print('¡Has tenido suerte, no ha conseguido impactarte!')
                            input('Presiona ENTER para continuar... ')
                            features.borrar_pantalla()
                            print(f'Vidas:')
                            print(f'Goblin: {goblin_espada["vida"]}')
                            print(f'Personaje (tú): {personaje["vida"]}')
                            input('Presiona ENTER para continuar... ')
            else:
                print(f'El primer enemigo es un goblin con escudo. Tiene {goblin_escudo["vida"]} puntos de vida')
                input('Presiona ENTER para continuar... ')
                while goblin_escudo['vida'] > 0 or personaje['vida'] > 0:  # Mientras que ninguno de los 2 muera...
                    # Consumición de la poción de vida
                    try:
                        is_pocion = equipo['poción de vida']['cantidad']
                        if is_pocion > 0:
                            run = True
                            while run:
                                print(f'Tienes {personaje["vida"]} puntos de vida y {is_pocion} pociones guardadas')
                                usar_pocion = input('¿Quieres consumir una de tus pociones? [s/n]: ')
                                if usar_pocion.lower() == 's':
                                    print(f'Ten en cuenta que la poción de vida regenera {equipo["poción de vida"]["vida"]} puntos de vida como mínimo')
                                    while True:
                                        cantidad = int(input('¿Cuántas quieres consumir?: '))
                                        if 0 <= cantidad <= is_pocion:
                                            for veces in range(cantidad):
                                                posible_vida = random.randint(0, 6)
                                                personaje['vida'] += posible_vida + equipo['poción de vida']['vida']
                                            equipo['poción de vida']['cantidad'] -= cantidad
                                            run = False
                                            break
                                        else:
                                            features.borrar_pantalla()
                                            print('Algo ha ido mal, repita el proceso por favor')
                                            continue
                                elif usar_pocion.lower() == 'n':
                                    break
                                else:
                                    features.borrar_pantalla()
                                    print('Algo ha ido mal, repita el proceso por favor')
                                    continue
                    except KeyError:
                        pass
                    # Intenta atacar el jugador
                    is_impacto_jugador = random.randint(0, 20)
                    if goblin_escudo['vida'] <= 0:
                        conteo_goblins -= 1  # Goblin muerto, uno menos
                        print(f'¡Enhorabuena, has acabado con un goblin con escudo! Faltan {conteo_goblins}')
                        input('Presiona ENTER para continuar... ')
                        # Loot de goblin muerto
                        muerte_goblin(personaje, bolsillo, 'escudo', conteo_goblins)
                        break
                    elif personaje['vida'] <= 0:
                        features.borrar_pantalla()
                        print('Te has muerto')
                        time.sleep(3)
                        exit()
                    elif is_impacto_jugador >= goblin_escudo['defensa']:  # Consigue el ataque
                        time.sleep(3)
                        print('¡Perfecto! Has conseguido impactar')
                        for item in equipo:  # Identificar el arma que va a usar
                            try:
                                equipo[item]['arma']
                                impacto_final = random.randint(1, equipo[item]['daño']) + personaje['daño']
                                goblin_escudo['vida'] -= impacto_final
                            except KeyError:  # Si al principio se encuentra con el escudo, vuelve a ver cuál es el arma
                                pass
                        print(f'Has causado un daño de -{impacto_final}')
                        input('Presiona ENTER para continuar... ')
                        features.borrar_pantalla()
                        print(f'Vidas:')
                        print(f'Goblin: {goblin_escudo["vida"]}')
                        print(f'Personaje (tú): {personaje["vida"]}')
                        input('Presiona ENTER para continuar... ')
                    else:  # Ataque goblin escudo
                        print(f'No has podido atacar, has sacado un {is_impacto_jugador}')
                        is_impacto_goblin = random.randint(0, 20)
                        if is_impacto_goblin >= personaje['defensa'] or is_impacto_goblin == 20:  # Consigue el ataque
                            impacto_final = random.randint(1, goblin_escudo['daño'])
                            personaje['vida'] -= impacto_final
                            print('¡Prepárate! El goblin te va a atacar')
                            time.sleep(1)
                            print(f'Te ha causado un daño de -{impacto_final}')
                            input('Presiona ENTER para continuar... ')
                            features.borrar_pantalla()
                            print(f'Vidas:')
                            print(f'Goblin: {goblin_escudo["vida"]}')
                            print(f'Personaje (tú): {personaje["vida"]}')
                            input('Presiona ENTER para continuar... ')
                        else:
                            print('¡Has tenido suerte, no ha conseguido impactarte!')
                            input('Presiona ENTER para continuar... ')
                            features.borrar_pantalla()
                            print(f'Vidas:')
                            print(f'Goblin: {goblin_espada["vida"]}')
                            print(f'Personaje (tú): {personaje["vida"]}')
                            input('Presiona ENTER para continuar... ')
        else:  # Puedes huir desde el principio
            while True:  # Oportunidad de huir. Solo 1 vez por cada goblin
                oportunidad_huir = input('Puedes probar a huir, ¿lo intentas? [s/n]: ')
                if oportunidad_huir.lower() == 's':
                    no_combate = huir(len(tipo_goblin), False)
                    if no_combate:
                        return personaje, equipo, bolsillo, tipo_goblin  # Puedes huir
                    else:
                        break  # No puedes huir
                elif oportunidad_huir.lower() == 'n':
                    break
                else:
                    features.borrar_pantalla()
                    print('Algo ha ido mal, repita el proceso por favor')
                    continue
            if tipo_goblin[goblin] == 'espada':
                print(f'El siguiente enemigo es un goblin con espada. Tiene {goblin_espada["vida"]} puntos de vida')
                input('Presiona ENTER para continuar... ')
                while goblin_espada['vida'] > 0 or personaje['vida'] > 0:  # Mientras que ninguno de los 2 muera...
                    # Consumición de la poción de vida
                    try:
                        is_pocion = equipo['poción de vida']['cantidad']
                        if is_pocion > 0:
                            run = True
                            while run:
                                print(f'Tienes {personaje["vida"]} puntos de vida y {is_pocion} pociones guardadas')
                                usar_pocion = input('¿Quieres consumir una de tus pociones? [s/n]: ')
                                if usar_pocion.lower() == 's':
                                    print(f'Ten en cuenta que la poción de vida regenera {equipo["poción de vida"]["vida"]} puntos de vida como mínimo')
                                    while True:
                                        cantidad = int(input('¿Cuántas quieres consumir?: '))
                                        if 0 <= cantidad <= is_pocion:
                                            for veces in range(cantidad):
                                                posible_vida = random.randint(0, 6)
                                                personaje['vida'] += posible_vida + equipo['poción de vida']['vida']
                                            equipo['poción de vida']['cantidad'] -= cantidad
                                            run = False
                                            break
                                        else:
                                            features.borrar_pantalla()
                                            print('Algo ha ido mal, repita el proceso por favor')
                                            continue
                                elif usar_pocion.lower() == 'n':
                                    break
                                else:
                                    features.borrar_pantalla()
                                    print('Algo ha ido mal, repita el proceso por favor')
                                    continue
                    except KeyError:
                        pass
                    # Intenta atacar el jugador
                    is_impacto_jugador = random.randint(0, 20)
                    if goblin_espada['vida'] <= 0:
                        conteo_goblins -= 1  # Goblin muerto, uno menos
                        print(f'¡Enhorabuena, has acabado con un goblin con espada! Faltan {conteo_goblins}')
                        input('Presiona ENTER para continuar... ')
                        # Loot de goblin muerto
                        muerte_goblin(personaje, bolsillo, 'espada', conteo_goblins)
                        break  # Termina después de regresar el loot correspondiente
                    elif personaje['vida'] <= 0:
                        features.borrar_pantalla()
                        print('Te has muerto')
                        time.sleep(3)
                        exit()
                    elif is_impacto_jugador >= goblin_espada['defensa']:  # Consigue el ataque
                        time.sleep(3)
                        print('¡Perfecto! Has conseguido impactar')
                        for item in equipo:  # Identificar el arma que va a usar
                            try:
                                equipo[item]['arma']
                                impacto_final = random.randint(1, equipo[item]['daño']) + personaje['daño']
                                goblin_espada['vida'] -= impacto_final
                            except KeyError:  # Si al principio se encuentra con el escudo, vuelve a ver cuál es el arma
                                pass
                        print(f'Has causado un daño de -{impacto_final}')
                        input('Presiona ENTER para continuar... ')
                        features.borrar_pantalla()
                        print(f'Vidas:')
                        print(f'Goblin: {goblin_espada["vida"]}')
                        print(f'Personaje (tú): {personaje["vida"]}')
                        input('Presiona ENTER para continuar... ')
                    else:  # Ataque goblin espada
                        print(f'No has podido atacar, has sacado un {is_impacto_jugador}')
                        is_impacto_goblin = random.randint(0, 20)
                        if is_impacto_goblin >= personaje['defensa'] or is_impacto_goblin == 20:  # Consigue el ataque
                            impacto_final = random.randint(1, goblin_espada['daño'])
                            personaje['vida'] -= impacto_final
                            print('¡Prepárate! El goblin te va a atacar')
                            time.sleep(1)
                            print(f'Te ha causado un daño de -{impacto_final}')
                            input('Presiona ENTER para continuar... ')
                            features.borrar_pantalla()
                            print(f'Vidas:')
                            print(f'Goblin: {goblin_espada["vida"]}')
                            print(f'Personaje (tú): {personaje["vida"]}')
                            input('Presiona ENTER para continuar... ')
                        else:
                            print('¡Has tenido suerte, no ha conseguido impactarte!')
                            input('Presiona ENTER para continuar... ')
                            features.borrar_pantalla()
                            print(f'Vidas:')
                            print(f'Goblin: {goblin_espada["vida"]}')
                            print(f'Personaje (tú): {personaje["vida"]}')
                            input('Presiona ENTER para continuar... ')
            else:
                print(f'El primer enemigo es un goblin con escudo. Tiene {goblin_escudo["vida"]} puntos de vida')
                input('Presiona ENTER para continuar... ')
                while goblin_escudo['vida'] > 0 or personaje['vida'] > 0:  # Mientras que ninguno de los 2 muera...
                    # Consumición de la poción de vida
                    try:
                        is_pocion = equipo['poción de vida']['cantidad']
                        if is_pocion > 0:
                            run = True
                            while run:
                                print(f'Tienes {personaje["vida"]} puntos de vida y {is_pocion} pociones guardadas')
                                usar_pocion = input('¿Quieres consumir una de tus pociones? [s/n]: ')
                                if usar_pocion.lower() == 's':
                                    print(f'Ten en cuenta que la poción de vida regenera {equipo["poción de vida"]["vida"]} puntos de vida como mínimo')
                                    while True:
                                        cantidad = int(input('¿Cuántas quieres consumir?: '))
                                        if 0 <= cantidad <= is_pocion:
                                            for veces in range(cantidad):
                                                posible_vida = random.randint(0, 6)
                                                personaje['vida'] += posible_vida + equipo['poción de vida']['vida']
                                            equipo['poción de vida']['cantidad'] -= cantidad
                                            run = False
                                            break
                                        else:
                                            features.borrar_pantalla()
                                            print('Algo ha ido mal, repita el proceso por favor')
                                            continue
                                elif usar_pocion.lower() == 'n':
                                    break
                                else:
                                    features.borrar_pantalla()
                                    print('Algo ha ido mal, repita el proceso por favor')
                                    continue
                    except KeyError:
                        pass
                    # Intenta atacar el jugador
                    is_impacto_jugador = random.randint(0, 20)
                    if goblin_escudo['vida'] <= 0:
                        conteo_goblins -= 1  # Goblin muerto, uno menos
                        print(f'¡Enhorabuena, has acabado con un goblin con escudo! Faltan {conteo_goblins}')
                        input('Presiona ENTER para continuar... ')
                        # Loot de goblin muerto
                        muerte_goblin(personaje, bolsillo, 'escudo', conteo_goblins)
                        break
                    elif personaje['vida'] <= 0:
                        features.borrar_pantalla()
                        print('Te has muerto')
                        time.sleep(3)
                        exit()
                    elif is_impacto_jugador >= goblin_escudo['defensa']:  # Consigue el ataque
                        time.sleep(3)
                        print('¡Perfecto! Has conseguido impactar')
                        for item in equipo:  # Identificar el arma que va a usar
                            try:
                                equipo[item]['arma']
                                impacto_final = random.randint(1, equipo[item]['daño']) + personaje['daño']
                                goblin_escudo['vida'] -= impacto_final
                            except KeyError:  # Si al principio se encuentra con el escudo, vuelve a ver cuál es el arma
                                pass
                        print(f'Has causado un daño de -{impacto_final}')
                        input('Presiona ENTER para continuar... ')
                        features.borrar_pantalla()
                        print(f'Vidas:')
                        print(f'Goblin: {goblin_escudo["vida"]}')
                        print(f'Personaje (tú): {personaje["vida"]}')
                        input('Presiona ENTER para continuar... ')
                    else:  # Ataque goblin escudo
                        print(f'No has podido atacar, has sacado un {is_impacto_jugador}')
                        is_impacto_goblin = random.randint(0, 20)
                        if is_impacto_goblin >= personaje['defensa'] or is_impacto_goblin == 20:  # Consigue el ataque
                            impacto_final = random.randint(1, goblin_escudo['daño'])
                            personaje['vida'] -= impacto_final
                            print('¡Prepárate! El goblin te va a atacar')
                            time.sleep(1)
                            print(f'Te ha causado un daño de -{impacto_final}')
                            input('Presiona ENTER para continuar... ')
                            features.borrar_pantalla()
                            print(f'Vidas:')
                            print(f'Goblin: {goblin_escudo["vida"]}')
                            print(f'Personaje (tú): {personaje["vida"]}')
                            input('Presiona ENTER para continuar... ')
                        else:
                            print('¡Has tenido suerte, no ha conseguido impactarte!')
                            input('Presiona ENTER para continuar... ')
                            features.borrar_pantalla()
                            print(f'Vidas:')
                            print(f'Goblin: {goblin_espada["vida"]}')
                            print(f'Personaje (tú): {personaje["vida"]}')
                            input('Presiona ENTER para continuar... ')
    print('¡Has acabado con todos los goblins de la cueva!')
    muerte_goblin(personaje, bolsillo, 'escudo', conteo_goblins, True)
    return bolsillo, personaje


def combate_goblin(personaje, habilidades, mochila, bolsillo):
    # Generar enemigos (num y clase)
    features.borrar_pantalla()
    num_enemigos = random.randint(1, 6)
    clase = ['espada', 'escudo']
    clase_enemigo = []
    if num_enemigos == 1:
        print(f'¡Cuidado! Hay {num_enemigos} enemigo dentro de la cueva')
    else:
        print(f'¡Cuidado! Hay {num_enemigos} enemigos dentro de la cueva')
    for enemigo in range(num_enemigos):
        tipo_clase = random.choice(clase)
        print(f'{enemigo + 1}. Goblin con {tipo_clase}')
        clase_enemigo.append(tipo_clase)
    num_escudo = clase_enemigo.count('escudo')
    num_espada = clase_enemigo.count('espada')
    if num_escudo < num_enemigos or num_espada < num_enemigos:
        print('\n-----  Total  -----')
        print(f'Goblins con espada: {num_espada}')
        print(f'Goblins con escudo: {num_escudo}\n')
    # Oportunidad de huir antes del combate
    while True:
        print('Ten en cuenta que una vez dentro, solo vas a poder tratar de huir 1 vez por goblin')
        lucha = input('¿Quieres huir antes de entrar en combate? [s/n]: ')
        if lucha.lower() == 's':
            salida = huir(num_enemigos)
            if salida:
                return personaje, habilidades, mochila, bolsillo
            else:
                break
        elif lucha.lower() == 'n':
            break
        else:
            print('Algo ha ido mal, repita el proceso por favor')
            continue
    # Combate
    preparacion = pre_combate(mochila, habilidades, personaje)
    pelea = combate(personaje, preparacion[0], bolsillo, clase_enemigo)
    return personaje, habilidades, mochila, bolsillo


