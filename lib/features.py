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
    while tiempo != 1:
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
    # Mira cuantas cosas tienes, sin tener en cuenta las monedas
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
        print(
            'O ve a la tienda y véndelos a cambio de monedas de oro para comprar nuevas armas, protección, o pociones')
        print(f'Tienes {cantidad_monedas} monedas')
        return True
    elif cantidad_total == 20:
        print('Tienes que ir a tu cueva a dejar todo lo que has guardado')
        print('¡Ya no te entra nada en los bolsillos!')
        print(f'Tienes {cantidad_monedas} monedas')
        return False


def medidor_de_mochila(mochila, tipo_nuevo_elemento=False):
    # Explicación
    # Mira cuantas cosas tienes dentro de la mochila
    # En caso de meter algo más dentro de la mochila hay que determinar el tipo de elemento que se quiere meter
    # Los tipos de elementos son: arma, protección o pocion
    # Devuelve True si hay espacio, False en caso contrario (2 armas y 1 escudo, pociones ilimitadas)
    # Desarrollo
    cantidad_armas = 0
    cantidad_proteccion = 0
    for elemento in mochila:
        try:
            if elemento == 'puño' or elemento == 'puños':
                continue
            tipo = mochila[elemento]["arma"]
            if tipo:
                cantidad_armas += 1
        except KeyError:
            tipo = mochila[elemento]["proteccion"]
            if tipo:
                cantidad_proteccion += 1
    if cantidad_proteccion == 0 and cantidad_armas == 0:
        return True
    elif cantidad_proteccion == 1 and cantidad_armas == 2:
        return False
    elif cantidad_proteccion == 1 and tipo_nuevo_elemento == 'arma':
        if 0 <= cantidad_armas < 2:
            return True
        else:
            return False
    elif cantidad_proteccion == 1 and tipo_nuevo_elemento == 'proteccion':
        return False
    elif cantidad_armas == 2 and tipo_nuevo_elemento == 'proteccion':
        if cantidad_proteccion == 0:
            return True
        else:
            return False
    elif cantidad_armas == 2 and tipo_nuevo_elemento == 'arma':
        return False
