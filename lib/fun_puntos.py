def nuevo_punto(diccionario, habilidad, num_puntos, puntos):
    for punto in range(num_puntos):
        if habilidad == 'fuerza':
            if diccionario[habilidad] < 14:
                diccionario[habilidad] += 1
                puntos -= 1
            else:
                print(f'Recuerda que solo puedes añadir hasta 4 puntos en fuerza. Tienes {diccionario[habilidad]}')
                return diccionario, puntos
        elif habilidad == 'destreza':
            diccionario[habilidad] += 1
            puntos -= 1
        elif habilidad == 'constitucion':
            diccionario[habilidad] += 1
            puntos -= 1
    return diccionario, puntos