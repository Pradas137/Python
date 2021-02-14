accions={'MicroSopa':2.67,'AireTel': 1.2,'AmenizaDos': 0.98,'IbemePorUvas': 5.3,'MacChiton':0.25}
def insert_Millonari():
    diccionario={}
    diccionario2={}
    continua="s"
    nuevo="z"
    while continua=="s":
        nombre=input("Nombre :")
        edat=input("Edat:")
        diccionario[nombre]=edat
        continua=input("Quiere cargar otra palabra:[s/n]")
    while nuevo=="z":
        empresa=input("Empresa :")
        acciones=input("Acciones:")
        diccionario2[empresa]=acciones
        nuevo=input("Quiere cargar otra palabra:[z/n]")
    dest = dict(diccionario)
    dest.update(diccionario2)
    return dest

def imprimir(dest):
    print("Listado completo del diccionario")
    for nombre in dest:
        print(nombre,dest[nombre])

def insert_Empresas():

    return True
dest=insert_Millonari()
imprimir(dest)

