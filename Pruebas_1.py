# función de tienda

# Ejemplo 1 de tienda
# Tienda = []
"""def fun_tienda(tienda):
    for i in range(0, Tienda):
        tienda_aux = []
        for j in range(0, Tienda):
            aux = int(input("Introduzca el número de lo que desee:\n1)Armas \n2) Armadura \n3) Posiones "
                                    "\n4) Salir \nNúmero: ))

            tienda_aux.append(int(aux))
        Tienda.append(tienda_aux)
    # print(tienda)
    return Tienda"""

# Ejemplo de como puede ser la función de tienda con listas Se accedería a ella depende de la posición

# tienda_1 = [['espada (E)', 'escudo (S)', 'hacha (A)', 'hacha de dos manos (AA)', 'espada mágica (EM)'],
# ['(A1) Armadura nivel 1', ' (A2) Armadura nivel 2', ' (A3) Armadura nivel 3'], ['(P) Poción de vida']]

# Ejemplo 2 de tienda
"""def fun_tiendas():
    # armas : [0]
    # armadura [1]
    # poción de vida : [3]
    # luego que te salga que contiene la lista dependiendo de que numero se haya seleccionado...
    # se seleccionaria la posición del diccionario junto con la lista"""

# Ejemplo 3 de tienda metiendo diccionarios dentro de las listas

"""def Fun_Tienda():
    print("¡Bienvenido a la tienda!\n¿Qué te gustaría comprar?")
    Fun_Tienda = True
    while Fun_Tienda == True:
        numero_tienda_lista = int(input("Introduzca el número de lo que desee:\n1) Armas \n2) Armadura \n3) Pociones "
                                        "\n4) Salir \nNúmero: "))
        if numero_tienda_lista == 1:
            print(tienda[0])
            numero_tienda_diccionario = int(input("Introduzca la letra dentro del paréntesis de lo que desee: "))
            if numero_tienda_diccionario == 'EM':
                print(f'La espada mágica cuesta: ', armas.get('(EM) Espada Mágica'))
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 200
                    print("¡Gracias por tu compra, aquí tiene su espada mágica!")  # dar objeto
                    # hay que verificar si tiene el dinero
                    # si no tiene el dinero imprimir que no lo tiene y devolverlo al menu de la tienda
                    # restar el dinero de tu cuenta o acumulador de dinero

                elif numero_tienda_diccionario == 'E':
                    print(f'La espada cuesta: ', armas.get('(E) Espada'))
                    numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                    if numero_de_compra == 1:
                        cuenta_bancaria = cuenta_bancaria - 10
                        print("¡Gracias por tu compra, aquí tiene su espada!")
                        # insertar algo que se la de a la función del personaje

                elif numero_tienda_diccionario == 'H2':
                    print(f'El hacha de dos manos cuesta: ', armas.get('(H2) Hacha dos manos'))
                    numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                    if numero_de_compra == 1:
                        cuenta_bancaria = cuenta_bancaria - 30
                        print("¡Gracias por tu compra, aquí tiene su hacha de dos manos!")
                        # insertar algo que se la de a la función del personaje

                elif numero_tienda_diccionario == 'S':
                    print(f'El escudo cuesta: ', armas.get('(S) Escudo'))
                    numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                    if numero_de_compra == 1:
                        cuenta_bancaria = cuenta_bancaria - 10
                        print("¡Gracias por tu compra, aquí tiene su escudo!")
                        # insertar algo que se la de a la función del personaje

                else:
                    print("No disponemos de esa arma en la tienda, vuelva a seleccionarlo.")
                    continue

        elif numero_tienda_lista == 2:
            print(tienda[1])
            numero_tienda_diccionario = int(input("Introduzca la letra dentro del paréntesis de lo que desee: "))
            if numero_tienda_diccionario == 'A1':
                print(f'La armadura nivel 1 cuesta: ', armadura.get('(A1) Armadura nivel 1'))
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 30
                    print("¡Gracias por tu compra, aquí tiene su armadura nivel 1!")
                    # insertar algo que se la de a la función del personaje

            elif numero_tienda_diccionario == 'A2':
                print(f'La armadura nivel 2 cuesta: ', armadura.get('(A2) Armadura nivel 2'))
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 40
                    print("¡Gracias por tu compra, aquí tiene su armadura nivel 2!")
                    # insertar algo que se la de a la función del personaje

            elif numero_tienda_diccionario == 'A3':
                print(f'La armadura nivel 3 cuesta: ', armadura.get('(A3) Armadura nivel 3'))
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 50
                    print("¡Gracias por tu compra, aquí tiene su armadura nivel 3!")
                    # insertar algo que se la de a la función del personaje

            else:
                print("No disponemos de esa armadura en la tienda, vuelva a seleccionarlo.")
                continue

        elif numero_tienda_lista == 3:
            print(tienda[2])
            print(f'La pocion de vida cuesta: ', pocion.get('(P) Poción de vida'))
            numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
            if numero_de_compra == 1:
                cuenta_bancaria = cuenta_bancaria - 20
                print("¡Gracias por tu compra, aquí tiene su armadura nivel 1!")
                # insertar algo que se la de a la función del personaje

            else:
                print("No disponemos de esa pocion en la tienda, vuelva a seleccionarlo.")
                continue

        elif numero_tienda_lista == 4:
            print("Hasta pronto, espero verlo de nuevo")
            break

        else:
            print("No tenemos eso en la tienda, ¡vuelva a introducir un número válido!")
        continue


cuenta_bancaria = 1000
armas = {'(EM) Espada Mágica': 200, '(E) Espada': 10, '(H2) Hacha dos manos': 30, '(S) Escudo': 10}
armadura = {'(A1) Armadura nivel 1': 30, '(A2) Armadura nivel 2': 40, '(A3) Armadura nivel 3': 50}
pocion = {'(P) Poción de vida': 20}
tienda = [armas, armadura, pocion]
print(tienda[0])"""


# Fun_Tienda()
# Esta función consta de listas dentro de lista principal y se accede a ella dependiendo de la posición.

def Fun_Tienda():
    print("¡Bienvenido a la tienda!\n¿Qué te gustaría comprar?")
    Fun_Tienda = True
    while Fun_Tienda == True:
        numero_tienda_lista = int(input("Introduzca el número de lo que desee:\n1) Armas \n2) Armadura \n3) Pociones "
                                        "\n4) Salir \nNúmero: "))
        if numero_tienda_lista == 1:
            print(tienda[0])
            numero_tienda_sublista = str(input("Introduzca la letra dentro del paréntesis de lo que desee: "))
            if numero_tienda_sublista == 'EM':
                print('La espada mágica cuesta: 200 monedas')
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 200
                    print("¡Gracias por tu compra, aquí tiene su espada mágica!")
                    # dar objeto a la mochila del personaje


            elif numero_tienda_sublista == 'E':
                print(f'La espada cuesta: 10 monedas')
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 10
                    print("¡Gracias por tu compra, aquí tiene su espada!")
                    # insertar algo que se la de a la función del personaje

            elif numero_tienda_sublista == 'H2':
                print(f'El hacha de dos manos cuesta: 30 monedas')
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 30
                    print("¡Gracias por tu compra, aquí tiene su hacha de dos manos!")
                    # insertar algo que se la de a la función del personaje

            elif numero_tienda_sublista == 'S':
                print(f'El escudo cuesta: 10 monedas')
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 10
                    print("¡Gracias por tu compra, aquí tiene su escudo!")
                    # insertar algo que se la de a la función del personaje

            else:
                print("No disponemos de esa arma en la tienda, vuelva a seleccionarlo.")
                continue

        elif numero_tienda_lista == 2:
            print(tienda[1])
            numero_tienda_sublista = str(input("Introduzca la letra dentro del paréntesis de lo que desee: "))
            if numero_tienda_sublista == 'A1':
                print(f'La armadura nivel 1 cuesta: 30 monedas')
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 30
                    print("¡Gracias por tu compra, aquí tiene su armadura nivel 1!")
                    # insertar algo que se la de a la función del personaje

            elif numero_tienda_sublista == 'A2':
                print(f'La armadura nivel 2 cuesta: 40 monedas')
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 40
                    print("¡Gracias por tu compra, aquí tiene su armadura nivel 2!")
                    # insertar algo que se la de a la función del personaje

            elif numero_tienda_sublista == 'A3':
                print(f'La armadura nivel 3 cuesta: 50 monedas')
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
                if numero_de_compra == 1:
                    cuenta_bancaria = cuenta_bancaria - 50
                    print("¡Gracias por tu compra, aquí tiene su armadura nivel 3!")
                    # insertar algo que se la de a la función del personaje

            else:
                print("No disponemos de esa armadura en la tienda, vuelva a seleccionarlo.")
                continue

        elif numero_tienda_lista == 3:
            print(tienda[2])
            print(f'La pocion de vida cuesta: 20 monedas')
            numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))
            if numero_de_compra == 1:
                # aqui se resta del dinero de la mochila #
                print("¡Gracias por tu compra, aquí tiene su armadura nivel 1!")
                # insertar algo que se la de a la función del personaje

            else:
                print("No disponemos de esa pocion en la tienda, vuelva a seleccionarlo.")
                continue

        elif numero_tienda_lista == 4:
            print("Hasta pronto, espero verlo de nuevo")
            break

        else:
            print("No tenemos eso en la tienda, ¡vuelva a introducir un número válido!")
        continue


tienda = [['(EM) Espada Mágica', '(E) Espada', '(H2) Hacha dos manos', '(S) Escudo'],
          ['(A1) Armadura nivel 1', '(A2) Armadura nivel 2', '(A3) Armadura nivel 3'], ['(P) Poción de vida']]
# print(tienda[0])
Fun_Tienda()