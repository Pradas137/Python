flag_menu=False
def preuydescompte(preu, porcentage):
    resultado = preu*porcentage/100
    return resultado

def llegeix1a10 ():
    num = -1
    while num <= 0 or num >=10:
        num = int(input("escrive un numero:"))
    return num

def trueOFalse (c):
   #if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        #return True
    #elif c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
        #return True
    #return False
    if c in "aeiouAEIOU":
        return True
    else:
        return False

def multlista(lista):
    mult=0
    for x in range(len(lista)):
        mult=mult*lista[x]
    return mult

def imprimir_histograma(barras):
    for num in barras:
        print("*" * num)

def ingresar_datos(n):
    lista=[]
    for _ in range(n):
        num = int(input("Introduce num astericos para histograma: "))
        lista.append(num)
    return lista


def contador_minusculas_mayusculas(cadena):
    contador = {'mayusculas': 0}

    for c in cadena:
        if c.isupper():
            contador['mayusculas'] += 1
    return contador

while not flag_menu:
    print("1.-EXERCICI 1\n2.-EXERCICI 2\n3.-EXERCICI 3\n4.-EXERCICI 4\n5.-EXERCICI 5\n6.-EXERCICI 6\n7.-EXERCICI 7\n0.-SORTIR\nEscull una opcio:")
    opcio=int(input())
    if opcio==1:
       # Definiu i programeu una funció que, donats un preu i un percentatge de descompte, ens torni el preu amb
       # el descompte aplicat. La funció té dos paràmetres: preu i percentatge. Retorna el preu amb el descompte
       # aplicat.
        print("EXERCICI 1")
        descuento=30
        precio=float(input("escrive un preci:"))
        print("el precio con descuento es:",preuydescompte(precio,descuento))

    elif opcio==2:
        print("EXERCICI 2")
        r = llegeix1a10()
        print("el resultado de llegeix1a10 es ", r)

    elif opcio==3:
        print("EXERCICI 3")
        c = input("introduce una letra: ")
        if trueOFalse(c):
            print("es vocal")
        else:
            print("es consonante")
    elif opcio == 4:
        print("EXERCICI 4")
        lista = ([1,2,3,4])
        print("resultado de la lista multiplicada", multlista(lista))

    elif opcio == 5:
        print("EXERCICI 5")
        lista = ingresar_datos(3)
        imprimir_histograma(lista)
    elif opcio == 6:
        print("EXERCICI 6")

    elif opcio == 7:
        print("EXERCICI 7")
        frase = 'Python es un lenguaje de programación'
        print(contador_minusculas_mayusculas(frase))

        escritor = 'Fyodor Mijalovich Dostoevskiy'
        print(contador_minusculas_mayusculas(escritor))
    else:
        flag_menu=True
        print("FIN DEL PROGRAMA")