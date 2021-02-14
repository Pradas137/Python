def inserir_Millonari():
    Millo = {}
    continuar = "s"
    while continuar == "s":
        cod = "millonario"
        nom = input("Ingrese el nombre: ")
        edat = int(input("Ingrese la edat: "))
        quantitat = int(input("Ingrese la cantidad de acciones: "))
        Millo[cod] = (nom, edat, quantitat)
        continuar = input("Desea cargar otro producto[s/n]?")
    print(Millo)

def inserir_Empresas():
    accions = {}
    continuar = "s"
    while continuar == "s":
        cod = "Empresa"
        nom = input("Ingrese el nombre: ")
        precio = int(input("Ingrese el precio de la accion: "))
        accions[cod] = (nom, precio)
        continuar = input("Desea cargar otro producto[s/n]?")
    return accions

def Mostrar_Millonaris(Millo):
    print("\n ========================= ")
    print("      ElS MILLONETIS SON:   ")
    print(" =========================\n")
    for cod in Millo:
        print(cod,Millo[cod][0],Millo[cod][1],Millo[cod][2])