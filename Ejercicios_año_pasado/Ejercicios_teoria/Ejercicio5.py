def factorial(m):
    if  (m == 0):
        return 1
    else:
        return m * factorial (m-1)

def num_combinatorios(m , n):
	return print(factorial(m) // (factorial(n)*factorial(2)))

num_combinatorios(7 , 5)