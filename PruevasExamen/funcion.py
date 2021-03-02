import random
censImperi={
"AR1":{"nom":"Claudia","region":"Roma","edat":23,"sexe":"I","categoria":"centurio"},
"AD3":{"nom":"Maximo","region":"Hispania","edat":30,"sexe":"H","categoria":"soldat"},
"AC2":{"nom":"Marco","region":"Hispania","edat":28,"sexe":"H","categoria":"soldat"},
"AV6":{"nom":"Julius","region":"Roma","edat":35,"sexe":"H","categoria":"cesar"},
"SS5":{"nom":"Augustus","region":"Hispania","edat":21,"sexe":"H","categoria":"soldat"},
"WQ6":{"nom":"Eugenia","region":"Hispania","edat":28,"sexe":"D","categoria":"centurio"},
"JU8":{"nom":"Anastacia","region":"Hispania","edat":17,"sexe":"I","categoria":"soldat"},
"DF5":{"nom":"Aurelia","region":"Hispania","edat":20,"sexe":"D","categoria":"poble"},
"BR1":{"nom":"Antistia","region":"Roma","edat":16,"sexe":"D","categoria":"centurio"},
"KR9":{"nom":"Apolonia","region":"Roma","edat":25,"sexe":"I","categoria":"centurio"},
"KH7":{"nom":"Acucia","region":"Roma","edat":29,"sexe":"D","categoria":"centurio"},
"XH4":{"nom":"Titus","region":"Roma","edat":39,"sexe":"I","categoria":"poble"},
"KA2":{"nom":"Aurelio","region":"Roma","edat":15,"sexe":"H","categoria":"poble"},
"MJ8":{"nom":"Tiberius","region":"Roma","edat":22,"sexe":"H","categoria":"poble"}
}

def imprimirlista(lista,cantidad):
    lista1 = random.choices(lista, k=3)
    lista2 = random.choices(lista, k=cantidad)
    print(lista1)
    print(lista2)
cantidad = int(input("Escrive la cantidad de productos que compraras: "))
print(imprimirlista(censImperi,cantidad))
