from funcionesjueguito import *

#Variables globales de prueba Jugador (mochila y stats)
stats_player = {"vida":22,"destreza":11,"fuerza":11}
mochila = {"arma":{"puño":0}}


def alcantarilla(inventario,player_stats):

    print("Muy bien Jugador has decidido entrar a las Alcantarillas.")
    print("Ten cuidado este sitio esta repleto de Ratas Gigantes")
    combate(inventario,player_stats,1)

alcantarilla(mochila,stats_player)