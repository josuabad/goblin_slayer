# Versión oficial
from lib import features
from lib import config_habilidades


# Desarrollo
# Bienvenida al juego
features.borrar_pantalla()
print('Inicia sesión: ')
nombre = input('Usuario: ')
features.pantalla_de_carga()
print(f'¡Bienvenido {nombre}!')

# Habilidades del personaje
personaje_habilidades = {'fuerza': 10, 'destreza': 10, 'constitucion': 10}
puntos_habilidades = 3

# Creación del personaje
set_habilidades = config_habilidades.habilidades((personaje_habilidades, puntos_habilidades))
puntos_habilidades = set_habilidades[1]  # Actualización de los puntos de habilidad restantes
set_personaje = config_habilidades.especificas_personaje(personaje_habilidades)
dano = set_personaje[0]
defensa = set_personaje[1]
vida = set_personaje[2]