import random
import features


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


def combate_goblins():
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
    while True:
        lucha = input('¿Quieres huir antes de entrar en combate? [s/n]: ')
        if lucha.lower() == 's':
            salida = huir(num_enemigos)
            if salida:
                return  # Tiene que devolver algo que sea lo mismo que se le mete a la función
            else:
                break
        elif lucha.lower() == 'n':
            break
        else:
            print('Algo ha ido mal, repita el proceso por favor')
            continue