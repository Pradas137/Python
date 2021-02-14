# 1. Escriba un programa en Python para calcular la suma de una lista de números.
def sumarLista(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + sumarLista(num_List[1:])
#print(sumarLista([2, 4, 5, 6, 7]))

# 2. Escriba un programa Python para convertir un entero en una cadena en cualquier base.

def Entero_a_cadena(n,base):
   convertirString = "0123456789ABCDEF"
   if n < base:
      return convertirString[n]
   else:
      return Entero_a_cadena(n//base,base) + convertirString[n % base]

# 3. Escriba un programa Python de suma de listas de recursividad (Datos de prueba: [1, 2, [3,4], [5,6]]).

def suma_lista_recursiva(data_list):
    total = 0
    for element in data_list:
        if type(element) == type([]):
            total = total + suma_lista_recursiva(element)
        else:
            total = total + element
    return total

# 4. Escriba un programa en Python para obtener el factorial de un entero no negativo.

def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * (factorial(n - 1))

# 5. Escriba un programa en Python para resolver la secuencia de Fibonacci usando recursividad.

def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

# 6. Escriba un programa en Python para obtener la suma de un número entero no negativo.

def sumDigits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sumDigits(int(n / 10))

# 7. Escriba un programa Python para calcular la suma de los enteros positivos de n + (n-2) + (n-4) ... (hasta nx = <0).

def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)

# 8. Escriba un programa en Python para calcular la suma armónica de n-1.

def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))

# 9. Escriba un programa en Python para calcular la suma geométrica de n-1.

def geometric_sum(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)

# 10. Escriba un programa en Python para calcular el valor de 'a' elevado a la potencia 'b'.

def potencia(a,b):
    if b==0:
        return 1
    elif a==0:
        return 0
    elif b==1:
        return a
    else:
        return a*potencia(a,b-1)

# 11. Escriba un programa en Python para encontrar el máximo común divisor (mcd) de dos enteros.
def Recursive_MCD(a, b):
    baja = min(a, b)
    alta = max(a, b)
    if baja == 0:
        return alta
    elif baja == 1:
        return 1
    else:
        return Recursive_MCD(baja, alta%baja)
