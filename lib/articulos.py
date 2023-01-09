# Funciones
def arma(tipo):
    if tipo.lower() == 'espada':
        precio = 10
        return {'espada': {'daño': 8, 'precio': precio, 'venta': precio * 0.5, 'manos': 1, 'arma': True, 'cantidad': 1}}
    elif tipo.lower() == 'puños' or tipo.lower() == 'puño':
        return {'puños': {'daño': 4, 'manos': 1, 'arma': True}}
    elif tipo.lower() == 'espada goblin':
        return {'espada goblin': {'daño': 6, 'precio': None, 'venta': 5, 'manos': 1, 'arma': True, 'cantidad': 1}}
    elif tipo.lower() == 'espada mágica':
        precio_espada_magica = 200
        return {'espada mágica': {'daño': 6, 'precio': precio_espada_magica, 'venta': precio_espada_magica * 0.5, 'manos': 1, 'arma': True}}
    elif tipo.lower() == 'hacha dos manos':
        precio_hacha = 30
        return {'hacha dos manos': {'daño': 12, 'precio': precio_hacha, 'venta': precio_hacha * 0.5, 'manos': 2, 'arma': True}}


def proteccion(tipo):
    if tipo.lower() == 'escudo':
        precio = 10
        return {'escudo': {'precio': precio, 'venta': precio * 0.5, 'destreza': 1, 'protección': True, 'cantidad': 1}}
    elif tipo.lower() == 'escudo goblin':
        return {'escudo goblin': {'precio': None, 'venta': 5, 'destreza': 1, 'protección': True, 'cantidad': 1}}
    elif tipo.lower() == 'armadura nivel 1':
        precio_arm_uno = 30
        return {'escudo goblin': {'precio': precio_arm_uno, 'venta': precio_arm_uno * 0.5, 'destreza': 2, 'protección': True, 'cantidad': 1}}
    elif tipo.lower() == 'armadura nivel 2':
        precio_arm_dos = 40
        return {'armadura nivel 2': {'precio': precio_arm_dos, 'venta': precio_arm_dos * 0.5, 'destreza': 3, 'protección': True, 'cantidad': 1}}
    elif tipo.lower() == 'armadura nivel 3':
        precio_arm_tres = 50
        return {'armadura nivel 3': {'precio': precio_arm_tres, 'venta': precio_arm_tres * 0.5, 'destreza': 4, 'protección': True, 'cantidad': 1}}


def pocion(tipo):
    if tipo.lower() == 'poción de vida':
        precio_pocion = 20
        return {'poción de vida': {'precio': precio_pocion, 'venta': precio_pocion * 0.5, 'vida': 2, 'pocion': True, 'cantidad': 1}}
