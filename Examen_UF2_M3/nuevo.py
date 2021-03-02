def añadirId():
    cool = False
    while not cool:
        try:
            id = str(input("Introdueix la teva ID: ")).upper()
            if len(id) == 3:
                contr = 0
                for caracter in range(0,2):
                    if not id[caracter].isalpha():
                        print("Format incorrecte. El format ha de ser AB1.")
                    else:
                        contr += 1
                if not id[2].isnumeric():
                    print("Format incorrecte. El format ha de ser AB1.")
                else:
                    contr += 1
                if contr == 3:
                    cool = True
                    for persona in censImperi:
                        if persona == id:
                            print("Aquesta ID ja ha estat registrada")
                            cool = False
            else:
                print("Format incorrecte. La id han de ser 2 lletres i un numero junts.")
        except ValueError:
            print("La id han de ser dues lletres i un numero junts")


def añadirPersona():
    n=1
    if n > 0:
        id=añadirId()
        censImperi[id]={}
        censImperi[id]["nom"]=añadirFrase()
        censImperi[id]["region"] = añadirFrase("region")
        censImperi[id]["edat"] = añadirEdat()
        censImperi[id]["sexe"] = añadirSexe()
        censImperi[id]["categoria"] = añadirFrase("categoria")
        censImperi[id]["poder"] = añadirPoder()
        print("Fin añadido")
    else:
        print("Error ")
