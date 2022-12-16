import time
import fun_borrar_pantalla


def cama(vida, tiempo):  # Para recuperar toda la vida hay que dormir 8 horas
    relacion_sueño = vida/8
    for horas in range(tiempo + 1):
        print(f'Has dormido {horas} horas')
        time.sleep(relacion_sueño)
        fun_borrar_pantalla.borrar_pantalla()
    return [tiempo, relacion_sueño * tiempo]  # Devuelve [tiempo dormido, vida recuperada]


"""
def armario():
    pass


def inventario():
    pass


def cueva_del_jugador():
    pass
"""
