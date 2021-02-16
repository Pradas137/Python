def generar_Menu(*opciones, encabezado="\n"):
    flag_menu = False
    while not flag_menu:
        print(encabezado)
        for i in range(len(opciones)):
            print(i+1, ")", opciones[i])
        try:
            eleccion = int(input("Elige una opción: "))
            if 0 < eleccion <= len(opciones):
                flag_menu = True
                return eleccion
            else:
                print("Opcion Invalida.")
                flag_menu = False
        except ValueError:
            print("Ese no es un número. Vuelve a intentarlo")

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num
salir = False
opcion = 0
while not salir:
    print ("1. Opcion 1")
    print ("2. Opcion 2")
    print ("3. Opcion 3")
    print ("4. Salir")
    print ("Elige una opcion")
    opcion = pedirNumeroEntero()
    if opcion == 1:
        print ("Opcion 1")
        generar_Menu("List by ID", "List by name", "List by Stock", "Back", encabezado='MAIN MENU')
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
# Esta función crea un menú y tiene 2 argumentos:
# opciones: Todas las opciones se envían como tuplas ('Item1', 'Item2', 'Item3', etc.)
# Encabezado: por defecto, el encabezado es solo una nueva línea.
# Para declarar un encabezado, debe hacerse como menu_generator ([elementos del menú], encabezado = 'MENÚ')
# Ejemplo de llamada a función sin encabezado: menu_generator ('item1', 'item2', 'item3')
# Ejemplo de llamada de función con encabezado: menu_generator ('item1', 'item2', 'item3', header = 'MAIN MENU')
# La opción de encabezado DEBE declararse siempre la última, en caso de que se declare.
