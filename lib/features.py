import os
import time


def borrar_pantalla():  # El código para borrar la pantalla depende del SO
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def pantalla_de_carga():  # Embellecedor
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