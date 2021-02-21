def Potencia (x, y):
    if y==1: 
        return x
    elif y==0:
        return 1
    else:
        return x*Potencia(x, y-1)
print(Potencia (2,3))