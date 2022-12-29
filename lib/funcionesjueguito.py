import random

vida_rata = 0
damage_rata = 0
damage = 0


def dados(n): #La función en resumen crea una lista según el número de caras del dado y de ahi hace un random.choice
    dado_juego = []
    dado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for x in range(0, n):

        dado_juego.append(dado[x])

    res_dado = random.choice(dado_juego)
    return res_dado



def rat_attack():
    damage_rata = dados(4)
    damage = damage_rata
    return damage_rata

def gob_attack():
    damage_gob = dados(4)
    damage = damage_rata
    return damage_rata


#Manera de calcular el daño para cualquier enemigo V1
vida_player = 20
print(vida_player)
vida_player2 = vida_player-(rat_attack())
print(f"La rata ha hecho,{20-vida_player2} puntos de daño ")
print(vida_player2)
#Para la huida, creamos una variable que guarde el resultado de la eleccion como un SI o un NO
print("Has iniciado un combate, si deseas huir debes sacar más de 6 en un dado de 10. ")


try:
    eleccion_huida = input(" SI|NO : ")
    eleccion_huida = eleccion_huida.upper()

except ValueError:
    print("Has introducido un valor erroneo. Intentalo de nuevo") #Arreglar introduccion dato de eleccion

if eleccion_huida == "SI" or "1":
    print("Muy bien has decidido huir, vamos a probar suerte.")
    huida = dados(10)
    if huida > 6:
        print(f"Has sacado un {huida}.")
        print("Muy bien has logrado huir ")
    else:
        print(f"Has sacado un {huida}.")
        print("ooohh..... no, no has logrado huir te va a tocar luchar")











