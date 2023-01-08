from funcionesjueguito import *
import time

stats_player = {"vida": 22,"const":1,"destreza":11,"fuerza":11,}
mochila = {"Armas": {"puño": 0, "espada": 3, "Escudo": 4, "Espada_Magica": 1}, "objetos":{"Pociones":3, "Hidromiel": 0, "Monedas": 4, "Llave": True}}

armario = {} #Variable general para el armario del jugador

def cueva_jugador(inventario,stats_player):
    print("Muy bien jugador has llegado a tu cueva, aquí podrás descansar y guardar los objetos que más te interesen.")
    dormir = 0
    cueva = True
    armario_est =False
    cama = False
    while cueva == True:
        decision = int(input("Que deseas hacer. 1) Descansar  2) Guardar Objetos   3) Salir.  Elige: "))
        if decision == 1:
            print("Has decidido Descansar, esta funcion te permite recuperar 1 punto de vida por cada 10 segundos que duermas, acumulando hasta 4 puntos de vida o hasta que se te llene la vida.")
            time.sleep(1)
            cama = True

            while cama == True:

                if dormir == 4:
                    print("Vaya parece que no puedes seguir durmiendo, has dormido bastante por ahora, volveras al menú.")
                    time.sleep(1)
                    cama = False

                elif stats_player.get("vida") >= ((stats_player.get("const")) * 2 + 20):
                    print("Parece que tiene la vida al máximo ahora no puedes dormir, volveras al menu.")
                    time.sleep(1)
                    cama = False

                else:

                    while dormir <= 4:
                        print("durmiendo.")
                        time.sleep(1)
                        print("durmiendo..")
                        time.sleep(2)
                        print("durmiendo...")
                        time.sleep(3)
                        print("durmiendo....")
                        time.sleep(4)

                        dormir += 1
                        stats_player.update({"vida": stats_player.get("vida") + 1})
                        break
                    print(f"Tu vida actual es de {stats_player.get('vida')} puntos.")
                    decision_1 = int(input("Deseas seguir durmiendo o salir.  1) Dormir  2) Salir  Elige: "))

                    if decision_1 == 1:
                        print("vas a seguir durmiendo")
                        continue

                    elif decision_1 == 2:
                        print("Vas a dejar de dormir.")
                        cama = False

#Continuar con el armario, solucionari problema acceder mochila ya que esta dentro de una funcion y eso no lo he tenido en cuenta
        elif decision == 2:
            print("Has decidido guardar objetos.")
            armario_est = True
            print(f"Actualmente estos son tus objetos en el armario: {armario}")

            while armario_est == True:
                objeto_guardar = input(f"A que menu quieres acceder {inventario.keys()}, \n Elige: ")

                if objeto_guardar == "Armas":
                    print(f"Estas son tus armas: {inventario['Armas']}")
                    objeto_guardar = input("Que objeto quieres guardar: ")
                    if objeto_guardar not in armario and objeto_guardar in inventario["Armas"]:
                        contador_objetos = 0
                        armario.update({objeto_guardar:contador_objetos+1})
                        #inventario.update({"Armas":inventario.get(objeto_guardar) - 1})
                        print(armario)
                    elif objeto_guardar in armario:
                        contador_objetos = armario.get(objeto_guardar)
                        armario.update({objeto_guardar: contador_objetos + 1})
                        #inventario.update({"Armas": inventario.get(objeto_guardar) - 1})
                        print(armario)
                    else:
                        print("El objeto introducido no existe")
                        continue


                elif objeto_guardar == "objetos":
                    print(f"Estas son tus objetos: {inventario['objetos']}")
                    objeto_guardar = input("Que objeto quieres guardar: ")
                    if objeto_guardar not in armario and objeto_guardar in inventario["objetos"]:
                        contador_objetos = 0
                        armario.update({objeto_guardar: contador_objetos + 1})
                        # inventario.update({"Armas":inventario.get(objeto_guardar) - 1})
                        print(armario)
                    elif objeto_guardar in armario:
                        contador_objetos = armario.get(objeto_guardar)
                        armario.update({objeto_guardar: contador_objetos + 1})
                        # inventario.update({"Armas": inventario.get(objeto_guardar) - 1})
                        print(armario)
                    else:
                        print("El objeto introducido no existe")
                        continue
                    continue

                else:
                    print("Eso no es un dato válido, intentalo de nuevo.")
                    continue



        elif decision == 3:
            print("Muy bien has decidido salir de la cueva")
            #mapa(inv,mochila), aqui llamariamos de nuevo a la funcion del mapa para que el jugador eliga un sitio a donde ir

        else:
            print("La opción introducida no es correcta intentalo de nuevo, jugador.")
            continue




cueva_jugador(mochila,stats_player)


#print(mochila)
"""a = mochila.get("Armas")
print(a)

v = "espada"
res = a.get(v) -1
a.update()

mochila.update({"Armas": mochila.get("Armas") - 1})
print(mochila)
"""
