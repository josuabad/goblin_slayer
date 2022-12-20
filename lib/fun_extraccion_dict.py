def extraer(diccionario, from_key, atributo, extrae_valor=True):
    # Explicación:
    # diccionario       ----    Diccionario
    # from_key          ----    Cuál es la palabra clave desde dónde buscar
    # atributo          ----    Atributo a buscar de la palabra clave
    # extrae_valor      ----    True = extrae valor; False = muestra una lista de los items con el atributo seleccionado
    # Desarrollo:
    lista_keys = list(diccionario.keys())
    lista_values = list(diccionario.values())
    if extrae_valor:
        return lista_values[lista_keys.index(from_key)].get(atributo)
    else:
        for items, num in zip(lista_keys, range(len(lista_keys))):
            print(f'- {items} | ({lista_values[num].get(atributo)})')


def intercambiar(diccionario_emisor, from_key, atributo, valor_de_cambio, diccionario_receptor):  # La función cambia valores (True), pero también puede modificarlos de un diccionario a otro (False)(Ejemplo: de mochila a inventario)
    # Explicación:
    # diccionario_emisor       ----    Diccionario de origen
    # from_key                 ----    Cuál es la palabra clave desde dónde buscar
    # atributo                 ----    Atributo a buscar de la palabra clave
    # valor_de_cambio          ----    Nuevo valor a guardar en el diccionario final
    # diccionario_receptor     ----    Diccionario de destino
    # Base:
    # Quiero saber los atributos de un from_key que no se dónde se encuentra.
    diccionario_emisor_view_keys = list(diccionario_emisor.keys())
    diccionario_emisor_view_values = list(diccionario_emisor.values())
    # Tengo que saber dónde está para preguntarle cositas
    donde_encontrar = diccionario_emisor_view_keys.index(from_key)
    # Ahora quiero saber los atributos del from_key.
    donde_buscar = list(diccionario_emisor_view_values[donde_encontrar].keys())
    # Pero no se donde tengo que cambiar
    donde_cambiar = donde_buscar.index(atributo)
    # Y, como los quiero manipular, pongo como una lista los valores que tengo que cambiar
    que_cambiar = list(diccionario_emisor_view_values[donde_encontrar].values())
    # Desarrollo:
    valor_de_origen = extraer(diccionario_emisor, from_key, atributo)
    if valor_de_cambio == valor_de_origen:
        diccionario_receptor.update({from_key: {donde_buscar[donde_cambiar]: valor_de_cambio}})
        donde_buscar.pop(donde_cambiar)
        que_cambiar.pop(donde_cambiar)
        for elmnt in donde_buscar:
            diccionario_receptor[from_key][elmnt] = que_cambiar[donde_buscar.index(elmnt)]
        diccionario_emisor.pop(from_key)
        return diccionario_emisor, diccionario_receptor
    elif valor_de_cambio < valor_de_origen and valor_de_cambio > 0:
        # 1º Cambiar el atributo           
        diccionario_receptor.update({from_key: {atributo: valor_de_cambio}})
        # diccionario_receptor[from_key][atributo] = valor_de_cambio
        # 2º Pasar el resto de atributos
        donde_buscar.pop(donde_cambiar)
        que_cambiar.pop(donde_cambiar)
        for elmnt in donde_buscar:
            diccionario_receptor[from_key][elmnt] = que_cambiar[donde_buscar.index(elmnt)]
        # 3º Borrar el sobrante del anterior
        diccionario_emisor[from_key][atributo] = valor_de_origen - valor_de_cambio
        # diccionario_emisor.update({from_key: {atributo: valor_de_origen - valor_de_cambio}})
        return diccionario_emisor, diccionario_receptor
    else:
        return False  # Hay que volver a perdir desde le sistema principal una opción válida


def modificar(diccionario, from_key, atributo, valor_de_cambio, tipo_operacion='modificar'):
    # Explicación:
    # diccionario              ----    Diccionario de origen
    # from_key                 ----    Cuál es la palabra clave desde dónde buscar
    # atributo                 ----    Atributo a buscar de la palabra clave
    # valor_de_cambio          ----    Nuevo valor a guardar en el diccionario final
    # tipo_operacion           ----    Si modificar: solo modifica el valo por el nuevo; Si no modificar, entonces suma/resta/multiplica/divide el valor de origen con el nuevo
    # Desarrollo:
    if tipo_operacion != 'modificar':
        valor_de_origen = extraer(diccionario, from_key, atributo)
        if tipo_operacion == 'sumar':
            diccionario[from_key][atributo] = valor_de_origen + valor_de_cambio
            return diccionario
        elif tipo_operacion == 'restar':
            diccionario[from_key][atributo] = valor_de_origen - valor_de_cambio
            return diccionario
        elif tipo_operacion == 'multiplicar':
            diccionario[from_key][atributo] = valor_de_origen * valor_de_cambio
            return diccionario
        elif tipo_operacion == 'dividir':
            diccionario[from_key][atributo] = valor_de_origen / valor_de_cambio
            return diccionario
    else:
        diccionario[from_key][atributo] = valor_de_cambio
        return diccionario


def nuevo(diccionario, from_key):
    """
    Casos:
    - No existe este elemento dentro del diccionario
        - Contar el número de atributos que puede tener ese elemento
        - Añadir cada atributo y su correspondiente valor. Sin contar la cantidad.
        - Añadir la cantidad de elementos, pueden haber varias pócimas en el bolsillo (por ejemplo)
    - Existe el elemento dentro del diccionario
        - Mensaje de, ya tienes este elemento en el diccionario, quieres guardarlo (sumar cantidad)?
    """
    pass