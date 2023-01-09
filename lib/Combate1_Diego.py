#Librerias de otros ficheros/archivos
from funcionesjueguito import *
#Variables globales de prueba Jugador (mochila y stats)
stats_player = {"vida": 22,"const":1,"destreza":11,"fuerza":11,}
mochila = {"Armas": {"puño": 0, "espada": 3, "Escudo": 4, "Espada_Magica": 1}, "objetos":{"Pociones":3, "Hidromiel": 0,  "Llave": True, } , "Experiencia" : 12, "Monedas": 4}

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
        combate_ogro(inventario,stats_player)
    elif enemigo_selec == 4:
        print("estafermo") #una vez a encontrado ese enemigo, inicia su funcion de combate, en este caso el estafermo
        combate_estafermo(inventario,stats_player) #Este tomara las variables del inventario y las estadisticas


#combate(mochila,stats_player,3)

def combate_ogro(inventario,stats_player):
    Combate, turno_player, turno_enemigo = False,False, False
    vida_ogro = 50
    dam_ogro = dados(12) + 2
    impacto_ogro = 16
    golpe_ogro = 0
    Combate = True

    while Combate == True:
        golpe_player = dados(20)
        print("\nEs tu turno Jugador")

        if golpe_player >= impacto_ogro:
            turno_player = True

        else:
            print("Vaya no has conseguido impactar.")
            turno_enemigo = True

        while turno_player == True:
            print("Has impactado")
            dam_player = (stats_player.get("fuerza") - 10) + dados(4) # Calcula el daño del jugador en base al arma, que en este caso al ser el puño he puesto directamente en dados(4), pero deberia ser el valor del arma que lleve en ese momento
            vida_ogro = vida_ogro - dam_player

            if vida_ogro <= 0:
                print("Muy bien, Jugador has conseguido derrotar el temible Jefe Ogro. ")
                print("Has ganado 500 puntos de experiencia, además te has llevado su botín de 200 monedas.")

                inventario.update({"Experiencia": inventario.get('Experiencia') + 500})
                inventario.update({"Monedas": inventario.get('Monedas') + 200})

                print("Ya has terminado tu labor ahora regresaras al pueblo")
                Combate, turno_player = False, False #Provisional esta linea
               # def victoria()

            else:
                print(f"Tu golpe ha hecho {dam_player} puntos de daño, el Ogro tiene {vida_ogro} puntos de vida")
                turno_player, turno_enemigo = False, True

        while turno_enemigo == True:
            print("\n Es el turno del Ogro.")
            impacto_player = 12 + (stats_player.get("destreza")-10) #Deberemos calcular cuanto debe sacar el enemigo para impactar al jugador, esto en base a la estadistica de destreza
            golpe_ogro = dados(20)

            if golpe_ogro >= impacto_player:
                print("El Ogro ha impactado.")
                vida_player = stats_player.get("vida") #Creamos una variable con el valor de vida que en ese momento tiene el jugador
                vida_player = vida_player - dam_ogro
                stats_player.update({"vida":vida_player}) #Subimos, por asñi decirlo, el nuevo valor al diccionario del jugador
                print(f"El Ogro te ha hecho {dam_ogro} punto de daño tienes, {vida_player} puntos de vida") #Imprimimos detalles del combate como el daño y nuestra vida
                turno_player, turno_enemigo = True,False

            else:
                print("El ogro no ha impactado")
                turno_enemigo, turno_player = False, True


combate(mochila,stats_player,3)

""""
IMPORTANTISIMO EN TODOS LOS COMBATES PONER EL CASO DE CUANDO EL JUGADOR MUERE
"""