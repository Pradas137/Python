import random
censImperi={
"AR1":{"nom":"Claudia","region":"Roma","edat":23,"sexe":"I","categoria":"centurio","poder":100},
"AD3":{"nom":"Maximo","region":"Hispania","edat":30,"sexe":"H","categoria":"soldat","poder":140},
"AC2":{"nom":"Marco","region":"Hispania","edat":28,"sexe":"H","categoria":"soldat","poder":150},
"AV6":{"nom":"Julius","region":"Roma","edat":35,"sexe":"H","categoria":"cesar","poder":160},
"SS5":{"nom":"Augustus","region":"Hispania","edat":21,"sexe":"H","categoria":"soldat","poder":200},
"WQ6":{"nom":"Eugenia","region":"Hispania","edat":28,"sexe":"D","categoria":"centurio","poder":300},
"JU8":{"nom":"Anastacia","region":"Hispania","edat":17,"sexe":"I","categoria":"soldat","poder":500},
"DF5":{"nom":"Aurelia","region":"Hispania","edat":20,"sexe":"D","categoria":"poble","poder":600},
"BR1":{"nom":"Antistia","region":"Roma","edat":16,"sexe":"D","categoria":"centurio","poder":700},
"KR9":{"nom":"Apolonia","region":"Roma","edat":25,"sexe":"I","categoria":"centurio","poder":800},
"KH7":{"nom":"Acucia","region":"Roma","edat":29,"sexe":"D","categoria":"centurio","poder":900},
"XH4":{"nom":"Titus","region":"Roma","edat":39,"sexe":"I","categoria":"poble","poder":240},
"KA2":{"nom":"Aurelio","region":"Roma","edat":15,"sexe":"H","categoria":"poble","poder":300},
"MJ8":{"nom":"Tiberius","region":"Roma","edat":22,"sexe":"H","categoria":"poble","poder":600},
"MB8":{"nom":"Tiberius","region":"Roma","edat":22,"sexe":"H","categoria":"soldat","poder":800}
}
def imprimir(cabecera, datos, titulo=""):
    print("{:^80}".format(titulo.upper()))
    print("*" * 100)
    for subtitulo in cabecera:
        print("{:^20}".format(subtitulo), end="")
    print("")
    print("*" * 100)
    for dato in datos:
       # print(dato)
        for elemento in dato:
            #print(elemnto)
            print("{:^20}".format(dato[elemento]), end="")
        print()
    print("*" * 100)
cabecera = ("NOM", "REGION", "EDAT", "SEXE", "CATEGORIA")
titulo = "DADES DEMANADES"

def añadirSexo():
    cool = False
    while not cool:
        try:
            sexo = str(input("Introdueix el teu sexe: ")).upper()
            if sexo == "I" or sexo == "H" or sexo == "D":
                cool = True
                return sexo
            else:
                print("El sexe ha de ser H (home), D (dona) o I (intersexual)")
        except ValueError:
            print('El sexe ha de ser de tipus text i sense números.')

def añadirEdatMin():
    cool = False
    while not cool:
        try:
            edat = int(input("Introdueix la edat Min: "))
            if 0 <= edat <= 100:
                return edat
            else:
                print("La edat ha de ser entre 0 i 100")
                cool = False
        except ValueError:
            print("La edat ha de ser un NUMERO ENTER entre 0 i 100")

def añadirEdatMax():
    cool = False
    while not cool:
        try:
            edat = int(input("Introdueix la edat Max: "))
            if 0 <= edat <= 100:
                return edat
            else:
                print("La edat ha de ser entre 0 i 100")
                cool = False
        except ValueError:
            print("La edat ha de ser un NUMERO ENTER entre 0 i 100")

def formarExercit():
    cool = False
    while not cool:
        encontrar = []
        region1 = "Hispania"
        region2 = "Roma"
        categoria = input("Escrive la categoria: ")
        edatmin = añadirEdatMin()
        edatmax = añadirEdatMax()
        sexo = añadirSexo()
        for formar in censImperi:
            if censImperi[formar]["edat"] > edatmin and censImperi[formar]["edat"] < edatmax   and censImperi[formar]["categoria"].startswith(categoria) and censImperi[formar]["sexe"].startswith(sexo) and censImperi[formar]["region"].startswith(region1):
                encontrar.append(censImperi[formar])
                aleatorio = random.choices(encontrar, k=3)
            if censImperi[formar]["edat"] > edatmin and censImperi[formar]["edat"] < edatmax   and censImperi[formar]["categoria"].startswith(categoria) and censImperi[formar]["sexe"].startswith(sexo) and censImperi[formar]["region"].startswith(region2):
                encontrar.append(censImperi[formar])
                aleatorio2 = random.choices(encontrar, k=3)
        if len(aleatorio) == 0:
            print("Error no existen")
            return
        if len(aleatorio2) == 0:
            print("Error no existen")
            return
        else:
            print("Ejercito de Hispania")
            imprimir(("NOM", "REGION", "EDAT", "SEXE", "CATEGORIA","PODER"), aleatorio, titulo="DADES DEMANADES")
            print("")
            print("")
            print(" Ejrcito de Roma")
            imprimir(("NOM", "REGION", "EDAT", "SEXE", "CATEGORIA","PODER"), aleatorio2, titulo="DADES DEMANADES")
            return aleatorio, aleatorio2

#str(someint).startswith("123")
#random.choice(list(d.values()))
def lluita(aleatorio, aleatorio2):
    total1=0
    total2=0
    for i in aleatorio:
        total1+=i["poder"]*random.randint(0, 10)
    for i in aleatorio2:
        total2+=i["poder"]*random.randint(0, 10)
    if total1 > total2:
        return("Hispania ha machacado a Roma")
    elif total1 < total2:
        return("Roma aplasta a Hispania")
    else:
        return("Los ejercitos han quedado en empate.")
