def sumar_dig(n):
	if n // 10 == 0:
		return n
	else:
		return n % 10+sumar_dig(n // 10)
print(sumar_dig(123))