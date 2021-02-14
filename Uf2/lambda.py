"""Fes una funció que rebi entre 2 i n valors enters i retorni el producte de tots el parametres.
Exemple de crides a la funció:
producte(1,2,3,4,5,6,7,8,9,10)
producte(1,2,3,4)
producte(1,2)"""

def producte(a,*b):
    producto=a
    #print(type(b))
    #b=list(b)
    for i in b:
        producto*=i
    return producto

print(producte(1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10))
print(producte(1,2,3,4,5,6,7,8,9,10))
print(producte(1,2,3,4))
print(producte(1,2))