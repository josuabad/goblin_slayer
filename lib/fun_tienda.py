import time
# import artículos
import config_habilidades
import features


# Esta función se basa en el modelo de una "tienda". Consta de comprar y vender artículos que se guardarán o retirarán
# de dos partes; el inventario y el bolsillo.
# Parámetros de entrada: inventario, bolsillo y habilidades.
# Parámetros de salida: inventario, bolsillo y habilidades.


def fun_tienda(inventario, bolsillo, habilidad, puntos):  # Fun_Tienda()
    print("========================================")
    print("    ¡Bienvenido a la tienda jugador!\n========================================\n")  # La bienvenida a la tienda.
    print(f'-------- Tienes: {bolsillo.get("monedas")} Monedas --------\n')
    print("¿Qué te gustaría comprar?")
    time.sleep(0.5)
    while True:  # Bucle para que esté dentro de la tienda hasta que quiera SALIR.
        tienda = [['(EM) Espada Mágica', '(E) Espada', '(H2) Hacha dos manos'],
                  ['(S) Escudo', '(A1) Armadura nivel 1', '(A2) Armadura nivel 2', '(A3) Armadura nivel 3'],
                  ['(P) Poción de vida']]
        # lista de [tienda], tiene sublistas, se acceden a través de la posición donde estén.
        numero_tienda_lista = int(input("Introduzca el número de lo que desee:\n1) Armas\n2) Protección\n3) Pociones "
                                        "\n4) Vender\n5) Salir\nNúmero: "))
        # Variable para ver que quieres de la tienda
        time.sleep(1)
        if numero_tienda_lista == 1:  # Si la variable es igual a 1 escogiste arma.
            input('Presiona ENTER para continuar...')
            print(f'Tenemos estas armas a la venta\n{tienda[0]}')  # Aquí imprime la posición 0 de la lista, y esa es
            # otra lista que contiene todas las armas.
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
                    medidor = features.medidor_de_bolsillos(bolsillo)
                    if medidor == True:
                        if bolsillo.get("monedas") >= 200:  # Aquí evalúa si tiene las 200 monedas
                            bolsillo.update({"monedas": bolsillo.get("monedas") - 200})  # Obtiene las monedas y las
                            # resta
                            bolsillo['espada magica']['cantidad'] += 1
                            # Le suma 1 al valor de la clave del diccionario
                            print("¡Gracias por tu compra, aquí tiene su espada mágica!")  # Agradecimiento
                            input('Presiona ENTER para continuar...')
                            print(f"--> Actualmente tienes: {bolsillo['espada magica']['cantidad']} Espadas Mágicas")
                            # Indica la cantidad que hay en la mochila de ese objeto
                            print(f"--> Te quedan: {bolsillo.get('monedas')} Monedas")
                            # Te recuerda cuantas monedas te quedan
                            continue
                        else:  # Si no tiene las 200 monedas.
                            print(f'Vaya parece que no tienes suficientes monedas.\nDispones de '
                                  f'{bolsillo.get("monedas")}.\nVuelve cuando tengas las 200. ¡Hasta pronto!')
                            time.sleep(2)
                            features.borrar_pantalla()
                            continue  # Lo devuelve a la tienda
                    elif medidor == False:
                        print("Ohhh no...")
                        print("No tienes espacio en tu bolsillo, te sugiero que vendas algo en la sección de Vender.")
                        continue
                elif numero_de_compra == 2:  # Si desea comprar otra cosa
                    features.borrar_pantalla()
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue
                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    time.sleep(1)
                    features.borrar_pantalla()
                    continue
            elif numero_tienda_sublista.upper() == 'E':  # Si colocas las letras E, pides la espada.
                print(f'La espada cuesta: 10 monedas')  # Aquí te imprime cuanto cuesta la espada.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    medidor = features.medidor_de_bolsillos(bolsillo)
                    if medidor == True:
                        if bolsillo.get("monedas") >= 10:  # Aquí evalúa si tiene las 10 monedas
                            bolsillo.update({"monedas": bolsillo.get("monedas") - 10})
                            bolsillo['espada']['cantidad'] += 1
                            print("¡Gracias por tu compra, aquí tiene su espada!")  # Agradecimiento
                            input('Presiona ENTER para continuar...')
                            print(f"--> Actualmente tienes: {bolsillo['espada']['cantidad']} Espadas")
                            print(f"--> Te quedan: {bolsillo.get('monedas')} Monedas")
                            continue
                        else:  # Si no tiene las 200 monedas.
                            print(f'Vaya parece que no tienes suficientes monedas.\nDispones de '
                                  f'{bolsillo.get("monedas")}.\nVuelve cuando tengas las 10 monedas. ¡Hasta pronto!')
                            time.sleep(2)
                            features.borrar_pantalla()
                            continue  # Lo devuelve a la tienda
                    elif medidor == False:
                        print("Ohhh no...")
                        print("No tienes espacio en tu bolsillo, te sugiero que vendas algo en la sección de Vender.")
                        continue
                elif numero_de_compra == 2:  # Si desea comprar otra cosa
                    features.borrar_pantalla()
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue
                else:  # ingreso un número que no es opción
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    time.sleep(1)
                    features.borrar_pantalla()
                    continue
            elif numero_tienda_sublista.upper() == 'H2':  # Si colocas las letras H2, pides el hacha de dos manos.
                print(f'El hacha de dos manos cuesta: 30 monedas')  # Aquí te imprime cuanto cuesta el hacha de dos
                # manos.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    medidor = features.medidor_de_bolsillos(bolsillo)
                    if medidor == True:
                        if bolsillo.get("monedas") >= 30:  # Aquí evalúa si tiene las 10 monedas
                            bolsillo.update({"monedas": bolsillo.get("monedas") - 30})
                            bolsillo['hacha dos manos']['cantidad'] += 1
                            print("¡Gracias por tu compra, aquí tiene su hacha de dos manos!")  # Agradecimiento
                            input('Presiona ENTER para continuar...')
                            print(f'--> Actualmente tienes: {bolsillo["hacha dos manos"]["cantidad"]} hacha de dos '
                                  f'manos')
                            print(f"--> Te quedan: {bolsillo.get('monedas')} Monedas")
                            continue
                        else:  # Si no tiene las 200 monedas.
                            print(f'Vaya parece que no tienes suficientes monedas.\nDispones de '
                                  f'{bolsillo.get("monedas")}.\nVuelve cuando tengas las 30 monedas. ¡Hasta pronto!')
                            time.sleep(2)
                            features.borrar_pantalla()
                            continue  # Lo devuelve a la tienda
                    elif medidor == False:
                        print("Ohhh no...")
                        print("No tienes espacio en tu bolsillo, te sugiero que vendas algo en la sección de Vender.")
                        continue
                elif numero_de_compra == 2:  # Si desea comprar otra cosa
                    features.borrar_pantalla()
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue
                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    time.sleep(1)
                    features.borrar_pantalla()
                    continue
            else:
                print("No disponemos de esa arma en la tienda, vuelva a seleccionarlo.")
                continue
        elif numero_tienda_lista == 2:  # Si la variable es igual a 2 escogiste armadura.
            time.sleep(0.5)
            print(f'Tenemos estas armas a la venta\n{tienda[1]}')
            input('Presiona ENTER para continuar...')
            numero_tienda_sublista = str(input("Introduzca la letra dentro del paréntesis de lo que desee: "))
            if numero_tienda_sublista.upper() == 'S':  # Si colocas la letra S, pides el escudo.
                print(f'El escudo cuesta: 10 monedas')  # Aquí te imprime cuanto cuesta el escudo.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    medidor = features.medidor_de_bolsillos(bolsillo)
                    if medidor == True:
                        if bolsillo.get("monedas") >= 10:  # Aquí evalúa si tiene las 10 monedas
                            bolsillo.update({"monedas": bolsillo.get("monedas") - 10})
                            bolsillo['escudo']['cantidad'] += 1
                            print("¡Gracias por tu compra, aquí tiene su escudo!")  # Agradecimiento
                            input('Presiona ENTER para continuar...')
                            print(f"--> Actualmente tienes: {bolsillo['escudo']['cantidad']} Escudos")
                            # Le muestra que tiene del objeto que mostró
                            print(f"--> Te quedan: {bolsillo.get('monedas')} Monedas")
                            time.sleep(1)
                            print("¡Enhorabuena! Por comprar un escudo te han dado 1 punto más para tu defensa. "
                                  "Suma tu punto")
                            config_habilidades.nuevo_punto(habilidad, 'destreza', 1, puntos)
                            continue
                        else:  # Si no tiene las 200 monedas.
                            print(f'Vaya parece que no tienes suficientes monedas.\nDispones de '
                                  f'{bolsillo.get("monedas")} .\nVuelve cuando tengas las 10 monedas.')
                            time.sleep(2)
                            features.borrar_pantalla()
                            continue  # Lo devuelve a la tienda
                    elif medidor == False:
                        print("Ohhh no...")
                        print("No tienes espacio en tu bolsillo, te sugiero que vendas algo en la sección de Vender.")
                        continue
                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue
                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    time.sleep(1)
                    features.borrar_pantalla()
                    continue
            elif numero_tienda_sublista.upper() == 'A1':  # Si colocas las letras A1, pides armadura nivel 1.
                print(f'La armadura nivel 1 cuesta: 30 monedas')  # Aquí te imprime cuanto cuesta la armadura nivel 1.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    medidor = features.medidor_de_bolsillos(bolsillo)
                    if medidor == True:
                        if bolsillo.get("monedas") >= 30:  # Aquí evalúa si tiene las 10 monedas
                            bolsillo.update({"monedas": bolsillo.get("monedas") - 30})
                            bolsillo['armadura nivel 1']['cantidad'] += 1
                            print("¡Gracias por tu compra, aquí tiene su armadura nivel 1!")  # Agradecimiento
                            input('Presiona ENTER para continuar...')
                            print(f"--> Actualmente tienes {bolsillo['armadura nivel 1']['cantidad']} Armadura nivel 1")
                            print(f"--> Te quedan: {bolsillo.get('monedas')} Monedas")
                            config_habilidades.nuevo_punto(habilidad, 'destreza', 2, puntos)
                            continue
                        else:  # Si no tiene las 200 monedas.
                            print(f'Vaya parece que no tienes suficientes monedas.\nDispones de '
                                  f'{bolsillo.get("monedas")} .\nVuelve cuando tengas las 30 monedas. ¡Hasta pronto!')
                            time.sleep(2)
                            features.borrar_pantalla()
                            continue  # Lo devuelve a la tienda
                    elif medidor == False:
                        print("Ohhh no...")
                        print("No tienes espacio en tu bolsillo, te sugiero que vendas algo en la sección de Vender.")
                        continue
                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue
                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    time.sleep(1)
                    features.borrar_pantalla()
                    continue
            elif numero_tienda_sublista.upper() == 'A2':  # Si colocas las letras A2, pides la armadura nivel 2.
                print(f'La armadura nivel 2 cuesta: 40 monedas')  # Aquí te imprime cuanto cuesta la armadura nivel 2.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    medidor = features.medidor_de_bolsillos(bolsillo)
                    if medidor == True:
                        if bolsillo.get("monedas") >= 40:  # Aquí evalúa si tiene las 10 monedas
                            bolsillo.update({"monedas": bolsillo.get("monedas") - 40})
                            # Si tiene las monedas, las resta de su inventario
                            bolsillo['armadura nivel 2']['cantidad'] += 1
                            # le suma el objeto que adquirió a su inventario
                            print("¡Gracias por tu compra, aquí tiene su armadura nivel 2!")  # Agradecimiento
                            input('Presiona ENTER para continuar...')
                            print(f"--> Actualmente tienes: {bolsillo['armadura nivel 2']['cantidad']} Armadura nivel "
                                  f"2")
                            print(f"--> Te quedan: {bolsillo.get('monedas')} Monedas")
                            config_habilidades.nuevo_punto(habilidad, 'destreza', 3, puntos)  # Por adquirir protección,
                            # pues le suma puntos a su destreza
                            continue
                        else:  # Si no tiene las 200 monedas.
                            print(f'Vaya parece que no tienes suficientes monedas.\nDispones de '
                                  f'{bolsillo.get("monedas")} .\nVuelve cuando tengas las 40 monedas. ¡Hasta pronto!')
                            time.sleep(2)
                            features.borrar_pantalla()
                            continue  # Lo devuelve a la tienda
                    elif medidor == False:
                        print("Ohhh no...")
                        print("No tienes espacio en tu bolsillo, te sugiero que vendas algo en la sección de Vender.")
                        continue
                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue
                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    time.sleep(1)
                    features.borrar_pantalla()
                    continue
            elif numero_tienda_sublista.upper() == 'A3':  # Si colocas las letras A3, pides la armadura nivel 3.
                print(f'La armadura nivel 3 cuesta: 50 monedas')  # Aquí te imprime cuanto cuesta la armdura nivel 3.
                time.sleep(0.5)
                numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
                # verificar si quieres hacer la compra.
                if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                    medidor = features.medidor_de_bolsillos(bolsillo)
                    if medidor == True:
                        if bolsillo.get("monedas") >= 50:  # Aquí evalúa si tiene las 10 monedas
                            bolsillo.update({"monedas": bolsillo.get("monedas") - 50})
                            bolsillo['armadura nivel 3']['cantidad'] += 1
                            print("¡Gracias por tu compra, aquí tiene su armadura nivel 3!")  # Agradecimiento
                            input('Presiona ENTER para continuar...')
                            print(f"--> Actualmente tienes: {bolsillo['armadura nivel 3']['cantidad']} Armadura nivel "
                                  f"3")
                            print(f"--> Te quedan: {bolsillo.get('monedas')} Monedas")
                            config_habilidades.nuevo_punto(bolsillo, 'destreza', 4, puntos)
                            continue
                        else:  # Si no tiene las 200 monedas.
                            print(f'Vaya parece que no tienes suficientes monedas.\nDispones de '
                                  f'{bolsillo.get("monedas")}.\nVuelve cuando tengas las 50 monedas. ¡Hasta pronto!')
                            time.sleep(2)
                            features.borrar_pantalla()
                            continue  # Lo devuelve a la tienda
                    elif medidor == False:
                        print("Ohhh no...")
                        print("No tienes espacio en tu bolsillo, te sugiero que vendas algo en la sección de Vender.")
                        continue
                elif numero_de_compra == 2:
                    print("\nVale, ¿desea comprar otra cosa?\n")
                    time.sleep(0.5)
                    continue
                else:
                    print("Esa opción no es válida, ¡vuela a introducir otra!")
                    time.sleep(1)
                    features.borrar_pantalla()
                    continue
            else:
                print("No disponemos de esa armadura en la tienda, vuelva a seleccionarlo.")
                time.sleep(1)
                continue
        elif numero_tienda_lista == 3:  # Si la variable es igual a 3 escogiste poción.
            print(f'Tenemos esta poción a la venta\n{tienda[2]}')  # Aquí imprime la posición 0 de la lista, y esa es
            # otra lista que contiene todas las armas.
            print(f'La poción de vida cuesta: 20 monedas')  # Aquí te imprime cuanto cuesta la poción.
            time.sleep(0.5)
            numero_de_compra = int(input("Deseas comprarla: \n1) Sí \n2) No \nTu opción es: "))  # Variable para
            # verificar si quieres hacer la compra.
            if numero_de_compra == 1:  # Indicas 1 si quieres la compra.
                medidor = features.medidor_de_bolsillos(bolsillo)
                if medidor == True:
                    if bolsillo.get("monedas") >= 20:  # Aquí evalúa si tiene las 10 monedas
                        bolsillo.update({"monedas": bolsillo.get("monedas") - 20})
                        bolsillo['pocion de vida']['cantidad'] += 1
                        print("¡Gracias por tu compra, aquí tiene su poción de vida!")  # Agradecimiento
                        input('Presiona ENTER para continuar...')
                        print(f"--> Actualmente tienes {bolsillo['pocion de vida']['cantidad']} Poción de vida")
                        print(f"--> Te quedan: {bolsillo.get('monedas')} Monedas")
                        continue
                    else:  # Si no tiene las 200 monedas.
                        print(f'Vaya parece que no tienes suficientes monedas.\nDispones de {bolsillo.get("monedas")} .'
                              f'\nVuelve cuando tengas las 20 monedas. ¡Hasta pronto!')
                        time.sleep(2)
                        features.borrar_pantalla()
                        continue  # Lo devuelve a la tienda
                elif medidor == False:
                    print("Ohhh no...")
                    print("No tienes espacio en tu bolsillo, te sugiero que vendas algo en la sección de Vender.")
                    continue
            elif numero_de_compra == 2:
                print("\nVale, ¿desea comprar otra cosa?\n")
                time.sleep(0.5)
                continue
            else:
                print("No disponemos de esa pocion en la tienda, vuelva a seleccionarlo.")  # Aquí es por si
                # introduce una poción que no exista.
                time.sleep(1)
                features.borrar_pantalla()
                continue  # Aquí lo devuelve a que quiere de pociones.
        elif numero_tienda_lista == 4:  # Si la variable es 4, pues has decidido vender
            while True:
                print("-------------------------------------")
                print("          Bienvenido player\n")
                print(" - Estas en la sección de venta\n")
                vender_tienda = int(input("¿Qué quieres hacer?\n"
                                          "1) Vender\n"
                                          "2) Volver a tienda\n"
                                          "---> Introduce el número: "))
                print("-------------------------------------\n")
                time.sleep(0.5)
                if vender_tienda == 1:
                    print("Vale, quieres venderme un artículo. Muéstrame  que traes.\n")
                    time.sleep(1)
                    input('Presiona ENTER para continuar...')
                    origen = str(input("Donde está el objeto que quieres vender?\n"
                                       "---> Bolsillo\n"
                                       "---> Inventario\n"
                                       "Introduce el lugar [i/b]: "))
                    time.sleep(1)
                    features.borrar_pantalla()
                    while True:
                        if origen.lower() == 'b':
                            print("-------------------------------------\n")
                            print(f'Tienes estos objetos para vender en tu bolsillo: ')
                            print("-------------------------------------\n")
                            print(f'Objeto:\n')
                            for element in bolsillo:
                                print(element, "\n")
                                continue
                            print("-------------------------------------\n")
                            input('Presiona ENTER para continuar...\n')
                            venta_obj = input(f'¿Cuál objeto quieres vender de tu bolsillo?\n'
                                              f'(ingresa "s" si quieres salir)\n'
                                              f'Ingresa el nombre del objeto: ')
                            if venta_obj.lower() == 's':
                                print("Regresemos...")
                                time.sleep(2)
                                features.borrar_pantalla()
                                break
                            elif venta_obj == 'monedas':
                                print("Jugador, no puedes venderme tus monedas, elige otra vez.")
                                continue
                            elif venta_obj == 'puños':
                                print("Jugador, no puedes venderme tus puños, te quedas sin manos. Elige otra vez")
                                continue
                            elif venta_obj in bolsillo:
                                time.sleep(1)
                                if bolsillo[venta_obj]["cantidad"] >= 1:
                                    print(f'Tienes {bolsillo[venta_obj]["cantidad"]} {venta_obj}')
                                    num_venta = int(input("¿Cuántas quieres vender?\n"
                                                          "---> Introduce el número: "))
                                    if num_venta > bolsillo[venta_obj]["cantidad"]:
                                        print("Estas introduciendo un numero mayor al posible")
                                        continue
                                    else:
                                        print(f'Muy bien, te compraré: {num_venta} {venta_obj}')
                                        time.sleep(2)
                                        bolsillo.update({'monedas': bolsillo.get('monedas') + bolsillo[venta_obj][
                                            'venta'] * num_venta})
                                        print(f'Aquí tienes tu {bolsillo[venta_obj]["venta"] * num_venta} monedas')
                                        print(f'Muy bien jugador, ahora tienes {bolsillo.get("monedas")} monedas')
                                        bolsillo[venta_obj]['cantidad'] -= num_venta
                                        print(f'Ahora tienes {bolsillo[venta_obj]["cantidad"]} {venta_obj}')
                                        time.sleep(2)
                                        features.borrar_pantalla()
                                        break
                                elif bolsillo[venta_obj]["cantidad"] < 1:
                                    time.sleep(0.5)
                                    print(f"No tienes {venta_obj} para vender")
                                    print("Ve tu bolsa de nuevo y dime algo que si tengas.")
                                    time.sleep(2)
                                    features.borrar_pantalla()
                                    continue
                            elif venta_obj not in bolsillo:
                                time.sleep(0.5)
                                print("Lo siento ese objeto no está en tu bolsa, ingresa otro de nuevo...")
                                time.sleep(2)
                                features.borrar_pantalla()
                                continue
                        if origen.lower() == 'i':
                            print("-------------------------------------\n")
                            print(f'Tienes estos objetos para vender en tu inventario: ')
                            print("-------------------------------------\n")
                            print(f'Objeto:\n')
                            for element in inventario:
                                print(element, "\n")
                                continue
                            print("-------------------------------------\n")
                            input('Presiona ENTER para continuar...')
                            venta_obj = input(f'¿Cuál objeto quieres vender de tu inventario?\n'
                                              f'(ingresa "s" si quieres salir)\n'
                                              f'Ingresa el nombre del objeto: ')
                            if venta_obj.lower() == 's':
                                print("Regresemos...")
                                time.sleep(2)
                                features.borrar_pantalla()
                                break
                            elif venta_obj in inventario:
                                time.sleep(1)
                                if inventario[venta_obj]["cantidad"] >= 1:
                                    print(f'Tienes {inventario[venta_obj]["cantidad"]} {venta_obj}')
                                    num_venta = int(input("¿Cuántas quieres vender?\n"
                                                          "---> Introduce el número: "))
                                    if num_venta > inventario[venta_obj]["cantidad"]:
                                        print("Estas introduciendo un numero mayor al posible")
                                        continue
                                    else:
                                        print(f'Muy bien, te compraré: {num_venta} {venta_obj}')
                                        time.sleep(2)
                                        bolsillo.update({'monedas': bolsillo.get('monedas') + inventario[venta_obj][
                                            'venta'] * num_venta})
                                        print(f'Aquí tienes tus {inventario[venta_obj]["venta"]} monedas')
                                        print(f'Muy bien jugador, ahora tienes {bolsillo.get("monedas")} monedas')
                                        inventario[venta_obj]['cantidad'] -= num_venta
                                        print(f'Ahora tienes {inventario[venta_obj]["cantidad"]} {venta_obj}')
                                        time.sleep(2)
                                        features.borrar_pantalla()
                                        break
                                elif inventario[venta_obj]["cantidad"] < 1:
                                    time.sleep(0.5)
                                    print(f"No tienes {venta_obj} para vender")
                                    print("Ve tu inventario de nuevo y dime algo que si tengas.")
                                    time.sleep(2)
                                    features.borrar_pantalla()
                                    continue
                            elif venta_obj not in inventario:
                                time.sleep(0.5)
                                print("Lo siento ese objeto no está en tu mochila, ingresa otro de nuevo...")
                                time.sleep(2)
                                features.borrar_pantalla()
                                continue

                elif vender_tienda == 2:
                    time.sleep(0.5)
                    print("Hasta pronto, ven cuando quieras a la sección de venta")
                    input('Presiona ENTER para continuar...')
                    print("Regresando a tienda...")
                    time.sleep(2)
                    features.borrar_pantalla()
                    break
                else:
                    print("No tenemos esa opción en la sección de vender, ¡inténtalo de nuevo!")
                    time.sleep(1)
                    features.borrar_pantalla()
                    continue
        elif numero_tienda_lista == 5:
            time.sleep(0.5)  # Si la variable es igual a 5 es porque escogiste salir.
            print("Hasta pronto, espero verlo de nuevo\n")  # Despedida.
            time.sleep(1)
            return bolsillo, bolsillo, habilidad, puntos
        else:
            print("No tenemos eso en la tienda, ¡vuelva a introducir un número válido!\n")  # Esto es por si el jugador
            # introduce algo que no está
            time.sleep(1)
            features.borrar_pantalla()
            continue  # Aquí te devuelve al menú de la tienda
    return bolsillo, bolsillo, habilidad, puntos

