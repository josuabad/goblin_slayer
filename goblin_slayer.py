# Versión oficial
import time
from lib import fun_borrar_pantalla

def pantalla_de_carga():  # Embellecedor
    tiempo = 0
    while tiempo != 3:
        fun_borrar_pantalla.borrar()
        print('Cargando.')
        time.sleep(1)
        fun_borrar_pantalla.borrar()
        print('Cargando..')
        time.sleep(1)
        fun_borrar_pantalla.borrar()
        print('Cargando...')
        time.sleep(1)
        fun_borrar_pantalla.borrar()
        tiempo += 1
"""
Cómo es la estructura del juego:
1. Empieza el juego (Bienvenida)
2. Configuración del personaje
2.1 Se crea al personaje (características + mochila)
2.2 Se modifica al personaje (distribuir puntos de habilidad)
3. Entra en el mapa
"""

fun_borrar_pantalla.borrar()
print('Inicia sesión: ')
nombre = input('Usuario: ')
# Loop de carga (embellecedor)
pantalla_de_carga()
print(f'¡Bienvenido {nombre}!')