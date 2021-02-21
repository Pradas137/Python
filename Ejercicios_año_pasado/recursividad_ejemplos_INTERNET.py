#
# Ejemplos de programas recursivos
# en Python 3.x
#
# Receta basica (usando idle3):
# 1) En idle3 open this file.
# 2) Run Module (F5) of this file.
# 3) Eventualmente en la ventana interactiva ejecutar comandos.
#
def suma (n):
    """
    Suma de Gauss hasta el entero n, version recursiva
    """
    if (n == 1):
        return 1
    else:
        return suma (n-1) + n
        
def maximo (A):
    """
    Maximo de la lista A, version recursiva
    """
    if len (A) == 1:
        return A [0]
    else:
        return my_max (maximo(A[0:len(A)-1]),A[len(A)-1])
        
def my_max (a,b):
    """
    Auxiliar de la funcion anterior.
    """
    if (a >= b):
        return a
    else:
        return b

def mcd (a,b):
    """
    Maximo Comun Divisor de los enteros a y b, version recursiva
    """
    if (a > b):
        t = b
        b = a
        a = t
    if   (a == 0):
        return b
    elif (a == b-a):
        return a
    else:
        return mcd (a,b-a)

def a_n21 (n):
    """
    Rosen, 5ta edicion, E21, pag. 264.
    Calculo del termino enesimo de la sucesion
    a_0 = 1, a_1 = 1, y a_n = a_{n-1} a_{n-2}, 
    para n = 2, 3, 4, ..., version recursiva.
    """
    if   (n == 0):
        return 1
    elif (n == 1):
        return 2
    else:   
        return a_n21 (n-1) * a_n21 (n-2)
    
def a_n24 (n):
    """
    Rosen, 5ta edicion, E24, pag. 264.
    Calculo del termino enesimo de la sucesion
    a_0 = 1, a_1 = 2, a_2 = 3, y 
    a_n = a_{n-1} + a_{n-2} + a_{n-3}, 
    para n = 3, 4, 5, ..., version recursiva.
    """
    if   (n == 0):
        return 1
    elif (n == 1):
        return 2
    elif (n == 2):
        return 3
    else:   
        return a_n24 (n-1) + a_n24 (n-2) + a_n24 (n-3)
    
def factorial (n):
    """
    Calculo del factorial del entero no-negativo n, version recursiva.
    """
    if  (n == 0):
        return 1
    else:
        return n * factorial (n-1)

# begin test
def test01 ():
    n = 100
    print ('La suma 1 + 2 + ... + n, con n = ', n)
    print ('es igual a ', suma (n), '\n')
    return

def test02 ():
    A = [ 1, 0, 3, 8, 5, 6, 7, 4, 9, 2 ]
    print ('El maximo de la lista A = ', A)
    print ('es igual a ',  maximo (A), '\n')
    return

def test03 ():
    a = 48
    b = 12
    print ('El mcd de ', a, ' y de ', b)
    print ('es igual a ',  mcd (a,b), '\n' )
    return

def test04 ():    
    n = 789
    print ('El factorial de ', n)
    print ('es igual a ',  factorial (n), '\n' )
    return

def test05 ():
    n = 12
    print ('Rosen, 5ta edicion, E21, pag. 264.        ')
    print ('Calculo del termino enesimo de la sucesion')
    print ('a_0 = 1, a_1 = 1, y a_n = a_{n-1} a_{n-2},')
    print ('para n = 2, 3, 4, ..., version recursiva. ')
    print ('Cuando n = ', n, ' es a_n = ', a_n21 (n), '\n')
    return

def test06 ():    
    n = 17
    print ('Rosen, 5ta edicion, E24, pag. 264.        ')
    print ('Calculo del termino enesimo de la sucesion')
    print ('a_0 = 1, a_1 = 2, a_2 = 3, y              ')
    print ('a_n = a_{n-1} + a_{n-2} + a_{n-3}         ')
    print ('para n = 3, 4, 5, ..., version recursiva. ')
    print ('Cuando n = ', n, ' es a_n = ', a_n24 (n), '\n')
    return

if __name__== "__main__":
    test01 ()
    test02 ()
    test03 ()
    test04 ()
    test05 ()
    test06 ()
#end

#El siguiente ejemplo es un algoritmo recursivo para imprimir una lista hacia atrás:
def imprimeAlReves(lista):
    if lista == None: 
        return cabeza = lista
        cola = lista.siguiente
        imprimeAlReves(cola)
        print cabeza

