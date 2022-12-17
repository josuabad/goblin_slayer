def extraccion_dict(diccionario, ext_key):
    lista_keys = diccionario.keys()
    lista_keys = list(lista_keys)
    lista_values = diccionario.values()
    lista_values = list(lista_values)
    for items, num in zip(lista_keys, range(len(lista_keys))):
        print(f'- {items} | ({lista_values[num].get(ext_key)})')