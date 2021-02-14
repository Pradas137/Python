def tres_lineas():
	x = 1
	while x<=3:
		print("")
		x+=1
def nueve_lineas():
	x = 1
	while x<=3:
		tres_lineas()
		x+=1
def neteja_pantalla():
	x = 1
	while x<=25:
		print("")
		x+=1
def concatena_n_vegades(c, n):
	i=0
	while i<n:
		print(c)
		i=i+1
#si cambiamos la funciones solo nos cambia el orden
neteja_pantalla()
nueve_lineas()
c = input("Introduce un caracter : ")
n = int(input("introduce un numero: "))
concatena_n_vegades(c, n)