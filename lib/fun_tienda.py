import time


def fun_tienda(mochila, bolsa):  # Fun_Tienda()
    print("¡Bienvenido a la tienda jugador!\n¿Qué te gustaría comprar?")  # La bienvenida a la tienda.
    while True:  # Bucle para que esté dentro de la tienda hasta que quiera SALIR.
        tienda = [['(EM) Espada Mágica', '(E) Espada', '(H2) Hacha dos manos', '(S) Escudo'],
                  ['(A1) Armadura nivel 1', '(A2) Armadura nivel 2', '(A3) Armadura nivel 3'], ['(P) Poción de vida']]
        # lista de [tienda], tiene sublistas, se acceden a través de la posición donde estén.
        numero_tienda_lista = int(input("Introduzca el número de lo que desee:\n1) Armas\n2) Armadura\n3) Pociones "
                                        "\n4) Vender\n5) Salir\nNúmero: "))
        # Variable para ver que quieres de la tienda
        time.sleep(1)
        if numero_tienda_lista == 1:  # Si la variable es igual a 1 escogiste arma.
            input('Presiona ENTER para continuar...')
            print(tienda[0])  # Aquí imprime la posición 0 de la lista, y esa es otra lista que contiene todas las
            # armas.
            input('Presiona ENTER para continuar...')
            numero_tienda_sublista = str(input("Introduzca la letra dentro del paréntesis de lo que desee: "))  # Aqu
            # í tienes que especificar que arma quieres colocando la letra dentro del paréntesis
            if numero_tienda_sublista.upper() == 'EM':  # Si colocas las letras EM, pides la espada mágica.
                time.sleep(1)
                print(f'La espada mágica cuesta: 200 monedas')  # Aquí te imprime cuanto cuesta la espada mágica.
                input('Presiona ENTER para continuar...')
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    # Aquí se le resta a la mochila en la sección de monedas - 200
                    if mochila.get("monedas") >= 200:  # Aquí evalúa si tiene las 200 monedas
                        mochila.update({"monedas": mochila.get("monedas") - 200})  # Obtiene las monedas y las resta
                        mochila['espada magica']['cantidad'] += 1
                        # Le suma 1 al valor de la clave del diccionario
                        print("¡Gracias por tu compra, aquí tiene su espada mágica!")  # Agradecimiento
                        print(f"--> Actualmente tienes: {mochila['espada magica']['cantidad']} Espadas Mágicas")
                        # Indica la cantidad que hay en la mochila de ese objeto
                        print(f"--> Te quedan: {mochila.get('monedas')} Monedas")
                        # Te recuerda cuantas monedas te quedan
                        continue
                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("monedas")} .'
                              f'\nVuelve cuando tengas las 200. ¡Hasta pronto!')
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
                    if mochila.get("monedas") >= 10:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"monedas": mochila.get("monedas") - 10})
                        mochila['espada']['cantidad'] += 1
                        print("¡Gracias por tu compra, aquí tiene su espada!")  # Agradecimiento
                        print(f"--> Actualmente tienes: {mochila['espada']['cantidad']} Espadas")
                        print(f"--> Te quedan: {mochila.get('monedas')} Monedas")
                        continue
                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("monedas")} .'
                              f'\nVuelve cuando tengas las 10 monedas. ¡Hasta pronto!')
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
                    if mochila.get("monedas") >= 30:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"monedas": mochila.get("monedas") - 30})
                        mochila['hacha dos manos']['cantidad'] += 1
                        print("¡Gracias por tu compra, aquí tiene su hacha de dos manos!")  # Agradecimiento
                        print(f'--> Actualmente tienes: {mochila["hacha dos manos"]["cantidad"]} hacha de dos manos')
                        print(f"--> Te quedan: {mochila.get('monedas')} Monedas")
                        continue
                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("monedas")} .'
                              f'\nVuelve cuando tengas las 30 monedas. ¡Hasta pronto!')
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
                    if mochila.get("monedas") >= 10:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"monedas": mochila.get("monedas") - 10})
                        mochila['escudo']['cantidad'] += 1
                        print("¡Gracias por tu compra, aquí tiene su escudo!")  # Agradecimiento
                        print(f"--> Actualmente tienes: {mochila['escudo']['cantidad']} Escudos")
                        print(f"--> Te quedan: {mochila.get('monedas')} Monedas")
                        continue
                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("monedas")} .'
                              f'\nVuelve cuando tengas las 10 monedas. ¡Hasta pronto!')
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
                    if mochila.get("monedas") >= 30:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"monedas": mochila.get("monedas") - 30})
                        mochila['armadura nivel 1']['cantidad'] += 1
                        print("¡Gracias por tu compra, aquí tiene su armadura nivel 1!")  # Agradecimiento
                        print(f"--> Actualmente tienes {mochila['armadura nivel 1']['cantidad']} Armadura nivel 1")
                        print(f"--> Te quedan: {mochila.get('monedas')} Monedas")
                        continue
                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("monedas")} .'
                              f'\nVuelve cuando tengas las 30 monedas. ¡Hasta pronto!')
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
                    if mochila.get("monedas") >= 40:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"monedas": mochila.get("monedas") - 40})
                        mochila['armadura nivel 2']['cantidad'] += 1
                        print("¡Gracias por tu compra, aquí tiene su armadura nivel 2!")  # Agradecimiento
                        print(f"--> Actualmente tienes: {mochila['armadura nivel 2']['cantidad']} Armadura nivel 2")
                        print(f"--> Te quedan: {mochila.get('monedas')} Monedas")
                        continue
                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("monedas")} .'
                              f'\nVuelve cuando tengas las 40 monedas. ¡Hasta pronto!')
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
                    if mochila.get("monedas") >= 50:  # Aquí evalúa si tiene las 10 monedas
                        mochila.update({"monedas": mochila.get("monedas") - 50})
                        mochila['armadura nivel 3']['cantidad'] += 1
                        print("¡Gracias por tu compra, aquí tiene su armadura nivel 3!")  # Agradecimiento
                        print(f"--> Actualmente tienes: {mochila['armadura nivel 3']['cantidad']} Armadura nivel 3")
                        print(f"--> Te quedan: {mochila.get('monedas')} Monedas")
                        continue
                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("monedas")} .'
                              f'\nVuelve cuando tengas las 50 monedas. ¡Hasta pronto!')
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
                if mochila.get("monedas") >= 20:  # Aquí evalúa si tiene las 10 monedas
                    mochila.update({"monedas": mochila.get("monedas") - 20})
                    mochila['pocion de vida']['cantidad'] += 1
                    print("¡Gracias por tu compra, aquí tiene su poción de vida!")  # Agradecimiento
                    print(f"--> Actualmente tienes {mochila['pocion de vida']['cantidad']} Poción de vida")
                    print(f"--> Te quedan: {mochila.get('monedas')} Monedas")
                    continue
                else:  # Si no tiene las 200 monedas.
                    print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {mochila.get("monedas")} .'
                          f'\nVuelve cuando tengas las 20 monedas. ¡Hasta pronto!')
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
            # input('Presiona ENTER para continuar...')
            origen = str(input("Donde está el objeto que quieres vender?\n"
                               "---> 1) Bolsa\n"
                               "---> 2) Mochila\n"
                               "Introduce el lugar [m/b]: "))
            if origen.lower() == 'b':
                print("-------------------------------------\n")
                print(f'Tienes estos artículos para vender en bolsa: ')
                print("-------------------------------------\n")
                print(f'Objeto              |    Precio para vender    |   Tienes:\n'
                      f'1. espada goblin    |    {bolsa["espada goblin"]["venta"]} monedas             |    '
                      f'  {bolsa["espada goblin"]["cantidad"]}\n'
                      f'2. escudo goblin    |    {bolsa["escudo goblin"]["venta"]} monedas             |    '
                      f'  {bolsa["escudo goblin"]["cantidad"]}\n')
                print("-------------------------------------\n")
                input('Presiona ENTER para continuar...')
                venta_obj = input(f'¿Cuál objeto quieres vender de tu mochila?\n'
                                  f'Ingresa el nombre del objeto: ')
                if venta_obj == 'espada goblin':
                    if bolsa['espada goblin']["cantidad"] >= 1:
                        print(f'Muy bien, te compraré tu espada goblin')
                        mochila.update({'monedas': mochila.get('monedas') - 5})
                        bolsa['espada goblin']['cantidad'] -= 1
                        print(f'Aquí tienes tu dinero [5 monedas] ')
                        print(f'Muy bien jugador, ahora tienes {mochila.get("monedas")} monedas')
                        print(bolsa['espada goblin']['cantidad'])
                        continue
                    elif bolsa['espada goblin']["cantidad"] < 1:
                        print(f"No tienes espadas goblin para vender")
                        print("Ve tu bolsa de nuevo y dime algo que si tengas.")
                        continue
                elif venta_obj == 'escudo goblin':
                    if bolsa['espada goblin']["cantidad"] >= 1:
                        print(f'Muy bien, te compraré tu escudo goblin')
                        mochila.update({'monedas': mochila.get('monedas') - 5})
                        menos_objeto = bolsa['escudo goblin']['cantidad'] - 1
                        print(f'Aquí tienes tu dinero [5 monedas] ')
                        print(f'Muy bien jugador, ahora tienes {mochila.get("monedas")} monedas')
                        print(menos_objeto)
                        continue
                    elif bolsa['escudo goblin']["cantidad"] < 1:
                        print(f"No tienes escudos goblin para vender")
                        print("Ve tu bolsa de nuevo y dime algo que si tengas.")
                        continue
                elif venta_obj not in bolsa:
                    print("Lo siento ese objeto no está en tu mochila, ingresa otro de nuevo...")
                    continue
            if origen.lower() == 'm':
                print("-------------------------------------\n")
                print(f'Tienes estos artículos para vender en mochila: ')
                print("-------------------------------------\n")
                print(f'Objeto              |    Precio para vender    |   Tienes:\n'
                      f'1. Espada           |    {mochila["espada"]["venta"]} monedas           |    '
                      f'  {mochila["espada"]["cantidad"]}\n'
                      f'2. Espada mágica    |    {mochila["espada magica"]["venta"]} monedas         |    '
                      f'  {mochila["espada magica"]["cantidad"]}\n'
                      f'3. Escudo           |    {mochila["escudo"]["venta"]} monedas           |    '
                      f'  {mochila["escudo"]["cantidad"]}\n'
                      f'4. Hacha dos manos  |    {mochila["hacha dos manos"]["venta"]} monedas          |    '
                      f'  {mochila["hacha dos manos"]["cantidad"]}\n')
                print("-------------------------------------\n")
                input('Presiona ENTER para continuar...')
                venta_obj = input(f'¿Cuál objeto quieres vender de tu mochila?\n'
                                  f'Ingresa el nombre del objeto: ')
                if mochila[venta_obj]["cantidad"] >= 1:
                    print(f'Muy bien, te compraré tu {venta_obj}')
                    # vender = {mochila[venta_obj]['venta']}
                    mochila.update({'monedas': mochila.get('monedas') + {mochila[venta_obj]['venta']}})
                    print(f'Aquí tienes tu dinero {mochila[venta_obj]["venta"]}')
                    print(f'Muy bien jugador, ahora tienes {mochila.get("monedas")} monedas')
                    continue
                elif mochila[venta_obj]["cantidad"] < 1:
                    print(f"No tienes {venta_obj} para vender")
                    print("Ve tu mochila de nuevo y dime algo que si tengas.")
                    continue
                elif venta_obj not in mochila:
                    print("Lo siento ese objeto no está en tu mochila, ingresa otro de nuevo...")
                    continue
            # bolsa.update({"poción de vida": bolsa.get("poción de vida") + 1})
            # mochila.update({"Monedas": mochila.get("Monedas") - 20})
        elif numero_tienda_lista == 5:  # Si la variable es igual a 4 es porque escogiste salir.
            print("Hasta pronto, espero verlo de nuevo\n")  # Despedida.
            time.sleep(1)
            return mochila
        else:
            print("No tenemos eso en la tienda, ¡vuelva a introducir un número válido!\n")  # Esto es por si el jugador
            # introduce algo que no está
            time.sleep(1)
        continue  # Aquí te devuelve al menú de la tienda
    return mochila, bolsa


bolsillo = {'espada goblin': {'daño': 6, 'precio': None, 'venta': 5, 'manos': 1, 'arma': True, 'cantidad': 3},
            'escudo goblin': {'precio': None, 'venta': 5, 'destreza': 1, 'protección': True, 'cantidad': 1}}

mochi = {'escudo': {'precio': 10, 'venta': 10 * 0.8, 'destreza': 1, 'protección': True, 'cantidad': 0},
         'espada': {'daño': 8, 'precio': 10, 'venta': 10 * 0.8, 'manos': 1, 'arma': True, 'cantidad': 1},
         'espada magica': {'daño': 6, 'precio': 200, 'venta': 200 * 0.5, 'manos': 1, 'arma': True, 'cantidad': 0},
         'hacha dos manos': {'daño': 12, 'precio': 30, 'venta': 30 * 0.5, 'manos': 2, 'arma': True, 'cantidad': 0},
         'armadura nivel 1': {'precio': 30, 'venta': 30 * 0.5, 'destreza': 2, 'protección': True, 'cantidad': 0},
         'armadura nivel 2': {'precio': 40, 'venta': 40 * 0.5, 'destreza': 3, 'protección': True, 'cantidad': 0},
         'armadura nivel 3': {'precio': 50, 'venta': 50 * 0.5, 'destreza': 4, 'protección': True, 'cantidad': 0},
         'pocion de vida': {'precio': 20, 'venta': 20 * 0.5, 'vida': 2, 'pocion': True, 'cantidad': 0}, 'monedas': 1000
         }

fun_tienda(mochi, bolsillo)  # Llamando a la función tienda

#          NOTAS          #

# 1. Enseñar todas las cosas que tiene (listo)
# 2. Decidir de donde quieres vender algo (bolsa o mochila) (listo)
# 3. Decidir lo que quieres vender [mochila (espada)]  (me falta en mochila)
# 4. Devolver el precio  ---  mochila[venta_obj]['venta']   ---- venta_obj = mochila[pedir]['venta']  (listo)
# 5. Cuántos quieres vender  ---  mochila[venta_obj]['cantidad']   ---- venta_obj = mochila[pedir]['venta']
# 6. Verificar si tiene la cantidad (por lo menos para vender uno) (listo)
# 7. Update el diccionario en cantidad (puede ser o en mochila o bolsa) y en monedas (mochila)


#################################################################################################################
#                                           P R E G U N T A S                                                   #

# 1. En mochila para que reste la venta directa (TypeError: unsupported operand type(s) for +: 'int' and 'set') #
# 2. Los continue cuando vendes algo en bolsa                                                                   #
# 3. Los return para que se actualice la mochila y bolsa                                                        #
#################################################################################################################
