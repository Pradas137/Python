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

productos = [
(41419, 'Fideus', 'Eco', 0.75, 210),
(70717, 'Quadern', 'Bio', 1.5, 119),
(78714, 'Sabó', 'Eco', 2.34, 708),
(30877, 'Desodorant', 'Eco', 2.5, 79),
(47470, 'Iogurt', 'Bio', 0.43, 832),
(50809, 'Pomes', 'Eco', 0.56, 55),
(75466, 'Galetes', 'Eco', 2.35, 0),
(33692, 'Beguda', 'Bio', 0.81, 20),
(89148, 'Arròs', 'Bio', 1.48, 121),
(66194, 'Llapis', 'Eco', 1, 900),
(15982, 'Llet', 'Bio', 1.6, 40),
(41235, 'xocolate', 'Eco', 3.75, 48),
]

def imprimir(lista,cantidad):
    lista1 = random.choices(lista, k=cantidad)
    lista2 = random.choices(lista, k=cantidad)
    print(lista1)
    print(lista2)

def aumentarPrecio(lista):
    print(lista)
    res = sorted(lista,key=lambda p: float(p[2]*1.20))
    print(res)
    print(max(res))

def bioEco(lista):
    #print(lista)
    for p in lista:
        if p[2] == "Eco":
            #print("ECO")
            eco = p[3]*0.25*p[4]
            #print(eco)
        elif p[2] == "Bio":
            #print("BIO")
            bio = p[3]*0.45*p[4]
            #print(bio)
    sumaEco=0
    sumaBio=0
    sumaEco+=eco
    print(sumaEco)
    sumaBio+=bio
    if sumaBio>sumaEco:
        print('Los BIO es mayor que ECO: ',sumaBio)
    elif sumaBio<sumaEco:
        print('Los ECO es mayor que BIO: ', sumaEco)
    else:
        print('Tanto ECO como BIO son iguales ')

def eliminar(lista):
    lista = [x for x in lista if x!= (41419, 'Fideus', 'Eco', 0.75, 210)]
    print(lista)

def Modificar(lista):
    index = -1
    target = int(input("Escrive id: "))
    new_value = "Gato"
    for i, v in enumerate(lista):
        if v[0] == target:
            index = i
            break
        if index >= 0:
            lista[index] = (lista[index][2], new_value)
    print(lista)
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
    """print ("1. Inserir producte al magatzem")
    print ("2. Inserir clients")
    print ("3. Producte més car")
    print ("4. Preu total que costa tots els productes del magatzem")
    print ("5. Ingrés total por vendes")
    print ("6. Producte amb més ingressos")
    print ("7. Client que més ha gastat")
    print ("8. Total de vendes del mes")
    print ("9. Data última venda producte")"""
    print ("-------> 1. Crear listas de productos aleatorias <--------")
    print ("-------> 2. Aumentar 1.20% el precio <--------")
    print ("-------> 3. Productos Bio y Eco <--------")
    print ("-------> 4. Eliminar <--------")
    print ("-------> 5. Modificar <--------")

    print ("0. Salir")
    print ("Elige una opcion")
    opcion = pedirNumeroEntero()
    if opcion == 1:
        print("1. Crear listas de productos aleatorias")
        cantidad = int(input("Escrive la cantidad de productos que compraras: "))
        print(imprimir(productes,cantidad))
    elif opcion == 2:
        print("2. Aumentar 1.20% el precio")
        print(aumentarPrecio(productes))
    elif opcion == 3:
        print("3. Productos Bio y Eco")
        print(bioEco(productos))
    elif opcion == 4:
        print("4. Eliminar")
        print(eliminar(productos))
    elif opcion == 5:
        print("5. Modificar")
        print(Modificar(productos))
    elif opcion == 0:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 10")
print ("Fin")
