import articulos


def comparar(diccionario, atributo):
    # Explicación:      ----    Función que compara los valores del atributo seleccionado
    # diccionario       ----    Diccionario
    # from_key          ----    Cuál es la palabra clave desde dónde buscar
    # atributo          ----    Atributo a buscar de la palabra clave
    # extrae_valor      ----    True = extrae valor; False = muestra una lista de los items con el atributo seleccionado
    # Desarrollo:
    lista_keys = list(diccionario.keys())
    lista_values = list(diccionario.values())
    for items, num in zip(lista_keys, range(len(lista_keys))):
        print(f'- {items} | {lista_values[num].get(atributo)}')


def intercambiar(diccionario_1, diccionario_2, elemento, valor):
    # Explicación   ----    Función que intercambia de un diccionario (1) a otro (2) un elemento. Tengo 3 pociones de vidas (elemento) en el inventario (1) y quiero pasar una (valor) a mi mochila (2)
    if valor < 0 or valor > diccionario_1[elemento]['cantidad']:
        return False
    elif valor == diccionario_1[elemento]['cantidad']:
        diccionario_1.pop(elemento)
        diccionario_2[elemento]['cantidad'] += valor
        return diccionario_1, diccionario_2
    else:
        diccionario_1[elemento]['cantidad'] -= valor
        diccionario_2[elemento]['cantidad'] += valor
        return diccionario_1, diccionario_2


def nuevo(diccionario, from_key):
    # Explicación   ----    Función que añade nuevos atributos a un diccionario. Soporta errores de existencias
    # diccionario   ----    Diccionario de origen
    # from_key      ----    Cuál es la palabra clave desde dónde buscar
    # Desarrollo
    try:
        diccionario[from_key]
        run = True
        while run:
            alternativa = input('Este artículo ya existe. ¿Quieres añadir una nueva cantidad? [s/n]: ')
            if alternativa.lower() == 's':
                diccionario[from_key]['cantidad'] += 1
                return diccionario
            elif alternativa.lower() == 'n':
                return diccionario
            else:
                while True:
                    opc = input('Ha habido un error. ¿Quieres repetir o salir? [r/s]: ')
                    if opc.lower() == 'r':
                        break
                    elif opc.lower() == 's':
                        return diccionario
                    else:
                        continue
    except KeyError:
        estado = articulos.clase(from_key)
        if estado == 'arma':
            diccionario.update(articulos.arma(from_key))
        else:  # Única otra opción es que sea poción porque no hay más
            diccionario.update(articulos.pocion(from_key))
        diccionario[from_key]['cantidad'] = 1
        return diccionario