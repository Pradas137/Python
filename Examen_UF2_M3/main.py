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

#Ejercicio 2 añadir datos.

#Ejercicio 3 Buscar.
def buscarPersona(buscar):
    for clave, valor in censImperi.items():
        elementos = ", ".join(valor.keys())
        print(clave, ":", elementos)

#Ejercicio 4 Mostrar SoldadoHispania
def MostrarSoldadoHispania():
    found = None
    for key, val in censImperi.items():
        if search_key in key:
            if found is None:
                found = val
            else:
                print("Found more than one match, please be more specific")
                break
        else:
            if found is None:
                print("Nothing found, please search again")
            else:
                print("Match found! {}".format(found))

#Ejercicio 5 VISUALITZAR CATEGORIA DEL CENS
def mostrarCategoria(censImperi):
    lista=[]
    nombre=input("escribe un nombre:")
    for mat in censImperi.values():
        for j in nombre:
            if mat["categoria"]==j["categoria"]:
                lista.append(mat)
    lista=sorted(lista,key=lambda elemento: elemento["categoria"],reverse=False)
    return lista


def menu_generator(options, header,linea):
    flag_menu = False
    while not flag_menu:
        print(header)
        print(linea*53)
        for i in range(len(options)):
            print(i+1, ")", options[i])
        try:
            user_option = int(input("Choose an option: "))
            if 0 < user_option <= len(options):
                flag_menu = True
                return user_option
            else:
                print("Invalid option.")
                flag_menu = False
        except ValueError:
            print("That's no a number. Try again.")

datos=("Incloure persona en el cens","Buscar persona en el cens","Mostrar soldats Hispania","Visualitzar categoria del cens")
titol="CENS ROMA"
capsalera="_"
flag_principal = False
while not flag_principal:
    opcion_menu = menu_generator(datos,titol,capsalera)
    if opcion_menu == 1:
        print("opcion1")
    elif opcion_menu == 2:
        print("opcion2")
        buscar = input("Introdueixi Nom: ")
        buscarPersona(buscar)
    elif opcion_menu == 3:
        print("opcion3")
    elif opcion_menu == 4:
        salir = True
        break
