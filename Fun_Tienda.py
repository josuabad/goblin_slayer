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


cuenta_bancaria = 1000  # aquí habría que crear como una cuenta bancaria, en donde vaya acumulando lo que se gana y
# luego restando cuando se va a la tienda
tienda = [['(EM) Espada Mágica', '(E) Espada', '(H2) Hacha dos manos', '(S) Escudo'],
          ['(A1) Armadura nivel 1', '(A2) Armadura nivel 2', '(A3) Armadura nivel 3'], ['(P) Poción de vida']]
# print(tienda[0])
Fun_Tienda()


#          NOTAS          #

# 1) Falta crear una variable que actúe como cuenta bancaria. #
#    * Para esta función tener en cuenta:
#    1.1) Hay que verificar si tiene el dinero.
#    1.2) Si no tiene el dinero imprimir que no lo tiene y devolverlo al menu de la tienda.
#    1.3) En caso de que si lo tenga, restar el dinero de su cuenta o acumulador de dinero.
#
# 2) Falta una función del personaje que actúe como mochila o característica para que guarde lo que compró #