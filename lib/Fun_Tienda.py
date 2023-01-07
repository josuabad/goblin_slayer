# Fun_Tienda()
# Esta función consta de listas dentro de lista principal y se accede a ella dependiendo de la posición.

import time


def Fun_Tienda(mochila):
    print("¡Bienvenido a la tienda jugador!\n¿Qué te gustaría comprar?")  # La bienvenida a la tienda.
    Fun_Tienda = True  # Mientras que la función de tienda sea True, siempre va a estar dentro del bucle.
    while Fun_Tienda == True:  # Bucle para que esté dentro de la tienda hasta que quiera SALIR.
        numero_tienda_lista = int(input("Introduzca el número de lo que desee:\n1) Armas \n2) Armadura \n3) Pociones "
                                        "\n4) Salir \nNúmero: "))  # Variable para ver que quieres de la tienda
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
                    print("¡Gracias por tu compra, aquí tiene su espada mágica!")  # Agradecimiento
                    # dar objeto y guardarla en la lista del personaje
                    return mochila

                elif numero_de_compra == 2:
                    return Fun_Tienda


            elif numero_tienda_sublista.upper() == 'E':  # Si colocas las letras E, pides la espada.
                print(f'La espada cuesta: 10 monedas')  # Aquí te imprime cuanto cuesta la espada.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    # Aquí se le resta a la mochila en la sección de monedas - 10
                    print("¡Gracias por tu compra, aquí tiene su espada!")  # Agradecimiento
                    # insertar algo que se la de a la función del personaje

            elif numero_tienda_sublista.upper() == 'H2':  # Si colocas las letras H2, pides el hacha de dos manos.
                print(f'El hacha de dos manos cuesta: 30 monedas')  # Aquí te imprime cuanto cuesta el hacha de dos
                # manos.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    # Aquí se le resta a la mochila en la sección de monedas - 30
                    print("¡Gracias por tu compra, aquí tiene su hacha de dos manos!")  # Agradecimiento
                    # insertar algo que se la de a la función del personaje

            elif numero_tienda_sublista.upper() == 'S':  # Si colocas la letra S, pides el escudo.
                print(f'El escudo cuesta: 10 monedas')  # Aquí te imprime cuanto cuesta el escudo.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    # Aquí se le resta a la mochila en la sección de monedas - 10
                    print("¡Gracias por tu compra, aquí tiene su escudo!")  # Agradecimiento
                    # insertar algo que se la de a la función del personaje

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
                    # import de donde esté la función de mochila

                    # Aquí se le resta a la mochila en la sección de monedas - 30
                    print("¡Gracias por tu compra, aquí tiene su armadura nivel 1!")  # Agradecimiento
                    # insertar algo que se la de a la función del personaje

            elif numero_tienda_sublista.upper() == 'A2':  # Si colocas las letras A2, pides la armadura nivel 2.
                print(f'La armadura nivel 2 cuesta: 40 monedas')  # Aquí te imprime cuanto cuesta la armadura nivel 2.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    # Aquí se le resta a la mochila en la sección de monedas - 40
                    print("¡Gracias por tu compra, aquí tiene su armadura nivel 2!")  # Agradecimiento
                    # insertar algo que se la de a la función del personaje

            elif numero_tienda_sublista.upper() == 'A3':  # Si colocas las letras A3, pides la armadura nivel 3.
                print(f'La armadura nivel 3 cuesta: 50 monedas')  # Aquí te imprime cuanto cuesta la armdura nivel 3.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    # Aquí se le resta a la mochila en la sección de monedas - 50
                    print("¡Gracias por tu compra, aquí tiene su armadura nivel 3!")  # Agradecimiento
                    # insertar algo que se la de a la función del personaje

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
                # Aquí se le resta a la mochila en la sección de monedas - 20
                print("¡Gracias por tu compra, aquí tiene su poción de vida!")  # Agradecimiento
                # insertar algo que se la de a la función del personaje

            else:
                print("No disponemos de esa pocion en la tienda, vuelva a seleccionarlo.")  # Aquí es por si
                # introduce una poción que no exista.
                continue  # Aquí lo devuelve a que quiere de pociones.

        elif numero_tienda_lista == 4:  # Si la variable es igual a 4 es porque escogiste salir.
            print("Hasta pronto, espero verlo de nuevo\n")  # Despedida.
            time.sleep(1)

        else:
            print("No tenemos eso en la tienda, ¡vuelva a introducir un número válido!\n")  # Esto es por si el jugador
            # introduce algo que no está
            time.sleep(1)
        continue  # Aquí te devuelve al menú de la tienda


tienda = [['(EM) Espada Mágica', '(E) Espada', '(H2) Hacha dos manos', '(S) Escudo'],
          ['(A1) Armadura nivel 1', '(A2) Armadura nivel 2', '(A3) Armadura nivel 3'], ['(P) Poción de vida']]
# Tienda se creó en una lista con sublistas, de manera que la posición uno sean las armas, la 2 las armaduras y la 3
# la poción.

# print(tienda[0])
Fun_Tienda()  # Llamando a la función tienda

#          NOTAS          #

# 1) Falta restar las monedas en la mochila #
#    * Para esta función tener en cuenta:
#    1.1) Hay que verificar si tiene el dinero.
#    1.2) Si no tiene el dinero imprimir que no lo tiene y devolverlo al menu de la tienda.
#    1.3) En caso de que si lo tenga, restar el dinero de la mochila
#
# 2) Falta luego de la compra sumar el artículo al diccionario de la mochila
