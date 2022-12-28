# Archivo susceptible de edición
import random


def arma(tipo):
    if tipo == 'espada':
        dano_arma = random.randint(0, 8)
        precio = 10
        return {'espada': {'daño': dano_arma, 'precio': precio, 'venta': precio * 0.8}}
    elif tipo == 'puños' or tipo == 'puño':
        dano_arma = random.randint(0, 4)
        precio = 0
        return {'puños': {'daño': dano_arma, 'precio': precio, 'venta': precio * 0.8}}


def pocion():
    pass


def clase(articulo):
    arma = ['espada', 'escudo']
    pocion = ['vida']
    if articulo in arma:
        return 'arma'
    else:
        return 'pocion'