def numDigitos(n):
    if n // 10 == 0:
        return 1
    else:
        return 1 + numDigitos(n // 10)
 
def invertir(n):
    if numDigitos(n) == 1:
        return n
    return (n % 10) * 10 ** (numDigitos(n) - 1) + invertir(n // 10)

print(invertir(3456))