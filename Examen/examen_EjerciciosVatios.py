# EJERCICIO 1
import random
def suma(lista):
    suma=0
    for y in (lista):
         suma=suma+y
    return suma

def multi(lista):
    multi=1
    for x in (lista):
        multi=multi*x
    return multi


lista=[]
long=random.randrange(2,10)
num=0
for i in range(long):
    num= random.randrange(100)
    lista.append(num)
print(lista)
print("La suma es: ", suma(lista))
print("La multiplicacio es: ", multi(lista))
# EJERCICIO 2

def creaciollista(i):
    llista=[]
    print("Quantes paraules te la llista: ", i+1, "?")
    long=int(input())
    for x in range(long):
        paraula=input("Introdueix una paraula: ")
        llista.append(paraula)
    return llista

quantitat=int(input(("Quantes llistes vols crear: ")))
final=[]
for i in range(quantitat):
    resultat=("La llista", i+1,"es:", creaciollista(i))
    final.append(resultat)
for x in final:
    print (x)

# EJERCICIO 3

def sumadesc(*num):
    suma=0

    for x in num:
        suma=suma+x
    return suma

print("La suma es: ", sumadesc(1,2))
print("La suma es: ", sumadesc(1,2,3,4,5,6,7,8))

# EJERCICIO 4

def multiplicar(num,pos=10):
    taula=[]
    for i in range(pos):
        resultat=num*i
        taula.append(resultat)
    return taula
print("La taula de multiplicar de ",4," es: ", multiplicar(4,5))
print("La taula de multiplicar de ",4," es: ", multiplicar(4))

# EJERCICIO 5

def binario(numero,base,resultat):
    if numero<base:
        return 0
    else:
        residu=numero-base
        residu=str(residu)
        resultat=resultat+residu
        return 1 + binario(numero - base, base, resultat)
print("resultat: ",binario(12,3,""))

# EJERCICIO 6

def dibuix(lista1,lista2,i,j,contador):
    if contador<2:
        if len(lista1)>i:
            print(lista1[i],end=" ")
            return dibuix(lista1,lista2,i+1,j,contador)
        elif len(lista1)==i:
            print("\n")
            return dibuix(lista1, lista2, i+1, j,contador)
        elif len(lista2)>j:
            print(lista2[j],end=" ")
            return dibuix(lista1,lista2,i,j+1,contador)
        elif len(lista2)==i:
            print("\n")
            return dibuix(lista1, lista2, i, j+1,contador)
        else:
            print("\n")
            lista2=[]
            i=0
            j=0
            return dibuix(lista1, lista2, i, j,contador+1)
    return
contador=0
i=0
j=0
dibuix([" ","A"," "],["B","A","B"],i,j,contador)

# EJERCICIO 7
