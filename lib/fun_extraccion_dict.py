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


def modificar(diccionario_emisor, from_key, atributo, valor_de_cambio, diccionario_receptor=False, cambiar=False):  # La función cambia valores (True), pero también puede modificarlos de un diccionario a otro (False)(Ejemplo: de mochila a inventario)
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
    if cambiar:
        diccionario_emisor[from_key][atributo] = valor_de_cambio
        return diccionario_emisor
    else:
        if valor_de_cambio == valor_de_origen:
            diccionario_receptor.update({diccionario_emisor_view_keys[donde_encontrar]: {donde_buscar[donde_cambiar]: valor_de_cambio}})
            donde_buscar.pop(donde_cambiar)
            que_cambiar.pop(donde_cambiar)
            for elmnt in donde_buscar:
                diccionario_receptor[diccionario_emisor_view_keys[donde_encontrar]][elmnt] = que_cambiar[donde_buscar.index(elmnt)]
            diccionario_emisor.pop(from_key)
            return diccionario_emisor, diccionario_receptor
        elif valor_de_cambio < valor_de_origen and valor_de_cambio > 0:
            # 1º Cambiar el atributo           
            diccionario_receptor.update({diccionario_emisor_view_keys[donde_encontrar]: {donde_buscar[donde_cambiar]: valor_de_cambio}})
            # 2º Pasar el resto de atributos
            donde_buscar.pop(donde_cambiar)
            que_cambiar.pop(donde_cambiar)
            for elmnt in donde_buscar:
                diccionario_receptor[diccionario_emisor_view_keys[donde_encontrar]][elmnt] = que_cambiar[donde_buscar.index(elmnt)]
            # 3º Borrar el sobrante del anterior
            diccionario_emisor[from_key][atributo] = valor_de_origen - valor_de_cambio
            # diccionario_emisor.update({diccionario_emisor_view_keys[donde_encontrar]: {atributo: valor_de_origen - valor_de_cambio}})
            return diccionario_emisor, diccionario_receptor
        else:
            return False  # Hay que volver a perdir desde le sistema principal una opción válida