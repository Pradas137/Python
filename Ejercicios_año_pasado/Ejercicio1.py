def mult(l):
	print(l)
	if len(l) == 0:
		return 1
	return l[0]*mult(l[1:])		
		 
print("soy mul", mult([2,1,3,4]))

