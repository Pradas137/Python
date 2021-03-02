from Examen_UF2_M3_Parte2.funcionsCens import *
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

datos=("Incloure persona en el cens","Buscar persona en el cens","Mostrar soldats Hispania","Visualitzar categoria del cens","Formar Exercit","Lluitar")
titol="CENS ROMA"
capsalera="_"
flag_principal = False
while not flag_principal:
    opcion_menu = menu_generator(datos,titol,capsalera)
    if opcion_menu == 1:
        print("opcion1")
    elif opcion_menu == 2:
        print("opcion2")
    elif opcion_menu == 3:
        print("opcion3")
    elif opcion_menu == 4:
        print("opcion4")
    elif opcion_menu == 5:
        print("opcion5")
        ejercito1,ejercito2= formarExercit()
    elif opcion_menu == 6:
        print("opcion6")
        print(lluita(ejercito1,ejercito2))
    elif opcion_menu == 0:
        salir = True
        break
