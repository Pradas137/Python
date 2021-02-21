import random
productes = [
(41419, 'Fideus', 0.75, 210),
(70717, 'Quadern', 1.5, 119),
(78714, 'Sabó', 2.34, 708),
(30877, 'Desodorant', 2.5, 79),
(47470, 'Iogurt', 0.43, 832),
(50809, 'Pomes', 0.56, 55),
(75466, 'Galetes', 2.35, 0),
(33692, 'Beguda', 0.81, 20),
(89148, 'Arròs', 1.48, 121),
(66194, 'Llapis', 1, 900),
(15982, 'Llet', 1.6, 40),
(41235, 'xocolate', 3.75, 48),
]

def imprimir(lista,cantidad):
    lista1 = random.choices(lista, k=cantidad)
    lista2 = random.choices(lista, k=cantidad)
    print(lista1)
    print(lista2)

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
    print ("1. Inserir producte al magatzem")
    print ("2. Inserir clients")
    print ("3. Producte més car")
    print ("4. Preu total que costa tots els productes del magatzem")
    print ("5. Ingrés total por vendes")
    print ("6. Producte amb més ingressos")
    print ("7. Client que més ha gastat")
    print ("8. Total de vendes del mes")
    print ("9. Data última venda producte")
    print ("-------> 10. Crear listas de productos aleatorias <--------")
    print ("0. Salir")
    print ("Elige una opcion")
    opcion = pedirNumeroEntero()
    if opcion == 1:
        print("opcion1")
        id = int(input("Escrive un codigo:"))
        nombre = input("Escrive un nombre:")
        precio = float(input("Escrive un prexio:"))
        stock = int(input("Escrive cantidad del producto:"))
        anadir_elemento(productes,id,nombre,precio,stock)
    elif opcion == 2:
        print("opcion2")
    elif opcion == 3:
        print("opcion3")
    elif opcion == 4:
        print("opcion4")
    elif opcion == 5:
        print("opcion5")
    elif opcion == 6:
        print("opcion6")
    elif opcion == 7:
        print("opcion7")
    elif opcion == 8:
        print("opcion8")
    elif opcion == 9:
        print("opcion9")
    elif opcion == 10:
        print("opcion10")
        cantidad = int(input("Escrive la cantidad de productos que compraras: "))
        print(imprimir(productes,cantidad))
    elif opcion == 0:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 10")
print ("Fin")
