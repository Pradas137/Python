print("BON ANY")
"""#funcion con return
def suma1 (a,b):
    resultado = a+b
    return resultado
"print(suma(4,7))"

a=int(input("escrive un numero:"))
b=int(input("escrive un segundo numero:"))
s=suma1(a,b)
print("el resultado de suma1 es:",s)

#funcion sin return
def suma2 (a,b):
    resultado = a+b
    print("el resultado de suma2 es: ",resultado)

a=int(input("escrive un numero:"))
b=int(input("escrive un segundo numero:"))
suma2(a,b)
"""
#funcion sin parametron con return
def suma3 ():
    a = int(input("escrive un numero:"))
    b = int(input("escrive un segundo numero:"))
    resultado = a+b
    return resultado
r=suma3()
print("el resultado de suma3 es ",r)

#funcion sin parametron sin return
def suma4 ():
    a = int(input("escrive un numero:"))
    b = int(input("escrive un segundo numero:"))
    resultado = a+b
    print("el resultado de suma 4 es: ",resultado)

suma4()