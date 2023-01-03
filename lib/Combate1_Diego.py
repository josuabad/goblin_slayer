#Librerias de otros ficheros/archivos
from funcionesjueguito import *
#Variables globales de prueba Jugador (mochila y stats)
stats_player = {"vida":22,"destreza":11,"fuerza":11}
mochila = {"arma":{"puño":0}}

#Variables Globales de los enemigos
Combate = False
Ratas = 1
Goblins = 2
Ogro = 3
Estafermo = 4
NoEnemies = 0
turno_player = False
turno_enemigo = False
"""
Explicacion:
Por cada tipo de enemigo se crea una variable Booleana, al principio cada una de esas variables esta en False
osea no se activa nada.
Cuando la situacion lo requiera se elige el enemigo y la variable se cambia a True. Para posteriormente
llamar a la funcion combate(inv,stats,enemigo) donde en enemigo se introduce el enemigo con la variable en True
<<<<<<< HEAD
=======

Ahí dentro de la funcion principal se comprueba que enemigo es al que nos enfrentamos, entonces una vez
comprobado la funcion combate llamara a otra (ej: combate_ratas, combate_goblins, etc.) donde se encontrara el
combate y la logica para cada uno de los enemigos en este primer caso solo lo he probado con el estafermo

Esta el la primera Version de la plantilla para los combates, faltaria que les dieran ustedes el visto bueno,
para empezar a implementar la logica a los otros enemigos, y ajustar unos pequeños detalles
"""
"""

Ahí dentro de la funcion principal se comprueba que enemigo es al que nos enfrentamos, entonces una vez
comprobado la funcion combate llamara a otra (ej: combate_ratas, combate_goblins, etc.) donde se encontrara el
combate y la logica para cada uno de los enemigos en este primer caso solo lo he probado con el estafermo

Esta el la primera Version de la plantilla para los combates, faltaria que les dieran ustedes el visto bueno,
para empezar a implementar la logica a los otros enemigos, y ajustar unos pequeños detalles
"""

def combate(inventario, stats_player, enemigo_selec): #Esta funcion comprueba que combate debe activar
    enemigo = enemigo_selec #Enemigo es una variable que toma el valor de enemigo_selec
    if enemigo == NoEnemies:
        print("No hay un combate disponible")
    elif enemigo_selec == 1: #COmprueba uno por uno el tipo de enemigo
        print("ratas es True")
        combate_ratas(inventario,stats_player)
    elif enemigo_selec == 2:
        print("goblins")
    elif enemigo_selec == 3:
        print("ogro")
    elif enemigo_selec == 4:
        print("estafermo") #una vez a encontrado ese enemigo, inicia su funcion de combate, en este caso el estafermo
        combate_estafermo(inventario,stats_player) #Este tomara las variables del inventario y las estadisticas


combate(mochila,stats_player,4)






