import random
"""
print("-----------------------------------------------")
print("-----------------Suma Lista--------------------")
print("-----------------------------------------------")
def sumaLista(lista,pos):
          if pos == len(lista)-1:
                    return lista[pos]
          else:
                    return lista[pos] + sumaLista(lista,pos+1)

valores =[1,2,3,4]
print(sumaLista(valores,0))

print("-----------------------------------------------")
print("---------------Producto Lista------------------")
print("-----------------------------------------------")
def productolista(lista):
          if len(lista) == 1:
                    return lista[0]
          return lista[0] * productolista(lista[1:])
valores =[1,2,3]
print(productolista(valores))

print("-----------------------------------------------")
print("---------------Producto Lista------------------")
print("-----------------------------------------------")
"""
"""def mostrarNumeros(num):
    if 1 == num:
              print(num)
              return num
    print(1+mostrarNumeros(num-1))
    return num

numero = int(input("escrive un numero:"))
mostrarNumeros(numero)
"""
"""
def mostrarNumeros(num):
    if 1 == num:
              print(num)
    else:
              mostrarNumeros(num-1)
              print(num)

numero = int(input("escrive un numero:"))
mostrarNumeros(numero)
"""

"""
def suma(num):
    if num==0:
        return num
    if num%2!=0:
        num=num-1
    return num+suma(num-2)

print(suma(15))

def suma(num):
    if num==2:
        return 2
    elif num%2==0:
        return num+suma(num-2)
    else:
        return (num-1)+suma(num-3)
print(suma(11))

"""
"""1.Dissenyeu una funció recursiva tal que, donats dos llistes de números sencers, retorni un
booleà indicant si són iguals, és a dir, si tenen els mateixos valors a les mateixes posicions.""""""
def compararListas (lst1, lst2):
    if lst1 and lst2:
        if len(lst1) != len(lst2):
            return False
        if lst1[0] != lst2[0]:
            return False
        return compararListas(lst1[1:],lst2[1:])
    else:
        return True
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
print(compararListas(lista1,lista2))

"""
"""2.Donat una llista de números enters ordenada decreixentment, dissenyeu un programa
recursiu que comprovi si el valor d’algun dels elements de la llista coincideix amb el seu
índex.""""""

def compararListasIndex(lst):
    if len(lst)==1:
        if lst[-1]==lst.index(lst[-1]):
            return True
        else:
            return False
    if compararListasIndex(lst[:-1])==False:
        if lst[-1]==lst.index(lst[-1]):
            return True
        else:
            return False
    else:
        return True
lista1 = [1,2,3,4,5]
print(compararListasIndex(lista1))

def fubonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fubonacci(num-1) + fubonacci(num-2)
numero=int(input("Escrive un numero:"))
for i in range(numero):
    print(fubonacci(i),end=" ")
print(fubonacci(numero))

def rata():
    camino = random.randint(1,3)
    if camino==1:
        return 3+rata()
    if camino==2:
        return 5+rata()
    else:
        return 7
print(rata())
"""
"""
def recursividad(n):
    if n == 1:
        return 4
    return 4 * (-1) ** (n + 1) * (1 / (2 * n - 1)) + recursividad(n - 1)

n= int(input("escrive un numero: "))
print(recursividad(n))

def invertir(number):
   if number == 1:
      return number
   else:
      return int(str(number%10) + str(invertir(number//10)))
n=int(input("escrive un numero:"))
print(invertir(n))
"""
"""
def multiplicar(n):
    return n * 2

def dividir(n):
    return n // 2

def mult(m, n, a = 0):
    if n % 2 != 0:
        a = a + m
        m = multiplicar(m)
        n = dividir(n)
    if n % 2 == 0:
        m = multiplicar(m)
        n = dividir(n)
    if n != 0:
        return mult(m, n, a)
    return a

print(mult(27, 82))

def rusa (A,B):
    print(A,B)
    if A == 1:
        return B
    if A%2!=0:
        return B+rusa(A//2,B*2)
    return rusa(A//2,B*2)
print(rusa(27,82))
"""
"""def piramide(num, indent=0):
    if not num:
        return
    print(' ' * indent, end='')
    print(''.join(map(str, range(1, num))) +
          ''.join(map(str, range(num, 0, -1))))
    piramide(num - 1, indent + 1)
print(piramide(7))"""

"""
def curiositat(n):
    uno ="1"*n
    if n==1:
        print(int(uno)**2)
        return
    curiositat(n-1)
    print(int(uno)**2)
curiositat(7)
"""
"""
import random
random = random.randint(1,1000)
print(random)

def adivina():
    adivina = input("ingrese un número del 1 al 1000: ")
    return adivina

def adivina_el_número():
    try:
        numero = int(adivina())
        if random == numero:
            print("!Adivinaste el número¡")
            return
        elif random > numero:
            print("Un poco más alto.")
            adivina_el_número()
            return
        elif random < numero:
            print("un poco más bajo")
            adivina_el_número()
            return
    except:
        print("Por favor ingrese un número válido del una al diez")
        adivina_el_número()

adivina_el_número()
"""
"""
from random import randint
def guess(num, min=0, max=1000, attempt=1):
    user_guess = int(input("Which number do you think it is? "))
    if num == user_guess:
        print("CORRECT! You guessed the number at the ", attempt, "attempt")
        return
    else:
        if min < user_guess < num:
            print("The number is between", user_guess, "and", max)
            return guess(num, user_guess, max, attempt+1)
        elif num < user_guess < max:
            print("The number is between", min, "and", user_guess)
            return guess(num, min, user_guess, attempt+1)
        else:
            print("The number is between", min, "and", max)
            return guess(num, min, max, attempt+1)


print("A random number between 0 and 1000 will be chosen.")
guess(randint(0, 1001))

"""

"""
def cercaBinaria(lista, numBuscar, inf=0, sup=len(lista)):


    return

lista = [1,2,3,4,5]
if cercaBinaria(5,lista,0,len(lista)-1)==True:
    print("El numero esta en la lista")
else:
    print("El numero no esta en la lista")
"""

"""
def cercaBinario(lista, numBuscar):
    if len(lista) == 0:
        return False
    else:
        medio = len(lista)//2
        if lista[medio]==numBuscar:
            return True
        else:
            if numBuscar<lista[medio]:
                return cercaBinario(lista[:medio],numBuscar)
            else:
                return cercaBinario(lista[medio+1:],numBuscar)
lista = [1,2,3,4,5]
if cercaBinario(lista,4)==True:
    print("numero encontrado")
else:
    print("Numero no encontrado")


def cercaBinaria(numBuscar,lista,inf,sup):
    puntoMedio=(inf+sup)//2
    #CASO BASE
    if inf<=sup:
        if lista[puntoMedio]==numBuscar:
            return True
        elif lista[puntoMedio]<numBuscar:
            return cercaBinaria(numBuscar,lista,puntoMedio+1,sup)
        else:
            return cercaBinaria(numBuscar,lista,inf,puntoMedio-1)
    else:
        return False

lista=[100,200,300,400,500]
if cercaBinaria(301,lista,0,len(lista)-1)==True:
    print("El numero está en la lista")
else:
    print("El numero no está en la lista")
"""
"""
def cercaBurvuja(lista,n):
    for i in range(len(lista)-2):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
    if n>1:        
        cercaBurvuja(lista,n-1)

lista = [6,2,9,11,9,3,7,12]
n=len(lista)
cercaBurvuja(lista,n)
print(lista)

def burbuja2(l,n):
    if n ==1:
        return l
    for i in range(0,n-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
    return burbuja2(l,n-1)
l=[3,1,2]
print(burbuja2(l,len(l)))

"""
"""
def metodo_Burbuja_recurivo(array, pasos, comparaciones):
  if len(array)-1 < pasos:
      #print(len(array)-1,"-", pasos)
      return array
  else:
    if len(array[pasos])-2 < comparaciones :
        #print(len(array[pasos])-2,"-", comparaciones)
        return metodo_Burbuja_recurivo(array, pasos + 1, 0)
    elif array[pasos][comparaciones] > array[pasos][comparaciones - 1]:
        #print(array[pasos][comparaciones],"-",array[pasos][comparaciones + 1])
        array[pasos][comparaciones], array[pasos][comparaciones + 1] = array[pasos][comparaciones + 1], array[pasos][comparaciones]
        print(array[pasos][comparaciones],"-", array[pasos][comparaciones + 1])
    return metodo_Burbuja_recurivo(array, pasos, comparaciones + 1)

lst = [[3,1,2],[8,4,5],[9,-1,2]]
print(metodo_Burbuja_recurivo(lst,0,0))
"""