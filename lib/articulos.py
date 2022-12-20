# Archivo susceptible de edición
import random


def arma(tipo):
    if tipo == 'espada':
        dano = random.randint(0, 8)
        precio = 10
        return {'espada': {'daño': dano, 'precio': precio, 'venta': precio * 0.8}}


def pocion():
    pass


def clase(articulo):
    arma = ['espada', 'escudo']
    pocion = ['vida']
    if articulo in arma:
        return 'arma'
    else:
        return 'pocion'