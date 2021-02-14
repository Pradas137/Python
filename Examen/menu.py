from Examen.Operaciones_main import *
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
    print ("1. Sumar Lista")
    print ("2. Convertir entero a cadena")
    print ("3. Sumar lista de listas")
    print ("4. Calcular factorial entero no negativo")
    print ("5. Calcular Fibonacci")
    print ("6. Sumar entero no negativo")
    print ("7. Suma serie de numeros")
    print ("8. Calcular suma armónica")
    print ("9. Calcular suma geométrica")
    print ("10. Calcular potencia")
    print ("11. Calcular máximo común divisor")
    print ("0. Salir")
    print ("Elige una opcion")
    opcion = pedirNumeroEntero()
    if opcion == 1:
        print(sumarLista([2, 4, 5, 6, 7]))
    elif opcion == 2:
        print(Entero_a_cadena(2835,16))
    elif opcion == 3:
        print(suma_lista_recursiva([1, 2, [3,4],[5,6]]))
    elif opcion == 4:
        print(factorial(5))
    elif opcion == 5:
        print(fibonacci(7))
    elif opcion == 6:
        print(sumDigits(345))
    elif opcion == 7:
        print(sum_series(6))
    elif opcion == 8:
        print(harmonic_sum(7))
    elif opcion == 9:
        print(geometric_sum(7))
    elif opcion == 10:
        print(potencia(3,4))
    elif opcion == 11:
        print(Recursive_MCD(12,14))
    elif opcion == 0:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 11")
print ("Fin")
