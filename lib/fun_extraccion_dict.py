def extraer(diccionario, from_key, extrae_value_key, extrae_valor=True):
    # diccionario       ----    Diccionario
    # from_key          ----    Cuál es la palabra clave desde dónde buscar
    # extrae_value_key  ----    Atributo a buscar de la palabra clave
    # extrae_valor      ----    True = extrae valor; False = muestra una lista de los items con el atributo seleccionado
    lista_keys = list(diccionario.keys())
    lista_values = list(diccionario.values())
    if extrae_valor:
        return lista_values[lista_keys.index(from_key)].get(extrae_value_key)
    else:
        for items, num in zip(lista_keys, range(len(lista_keys))):
            print(f'- {items} | ({lista_values[num].get(extrae_value_key)})')


"""
def modificar(diccionario_emisor, diccionario_receptor, from_key, atributo, valor_de_cambio):  # Devuelve el diccionario usado y el modificado
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
    # Desarrollo
    valor_de_origen = extraer(diccionario_emisor, from_key, atributo)
    if valor_de_cambio < valor_de_origen and valor_de_cambio > 0:  # Caso 1
        diccionario_receptor.update({diccionario_emisor_view_keys[donde_encontrar]: {donde_buscar[donde_cambiar]: valor_de_cambio}})  # 1º Metes en el inventario todo lo que quieres valor_de_cambio
        # Pasar todos los atributos restantes del from_key
        donde_buscar.pop(donde_cambiar)
        que_cambiar.pop(donde_cambiar)
        for elmnt in donde_buscar:
            diccionario_receptor[diccionario_emisor_view_keys[donde_encontrar]][elmnt] = que_cambiar[donde_buscar.index(elmnt)]
        # Borrar el sobrante de la diccionario_emisor
        # cantidad_original = extraer(diccionario_emisor, 'espada', 'cantidad')
        diccionario_emisor[diccionario_emisor_view_keys[donde_encontrar]]['cantidad'] = cantidad_original - valor_de_cambio
    elif valor_de_cambio == valor_de_origen:  # Caso 2
        diccionario_receptor.update({diccionario_emisor_view_keys[donde_encontrar]: {donde_buscar[donde_cambiar]: valor_de_cambio}})  # 1º Metes en el inventario todo lo que quieres valor_de_cambio
    else:  # Caso 3. Se podría usar un try/except
        pass
"""