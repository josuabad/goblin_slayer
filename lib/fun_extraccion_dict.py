def extraer(diccionario, from_key, extrae_value_key, extrae_valor=True):
    lista_keys = list(diccionario.keys())
    lista_values = list(diccionario.values())
    if extrae_valor:
        return lista_values[lista_keys.index(from_key)].get(extrae_value_key)
    else:
        for items, num in zip(lista_keys, range(len(lista_keys))):
            print(f'- {items} | ({lista_values[num].get(extrae_value_key)})')
