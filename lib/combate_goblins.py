import random
import config_habilidades
import features
import articulos


def huir(num, inicio=True):
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
    porcentaje = [True, True, True, True, False, False, False, False, False, False]
    is_moneda = random.choice(porcentaje)
    if is_moneda:
        cantidad = random.randint(1, 6)
        return cantidad
    else:
        return False


def recuperar_extras(goblin):
    porcentaje = [True, True, False, False, False, False, False, False, False, False]
    is_recuperar = random.choice(porcentaje)
    if is_recuperar:
        if goblin == 'espada':
            return articulos.arma('espada goblin')
        else:
            return articulos.proteccion('escudo goblin')
    else:
        return False


def muerte_goblin(personaje, bolsillo, tipo, num, total=False):
    if tipo == 'espada':
        nuevo = recuperar_extras('espada')
        if nuevo != False:
            bolsillo.update(nuevo)
    else:
        nuevo = recuperar_extras('escudo')
        if nuevo != False:
            bolsillo.update(nuevo)
    moneda = monedas()
    if moneda != False:
        bolsillo.update(moneda)
    if total:
        bonus = 2 * num
        personaje['experiencia'] += bonus
    personaje['experiencia'] += 20
    return personaje, bolsillo


def pre_combate(mochila, habilidades, personaje):
    armas = []
    escudos = []
    arma_en_uso = {}
    manos = 2
    num = 0
    print('Armas disponibles')
    for item in mochila:  # Desplegable de armas
        try:
            mochila[item]['arma']
            num_manos = mochila[item]['manos']
            num += 1
            print(f'  {num}. {item} | {num_manos} manos')
            armas.append(item)
        except KeyError:
            escudos.append(item)
    while True:  # Saber que arma coger y si me quedan las manos libres para usar mi escudo
        arma_eleccion = int(input('Introduce el número del arma que quieres coger: '))
        if arma_eleccion < 1 or arma_eleccion > len(armas) or type(arma_eleccion) != int:
            features.borrar_pantalla()
            print('Algo ha ido mal, repita el proceso por favor')
            continue
        else:
            arma_en_uso.update(articulos.arma(armas[arma_eleccion - 1]))
            print(f'Has escogido: {armas[arma_eleccion - 1]}')
            break
    manos = 2 - arma_en_uso[armas[arma_eleccion - 1]]['manos']
    while True:
        if manos == 1 and len(escudos) != 0:
            print('Tienes una mano libre con la que puedes coger un escudo')
            usar_escudo = input('¿Quieres equiparte tu escudo?: [s/n]: ')
            if usar_escudo.lower() == 's':
                arma_en_uso.update(articulos.proteccion(escudos[0]))
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
    return mochila, habilidades, personaje


def combate(personaje, equipo, bolsillo, tipo_goblin):  # Recordar que "goblin" es una lista con todos los goblins que hay dentro de la cueva
    goblin_escudo = {'vida': 8, 'daño': 8, 'defensa': 13}
    goblin_espada = {'vida': 8, 'daño': 6, 'defensa': 12}
    conteo_goblins = len(tipo_goblin)
    for goblin in range(conteo_goblins):
        if goblin == 0:  # No puedes huir
            if tipo_goblin[goblin] == 'espada':
                while goblin_espada['vida'] > 0 or personaje['vida'] > 0:
                    # Ataque jugador
                    is_impacto_jugador = random.randint(0, 20)
                    if is_impacto_jugador >= goblin_espada['defensa']:  # Ataque
                        # Identificar el arma
                        for item in equipo:
                            try:
                                equipo[item]['arma']
                                impacto_final = random.randint(1, equipo[item]['daño']) + personaje['daño']
                                goblin_espada['vida'] -= impacto_final
                            except KeyError:
                                pass
                        if goblin_espada['vida'] <= 0:
                            conteo_goblins -= 1
                            print(f'¡Enhorabuena, has acabado con un goblin con espada! Faltan {conteo_goblins}')
                    else:  # Defensa
                        is_impacto_goblin = random.randint(0, 20)
                        if is_impacto_goblin >= personaje['defensa']:
                            impacto_final = random.randint(1, goblin_espada['daño'])
                            personaje['vida'] -= impacto_final
                        else:
                            print('¡Has tenido suerte, no ha conseguido impactarte!')
                        if personaje['vida'] <= 0:
                            features.borrar_pantalla()
                            print('Te has muerto')
                            exit()
            else:
                while goblin_escudo['vida'] > 0 or personaje['vida'] > 0: 
                    # Ataque jugador
                    is_impacto_jugador = random.randint(0, 20)
                    if is_impacto_jugador >= goblin_escudo['defensa']:  # Ataque
                        # Identificar el arma
                        for item in equipo:
                            try:
                                equipo[item]['arma']
                                impacto_final = random.randint(1, equipo[item]['daño']) + personaje['daño']
                                goblin_escudo['vida'] -= impacto_final
                            except KeyError:
                                pass
                        if goblin_espada['vida'] <= 0:
                            conteo_goblins -= 1
                            print(f'¡Enhorabuena, has acabado con un goblin con espada! Faltan {conteo_goblins}')
                    else:  # Defensa
                        is_impacto_goblin = random.randint(0, 20)
                        if is_impacto_goblin >= personaje['defensa']:
                            impacto_final = random.randint(1, goblin_escudo['daño'])
                            personaje['vida'] -= impacto_final
                        else:
                            print('¡Has tenido suerte, no ha conseguido impactarte!')
                            if personaje['vida'] <= 0:
                                features.borrar_pantalla()
                                print('Te has muerto')
                                exit()
        else:  # Puedes huir
            if tipo_goblin[goblin] == 'espada':
                while goblin_espada['vida'] > 0 or personaje['vida'] > 0:
                    while True:
                        oportunidad_huir = input('Puedes probar a huir, ¿lo intentas? [s/n]: ')
                        if oportunidad_huir.lower() == 's':
                            no_combate = combate_goblins.huir(len(tipo_goblin), False)
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
                    # Ataque jugador
                    is_impacto_jugador = random.randint(0, 20)
                    if is_impacto_jugador >= goblin_espada['defensa']:  # Ataque
                        # Identificar el arma
                        for item in equipo:
                            try:
                                equipo[item]['arma']
                                impacto_final = random.randint(1, equipo[item]['daño']) + personaje['daño']
                                goblin_espada['vida'] -= impacto_final
                            except KeyError:
                                pass
                        if goblin_espada['vida'] <= 0:
                            conteo_goblins -= 1
                            print(f'¡Enhorabuena, has acabado con un goblin con espada! Faltan {conteo_goblins}')
                    else:  # Defensa
                        is_impacto_goblin = random.randint(0, 20)
                        if is_impacto_goblin >= personaje['defensa']:
                            impacto_final = random.randint(1, goblin_espada['daño'])
                            personaje['vida'] -= impacto_final
                        else:
                            print('¡Has tenido suerte, no ha conseguido impactarte!')
                        if personaje['vida'] <= 0:
                            features.borrar_pantalla()
                            print('Te has muerto')
                            exit()
            else:
                while goblin_escudo['vida'] > 0 or personaje['vida'] > 0:
                    while True:
                        oportunidad_huir = input('Puedes probar a huir, ¿lo intentas? [s/n]: ')
                        if oportunidad_huir.lower() == 's':
                            no_combate = combate_goblins.huir(len(tipo_goblin), False)
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
                    # Ataque jugador
                    is_impacto_jugador = random.randint(0, 20)
                    if is_impacto_jugador >= goblin_escudo['defensa']:  # Ataque
                        # Identificar el arma
                        for item in equipo:
                            try:
                                equipo[item]['arma']
                                impacto_final = random.randint(1, equipo[item]['daño']) + personaje['daño']
                                goblin_escudo['vida'] -= impacto_final
                            except KeyError:
                                pass
                        if goblin_espada['vida'] <= 0:
                            conteo_goblins -= 1
                            print(f'¡Enhorabuena, has acabado con un goblin con espada! Faltan {conteo_goblins}')
                    else:  # Defensa
                        is_impacto_goblin = random.randint(0, 20)
                        if is_impacto_goblin >= personaje['defensa']:
                            impacto_final = random.randint(1, goblin_escudo['daño'])
                            personaje['vida'] -= impacto_final
                        else:
                            print('¡Has tenido suerte, no ha conseguido impactarte!')
                            if personaje['vida'] <= 0:
                                features.borrar_pantalla()
                                print('Te has muerto')
                                exit()


def combate_goblins(personaje, mochila):
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
        print('-----  Total  -----')
        print(f'Goblins con espada: {num_espada}')
        print(f'Goblins con escudo: {num_escudo}')
    # Oportunidad de huir antes del combate
    while True:
        lucha = input('¿Quieres huir antes de entrar en combate? [s/n]: ')
        if lucha.lower() == 's':
            salida = huir(num_enemigos)
            if salida:
                return personaje, mochila
            else:
                break
        elif lucha.lower() == 'n':
            break
        else:
            print('Algo ha ido mal, repita el proceso por favor')
            continue
    # Combate