def producto(num1, num2):
	if num2 == 1:
		return num1
	elif num2 == 0 or num1 == 0:
		return 0
	else: 
		return(num1+producto(num1, (num2-1)))

print(producto(0, 3))