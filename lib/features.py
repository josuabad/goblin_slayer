# Módulos
import os
import time


# Funciones
def borrar_pantalla():  # Borrar la pantalla
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def pantalla_de_carga():  # Embellecedor de tiempo de carga
    tiempo = 0
    while tiempo != 3:
        borrar_pantalla()
        print('Cargando.')
        time.sleep(1)
        borrar_pantalla()
        print('Cargando..')
        time.sleep(1)
        borrar_pantalla()
        print('Cargando...')
        time.sleep(1)
        borrar_pantalla()
        tiempo += 1


def medidor_de_bolsillos(bolsillo):
    # Explicación
    # Mira cuantas cosas tienes, sin tener en cuenta las monedas.
    # Devuelve True si hay espacio, False en caso contrario (20 elementos en total)
    # Desarrollo
    cantidad_total = 0
    cantidad_monedas = 0
    for elemento in bolsillo:
        try:
            cantidad_total += bolsillo[elemento]["cantidad"]
        except KeyError:
            cantidad_monedas = bolsillo[elemento]
    if cantidad_total == 0:
        print('Todavía no tienes nada, sal a la aventura y cárgate con lo que te encuentres')
        print('En el futuro te puede ser de gran ayuda')
        print(f'Tienes {cantidad_monedas} monedas')
        return True
    elif 9 <= cantidad_total <= 11:
        print(f'Tienes tus bolsillos llenos hasta la mitad ({cantidad_total})')
        print('Considera ir a tu cueva a guardar los excedentes')
        print('O ve a la tienda y véndelos a cambio de monedas de oro para comprar nuevas armas, protección, o pociones')
        print(f'Tienes {cantidad_monedas} monedas')
        return True
    elif cantidad_total == 20:
        print('Tienes que ir a tu cueva a dejar todo lo que has guardado')
        print('¡Ya no te entra nada en los bolsillos!')
        print(f'Tienes {cantidad_monedas} monedas')
        return False
