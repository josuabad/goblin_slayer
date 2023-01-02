from funcionesjueguito import *

#Variables globales de prueba Jugador (mochila y stats)
stats_player = {"vida":22,"destreza":11,"fuerza":11}
mochila = {"arma":{"puño":0}}

#Variables Globales de los enemigos
Combate = False
Ratas = False
Goblins = False
Ogro = False
Estafermo = False
NoEnemies = True
turno_player = False
turno_enemigo = False

def alcantarilla(inventario,player_stats):
    Estafermo = True
    print("Muy bien Jugador has decidido entrar a las Alcantarillas.")
    print("Ten cuidado este sitio esta repleto de Ratas Gigantes")
    combate(inventario,player_stats,Estafermo)

alcantarilla(mochila,stats_player)