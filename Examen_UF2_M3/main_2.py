import random
import itertools as IT
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
"MJ8":{"nom":"Tiberius","region":"Roma","edat":22,"sexe":"H","categoria":"poble"},
}
categoria = ["soldat", "cesar", "centurio", "poble"]
regio = ["Roma", "Hispania"]

# Incloure persona en el cens y comprovar nom, categoria i la regió.
def añadirFrase(verificar, frase="nom"):
    if verificar == "nom" or verificar == "categoria" or verificar == "regio":
        cool = False
        while not cool:
            try:
                if verificar == "nom" and frase != "nom":
                    if frase.isalpha():
                        return frase
                    else:
                        print("El ", verificar, "ha de ser text.")
                        frase = "nom"
                        cool = False
                elif frase != "nom":
                    # Volem evitar entrar a el else si ja tenim una frase.
                    print("")
                else:
                    if verificar == "nom":
                        frase = str(input('Entra el teu nom: '))
                    elif verificar == "categoria":
                        frase = str(input('Entra la categoría: '))
                    else:
                        frase = str(input('Entra la regio: '))
                if frase.isalpha():
                    if verificar == "categoria" and frase in categoria:
                        cool = True
                        return frase
                    elif verificar == "regio" and frase in regio:
                        cool = True
                        return frase
                    elif verificar == "categoria":
                        print("La categoria no es correcta")
                        frase = str(input('Entra la categoría: '))
                    elif verificar == "regio":
                        print("La regio no es correcta")
                        frase = str(input('Entra la regio: '))
                else:
                    print("El nom ha de ser text.")
            except ValueError:
                print('El nom ha de ser de tipus text i sense números.')
    else:
        return "null"


# Demanem un sexe al usuari, i ha de ser I, D o H.
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


# Demanem una categoria a l'usuari
def añadirCategoria():
    cool = False
    while not cool:
        try:
            cat = str(input("Introdueix la categoria: ")).lower()
            if cat in categoria:
                if cat == "cesar":
                    for persona in censImperi:
                        if censImperi[persona]["categoria"] == "cesar":
                            print("No por haver-hi més de un cesar!!!")
                            cool = False
                else:
                    cool = True
                if cool:
                    return cat
            else:
                print("La categoria no es vàlida")
        except ValueError:
            print('La categoría ha de ser de tipus text i sense números.')


# Demanem la edat a l'usuari i la comprovem.
def añadirEdat():
    cool = False
    while not cool:
        try:
            edat = int(input("Introdueix la teva edat: "))
            if 0 <= edat <= 100:
                return edat
            else:
                print("La edat ha de ser entre 0 i 100")
                cool = False
        except ValueError:
            print("La edat ha de ser un NUMERO ENTER entre 0 i 100")


# Retornem una força aleatoria entre 50 i 200
def añadirForca():
    return random.randint(50, 200)


# Comprovem la id de la persona.
def añadiridPersona():
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
                if cool:
                    return id
            else:
                print("Format incorrecte. La id han de ser 2 lletres i un numero junts.")
        except ValueError:
            print("La id han de ser dues lletres i un numero junts")


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


# Buscar persona en el censo
def buscarPersona():
    cool = False
    while not cool:
        encontrar = []
        nom = str(input("Introdueix el nom de la persona: "))
        for persona in censImperi:
            if censImperi[persona]["nom"].startswith(nom):
                encontrar.append(censImperi[persona])
        if len(encontrar) == 0:
            print("Aquesta persona no ha estat censada")
            return
        else:
            imprimir(("NOM", "REGION", "EDAT", "SEXE", "CATEGORIA"), encontrar, titulo="DADES DEMANADES")
            return encontrar

# Buscar soldados Hospania en el censo
def soldatHispania():
    cool = False
    while not cool:
        encontrar = []
        categoria = "soldat"
        hispania = "Hispania"
        for region in censImperi:
            if censImperi[region]["region"].startswith(hispania) and censImperi[region]["categoria"].startswith(categoria):
                encontrar.append(censImperi[region])
        if len(encontrar) == 0:
            print("La region no existe")
            return
        else:
            imprimir(("NOM", "REGION", "EDAT", "SEXE", "CATEGORIA"), encontrar, titulo="DADES DEMANADES")
            return encontrar

def buscarCategoria():
    cool = False
    while not cool:
        encontrar = []
        nomCategory = str(input("Introdueix el nom de la Categoria: "))
        for categoria in censImperi:
            if censImperi[categoria]["categoria"].startswith(nomCategory):
                encontrar.append(censImperi[categoria])
        if len(encontrar) == 0:
            print("Aquesta persona no ha estat censada")
            return
        else:
            imprimir(("NOM", "REGION", "EDAT", "SEXE", "CATEGORIA"), encontrar, titulo="DADES DEMANADES")
            print(encontrar)
            return encontrar

def modificarCenso():
    cool = False
    while not cool:
        encontrar = []
        code = input("Escrive el codigo a modificar: ")
        for codex in censImperi:
            if censImperi[codex]["AR1"].startswith(code):
                nom = input("Escrive nuevo nombre: ")
                nombre = censImperi.setdefault("nom",nom)
                encontrar.append(censImperi[codex])
        if len(encontrar) == 0:
            print("el codigo no existe")
            return
        else:
            imprimir(("NOM", "REGION", "EDAT", "SEXE", "CATEGORIA"), encontrar, titulo="DADES DEMANADES")
            print(encontrar)
            return encontrar

def removeCens(borrar,censImperi):
    encontrar=[]
    delete = []
    key_to_be_deleted = (borrar)
    delete.append(censImperi.pop(key_to_be_deleted))
    imprimir(("NOM", "REGION", "EDAT", "SEXE", "CATEGORIA"), delete, titulo="DADES DEMANADES")
    print(censImperi)
def menu_generator(options, header,linea):
    flag_menu = False
    while not flag_menu:
        print(header)
        print(linea*53)
        for i in range(len(options)):
            print(i+1, ")", options[i])
        try:
            user_option = int(input("Elige una opcion: "))
            if 0 < user_option <= len(options):
                flag_menu = True
                return user_option
            else:
                print("Opcion Invalida.")
                flag_menu = False
        except ValueError:
            print("Eso no es un número. Intentar otra vez.")

datos=("Incloure persona en el cens","Buscar persona en el cens","Mostrar soldats Hispania","Visualitzar categoria del cens","Modificar Censo","Borrar en Censo")
titol="CENS ROMA"
capsalera="_"
flag_principal = False
while not flag_principal:
    opcion_menu = menu_generator(datos,titol,capsalera)
    if opcion_menu == 1:
        print("opcion1")
        print(añadirFrase("categoria", "asd"))
        print(añadirSexo())
        añadirCategoria()
        añadirEdat()
        print(añadirForca())
        print(añadiridPersona())
    elif opcion_menu == 2:
        print("opcion2")
        buscarPersona()
    elif opcion_menu == 3:
        print("opcion3")
        soldatHispania()
    elif opcion_menu == 4:
        print("opcion4")
        buscarCategoria()
    elif opcion_menu == 5:
        print("opcion5")
        modificarCenso()
    elif opcion_menu == 6:
        print("opcion6")
        print("Las opciones de ID son.")
        print("AR1,AD3,AC2,AV6,SS5,WQ6,JU8,DF5,BR1,KR9,KH7,XH4,KA2,MJ8")
        borrar = input("ID a borrar: ")
        removeCens(borrar,censImperi)
    elif opcion_menu == 0:
        salir = True
        break

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce el número a convertir a binario: '))
print(binarizar(numero))
