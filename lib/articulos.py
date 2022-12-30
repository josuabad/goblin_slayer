# Archivo susceptible de edición
import random


def arma(tipo):
    if tipo == 'espada':
        precio = 10
        return {'espada': {'daño': 8, 'precio': precio, 'venta': precio * 0.8}}
    elif tipo == 'puños' or tipo == 'puño':
        return {'puños': {'daño': 4}}


def pocion():
    pass


def clase(articulo):
    arma = ['espada', 'escudo']
    pocion = ['vida']
    if articulo in arma:
        return 'arma'
    else:
        return 'pocion'