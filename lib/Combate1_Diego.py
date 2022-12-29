#Librerias de otros ficheros/archivos
from funcionesjueguito import *

#Variables Globales de los enemigos
Combate = False
Ratas = False
Goblins = False
Ogro = False
Estaferno = False





def combate(inventario, player_stats, enemigo_selec):
    enemigo = enemigo_selec
    if enemigo == (Ratas == True):
        print("ratas es True")
    elif enemigo == (Goblins == True):
        print("goblins")
    elif enemigo == (Ogro == True):
        print("ogro")
    elif enemigo == (Estaferno == True):
        print("estaferno")
        #combate_estaferno(inventario,player_Stats)



def combate_estaferno(inventario,player_stats):
    vida_estaferno = 50000
    dam_estaferno = 0
    Combate = True
    while Combate == True:












