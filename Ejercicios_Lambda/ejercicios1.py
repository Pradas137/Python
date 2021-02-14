"""
Traduir les següents funcions a expressions lambda:

a) def doble(num):
    return num*2
b) def invertir(cadena):
    return cadena[::-1]
c) def sumar(x,y):
    return x+y
d) def impar(n):
    return n%2!=0
"""

# a)
doblar = lambda num: num*2
print(doblar(4))

# b)
revertir = lambda cadena: cadena[::-1]
print(revertir("Vacaciones"))

# c)
sumar = lambda x,y: x+y
print(sumar(10,10))

# d)
impar = lambda num: num%2 != 0
print(impar(7))
