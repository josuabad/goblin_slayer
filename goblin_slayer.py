# Módulos
from lib import features, articulos, config_habilidades
from modulos import fun_mapa


# Desarrollo
# Bienvenida al juego
features.borrar_pantalla()
print('Inicia sesión: ')
nombre = input('Usuario: ')
features.pantalla_de_carga()
print(f'¡Bienvenido {nombre}!')
input('Pulsa ENTER para continuar...')

# Habilidades del personaje
personaje_habilidades = {'fuerza': 10, 'destreza': 10, 'constitucion': 10}
personaje_especificas = {'daño': 0, 'defensa': 0, 'vida': 0, 'experiencia': 0, 'level': 0}
mochila = {}
bolsillo = {'monedas': 0, 'Llave': False}
armario = {}
mochila.update(articulos.arma('puño'))
puntos_habilidades = 3

# Creación del personaje
run = True
while run:
    set_habilidades = config_habilidades.habilidades(personaje_habilidades, puntos_habilidades)
    puntos_habilidades = set_habilidades[1]  # Actualización de los puntos de habilidad restantes
    config_habilidades.especificas_personaje(personaje_habilidades, personaje_especificas)
    print(f'Tus características son las siguientes: {personaje_especificas}')
    while True:
        if puntos_habilidades > 0:
            features.borrar_pantalla()
            seguir = input(f'Todavía tienes {puntos_habilidades} más. ¿Deseas repartirlos? [s/n]: ')
            if seguir.lower() == 's':
                break
            elif seguir.lower() == 'n':
                run = False
                break
            else:
                features.borrar_pantalla()
                print('Algo ha ido mal, repita el proceso por favor')
                continue
        else:
            run = False
            break
input('Pulsa ENTER para continuar...')

# Entra al juego
fun_mapa.fun_mapa(nombre, mochila, bolsillo, personaje_especificas, personaje_habilidades, puntos_habilidades, armario)
