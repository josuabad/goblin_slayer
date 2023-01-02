# Archivo susceptible de edición
import random


def arma(tipo):
    if tipo.lower() == 'espada':
        precio = 10
        return {'espada': {'daño': 8, 'precio': precio, 'venta': precio * 0.8, 'manos': 1, 'arma': True}}
    elif tipo.lower() == 'puños' or tipo.lower() == 'puño':
        return {'puños': {'daño': 4, 'manos': 1, 'arma': True}}
    elif tipo.lower() == 'espada goblin':
        return {'espada goblin': {'daño': 6, 'precio': None, 'venta': 5, 'manos': 1, 'arma': True}}


def proteccion(tipo):
    if tipo.lower() == 'escudo':
        precio = 10
        return {'escudo': {'precio': precio, 'venta': precio * 0.8, 'destreza': 1, 'protección': True}}
    elif tipo.lower() == 'escudo goblin':
        return {'escudo goblin': {'precio': None, 'venta': 5, 'destreza': 1, 'protección': True}}


def pocion():
    pass