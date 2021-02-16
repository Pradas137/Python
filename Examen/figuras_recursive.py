def printstack(n, indent=0):
    if n > 0:
        printstack(n-1, indent+1)
        print(' '*indent + '* '*n)
#printstack(3)
printstack(3,5)
#printstack(3,1)
"""
def draw_triangle(n):
    if n == 0:
        return ''
    else:
        return ("*" * n + '\n') + draw_triangle(n - 1)

def main():
    num = int(input("Entra un numero: "))
    triangle = draw_triangle(num)
    print(triangle)
main()

# pascal normal

def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal(6))

#fibonacci dentro de pascal

def fib_pascal(n,fib_pos):
    if n == 1:
        line = [1]
        fib_sum = 1 if fib_pos == 0 else 0
    else:
        line = [1]
        (previous_line, fib_sum) = fib_pascal(n-1, fib_pos+1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
        if fib_pos < len(line):
            fib_sum += line[fib_pos]
    return (line, fib_sum)

def fib(n):
    return fib_pascal(n,0)[1]

for i in range(1,10):
    print(fib(i))


#cuadricula de fibonacci

memo = {0:0, 1:1}
def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def fib_index(*x):
    "" "encuentra el número natural i con fib (i) == n" ""
    if len(x) == 1:
        # iniciado por el usuario
        # buscar índice comenzando desde 0
        return fib_index(x[0], 0)
    else:
        n = fib(x[1])
        m = x[0]
        if  n > m:
            return -1
        elif n == m:
            return x[1]
        else:
            return fib_index(m, x[1]+1)


# código del ejemplo anterior con las funciones fib () y find_index ()

print(" index of a |    a |     b | sum of squares | index ")
print("=====================================================")
for i in range(15):
    square = fib(i)**2 + fib(i+1)**2
    print(f"{i:12d}|{fib(i):6d}|{fib(i+1):9d}|{square:14d}|{fib_index(square):5d}")

"""
def dibujo_rombo(valor):
  result1 = [" " * (valor - i) + "*" * (i + i - 1) for i in range(1, valor + 1)]
  return "\n".join(result1 + list(reversed(result1[:-1])))
# Llamada al método y entrada de datos
entrada_numero = int(input("Introduzca un número: "))
print(dibujo_rombo(entrada_numero))

def dibujo2(n):
    print("Pattern 1")
    for a1 in range (0,n):
        for a2 in range (a1):
            print("*", end="")
        print()

    for a1 in range (n,0,-1):
        for a2 in range (a1):
            print("*", end="")
        print()
n = 3
dibujo2(n)

def rectangulo():
    rows =int(input("How many rows? "))
    cols = int(input("How many columns? "))
    cnt = 0
    for r in range(rows):
        for c in range(cols):
            cnt += 1
        strToPrint = "*" * cnt
        cnt = 0
        print(strToPrint)
rectangulo()
