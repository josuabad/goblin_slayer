#          NOTAS          #

# Esta función consta de listas dentro de la lista principal y se accede a ella dependiendo de la posición
# de manera que la posición 1 sean las armas, la 2 las armaduras y la 3 la poción.


import time


def Fun_Tienda(mochila, bolsa):  # Fun_Tienda()
    print("¡Bienvenido a la tienda jugador!\n¿Qué te gustaría comprar?")  # La bienvenida a la tienda.
    Fun_Tienda = True  # Mientras que la función de tienda sea True, siempre va a estar dentro del bucle.
    while Fun_Tienda == True:  # Bucle para que esté dentro de la tienda hasta que quiera SALIR.
        numero_tienda_lista = int(input("Introduzca el número de lo que desee:\n1) Armas\n2) Armadura\n3) Pociones "
                                        "\n4) Vender\n5) Salir\nNúmero: "))  # Variable para ver que quieres de la tienda
        time.sleep(0.5)
        if numero_tienda_lista == 1:  # Si la variable es igual a 1 escogiste arma.
            print(tienda[0])  # Aquí imprime la posición 0 de la lista, y esa es otra lista que contiene todas las
            # armas.
            time.sleep(0.5)
            numero_tienda_sublista = str(input("Introduzca la letra dentro del paréntesis de lo que desee: "))  # Aqu
            # í tienes que especificar que arma quieres colocando la letra dentro del paréntesis
            if numero_tienda_sublista.upper() == 'EM':  # Si colocas las letras EM, pides la espada mágica.
                print('La espada mágica cuesta: 200 monedas')  # Aquí te imprime cuanto cuesta la espada mágica.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    # Aquí se le resta a la mochila en la sección de monedas - 200
                    if mochila.get("Monedas") >= 200:  # Aquí evalúa si tiene las 200 monedas
                        mochila.update({"Monedas": mochila.get("Monedas") - 200})  # Obtiene las monedas y las resta
                        mochila.update({"espada mágica": mochila.get("espada mágica") + 1})  # Le suma 1 al valor de la clave del diccionario
                        print("¡Gracias por tu compra, aquí tiene su espada mágica!")  # Agradecimiento
                        print(f"--> Actualmente tienes: {mochila.get('espada mágica')} Espadas Mágicas")  # Indica la cantidad que hay en la mochila de ese objeto
                        print(f"--> Te quedan: {mochila.get('Monedas')} Monedas")  # Te recuerda cuantas monedas te quedan
                        continue

                    else: # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("Monedas")} .\nVuelve cuando tengas las 200. ¡Hasta pronto!')
                        continue  # Lo devuelve a la tienda

                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue

                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    continue

            elif numero_tienda_sublista.upper() == 'E':  # Si colocas las letras E, pides la espada.
                print(f'La espada cuesta: 10 monedas')  # Aquí te imprime cuanto cuesta la espada.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    if mochila.get("Monedas") >= 10:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"Monedas": mochila.get("Monedas") - 10})
                        mochila.update({"espada": mochila.get("espada") + 1})
                        print("¡Gracias por tu compra, aquí tiene su espada!")  # Agradecimiento
                        print(f"--> Actualmente tienes: {mochila.get('espada')} Espadas")
                        print(f"--> Te quedan: {mochila.get('Monedas')} Monedas")
                        continue

                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("Monedas")} .\nVuelve cuando tengas las 10. ¡Hasta pronto!')
                        continue  # Lo devuelve a la tienda

                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue

                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    continue

            elif numero_tienda_sublista.upper() == 'H2':  # Si colocas las letras H2, pides el hacha de dos manos.
                print(f'El hacha de dos manos cuesta: 30 monedas')  # Aquí te imprime cuanto cuesta el hacha de dos
                # manos.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    if mochila.get("Monedas") >= 30:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"Monedas": mochila.get("Monedas") - 30})
                        mochila.update({"hacha de dos manos": mochila.get("hacha de dos manos") + 1})
                        print("¡Gracias por tu compra, aquí tiene su hacha de dos manos!")  # Agradecimiento
                        print(f'--> Actualmente tienes: {mochila.get("hacha de dos manos")} hacha de dos manos')
                        print(f"--> Te quedan: {mochila.get('Monedas')} Monedas")
                        continue

                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("Monedas")} .\nVuelve cuando tengas las 30. ¡Hasta pronto!')
                        continue  # Lo devuelve a la tienda

                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue

                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    continue

            elif numero_tienda_sublista.upper() == 'S':  # Si colocas la letra S, pides el escudo.
                print(f'El escudo cuesta: 10 monedas')  # Aquí te imprime cuanto cuesta el escudo.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    if mochila.get("Monedas") >= 10:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"Monedas": mochila.get("Monedas") - 10})
                        mochila.update({"escudo": mochila.get("escudo") + 1})
                        print("¡Gracias por tu compra, aquí tiene su escudo!")  # Agradecimiento
                        print(f"--> Actualmente tienes: {mochila.get('escudo')} Escudos")
                        print(f"--> Te quedan: {mochila.get('Monedas')} Monedas")
                        continue

                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("Monedas")} .\nVuelve cuando tengas las 10. ¡Hasta pronto!')
                        continue  # Lo devuelve a la tienda

                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue

                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    continue

            else:
                print("No disponemos de esa arma en la tienda, vuelva a seleccionarlo.")
                continue

        elif numero_tienda_lista == 2:  # Si la variable es igual a 2 escogiste armadura.
            print(tienda[1])  # Aquí imprime la posición 1 de la lista, y esa es otra lista que contiene todas las
            # armaduras.
            time.sleep(0.5)
            numero_tienda_sublista = str(input("Introduzca la letra dentro del paréntesis de lo que desee: "))  # Aqu
            # í tienes que especificar que armadura quieres colocando la letra dentro del paréntesis
            if numero_tienda_sublista.upper() == 'A1':  # Si colocas las letras A1, pides armadura nivel 1.
                print(f'La armadura nivel 1 cuesta: 30 monedas')  # Aquí te imprime cuanto cuesta la armadura nivel 1.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    if mochila.get("Monedas") >= 30:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"Monedas": mochila.get("Monedas") - 30})
                        mochila.update({"armadura nivel 1": mochila.get("armadura nivel 1") + 1})
                        print("¡Gracias por tu compra, aquí tiene su armadura nivel 1!")  # Agradecimiento
                        print(f"--> Actualmente tienes {mochila.get('armadura nivel 1')} Armadura nivel 1")
                        print(f"--> Te quedan: {mochila.get('Monedas')} Monedas")
                        continue

                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("Monedas")} .\nVuelve cuando tengas las 30. ¡Hasta pronto!')
                        continue  # Lo devuelve a la tienda

                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue

                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    continue

            elif numero_tienda_sublista.upper() == 'A2':  # Si colocas las letras A2, pides la armadura nivel 2.
                print(f'La armadura nivel 2 cuesta: 40 monedas')  # Aquí te imprime cuanto cuesta la armadura nivel 2.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    if mochila.get("Monedas") >= 40:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"Monedas": mochila.get("Monedas") - 40})
                        mochila.update({"armadura nivel 2": mochila.get("armadura nivel 2") + 1})
                        print("¡Gracias por tu compra, aquí tiene su armadura nivel 2!")  # Agradecimiento
                        print(f"--> Actualmente tienes: {mochila.get('armadura nivel 2')} Armadura nivel 2")
                        print(f"--> Te quedan: {mochila.get('Monedas')} Monedas")
                        continue

                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("Monedas")} .\nVuelve cuando tengas las 40. ¡Hasta pronto!')
                        continue  # Lo devuelve a la tienda

                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue

                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    continue

            elif numero_tienda_sublista.upper() == 'A3':  # Si colocas las letras A3, pides la armadura nivel 3.
                print(f'La armadura nivel 3 cuesta: 50 monedas')  # Aquí te imprime cuanto cuesta la armdura nivel 3.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    if mochila.get("Monedas") >= 50:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"Monedas": mochila.get("Monedas") - 50})
                        mochila.update({"armadura nivel 3": mochila.get("armadura nivel 3") + 1})
                        print("¡Gracias por tu compra, aquí tiene su armadura nivel 3!")  # Agradecimiento
                        print(f"--> Actualmente tienes: {mochila.get('armadura nivel 3')} Armadura nivel 3")
                        print(f"--> Te quedan: {mochila.get('Monedas')} Monedas")
                        continue

                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("Monedas")} .\nVuelve cuando tengas las 50. ¡Hasta pronto!')
                        continue  # Lo devuelve a la tienda

                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue

                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    continue

            else:
                print("No disponemos de esa armadura en la tienda, vuelva a seleccionarlo.")
                time.sleep(1)
                continue

        elif numero_tienda_lista == 3:  # Si la variable es igual a 3 escogiste poción.
            print(tienda[2])  # Aquí imprime la posición 2 de la lista, y esa es otra lista que contiene la poción.
            print(f'La poción de vida cuesta: 20 monedas')  # Aquí te imprime cuanto cuesta la poción.
            time.sleep(0.5)
            numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
            # verificar si quieres hacer la compra.
            if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                if mochila.get("Monedas") >= 20:  # Aquí evalúa si tiene las 10 monedas
                    mochila.update({"Monedas": mochila.get("Monedas") - 20})
                    mochila.update({"poción de vida": mochila.get("poción de vida") + 1})
                    print("¡Gracias por tu compra, aquí tiene su poción de vida!")  # Agradecimiento
                    print(f"--> Actualmente tienes {mochila.get('poción de vida')} Poción de vida")
                    print(f"--> Te quedan: {mochila.get('Monedas')} Monedas")
                    continue

                else:  # Si no tiene las 200 monedas.
                    print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("Monedas")} .\nVuelve cuando tengas las 20. ¡Hasta pronto!')
                    continue  # Lo devuelve a la tienda

            elif numero_de_compra == 2:
                print("\nVale, ¿desea comprar otra cosa?\n")
                time.sleep(0.5)
                continue

            else:
                print("No disponemos de esa pocion en la tienda, vuelva a seleccionarlo.")  # Aquí es por si
                # introduce una poción que no exista.
                continue  # Aquí lo devuelve a que quiere de pociones.

        elif numero_tienda_lista == 4:  # Si la variable es 4, pues has decidido vender
            time.sleep(0.5)
            print("Vale, quieres venderme un artículo. Muéstrame  que traes.\n")
            time.sleep(1)
            print("-------------------------------------\n")
            print(f'Tienes estos artículos para vender: \n{bolsa}\n{mochila}\n')
            print("-------------------------------------\n")
            objeto_vender = input("Que quieres vender?: ")
            mochila.get([objeto_vender]["venta"])

                #bolsa.update({"poción de vida": bolsa.get("poción de vida") + 1})
                #mochila.update({"Monedas": mochila.get("Monedas") - 20})

        elif numero_tienda_lista == 5:  # Si la variable es igual a 4 es porque escogiste salir.
            print("Hasta pronto, espero verlo de nuevo\n")  # Despedida.
            time.sleep(1)

        else:
            print("No tenemos eso en la tienda, ¡vuelva a introducir un número válido!\n")  # Esto es por si el jugador
            # introduce algo que no está
            time.sleep(1)
        continue  # Aquí te devuelve al menú de la tienda


tienda = [['(EM) Espada Mágica', '(E) Espada', '(H2) Hacha dos manos', '(S) Escudo'],
          ['(A1) Armadura nivel 1', '(A2) Armadura nivel 2', '(A3) Armadura nivel 3'], ['(P) Poción de vida']]
bolsa = {'espada goblin': 3, 'escudo goblin': 3, '': 0}
mochila = {'espada mágica': 0, 'espada': 0, 'hacha dos manos': 0, 'escudo': 0, 'armadura nivel 1': 0, 'Armadura nivel 2': 0, 'armadura nivel 3': 0, 'poción de vida': 0, 'Monedas': 1000}
# print(tienda[0])
Fun_Tienda(mochila, bolsa)  # Llamando a la función tienda


