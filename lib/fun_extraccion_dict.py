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


inventario = {'arma':{'puño':0},'pociones':{'poc_salud':2},'armadura':0,'armas':{'espada':2,'hacha':4},'armaduras':{}}

