def suma(l):
	if (len(l) == 0):
		return 0
	return l[0] + suma(l[1:])

lista = [1,2,2,2]
print(suma(lista))