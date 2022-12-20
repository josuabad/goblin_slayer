# Archivo susceptible de edición
import random


def arma_espada():
    dano = random.randint(8)
    precio = 10
    return {'espada': {'daño': dano, 'precio': precio, 'venta': precio * 0.8}}