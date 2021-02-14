def aprovats(lista_al, lista_not):
    for j in range(len(lista_not)):
        if lista_not[j] >= 5:
            print(lista_al[j])


def num_aprovats(lista_not):
    suma = 0
    for j in lista_not:
        if j >= 5:
            suma += 1
    return suma


def max_nota(lista_al, lista_not):
    maximo = lista_not[0]
    for i in lista_not:
        if i > maximo:
            maximo = i
            #print("La nota Maxima es: ", maximo)
    for i in range(len(lista_not)):
        if lista_not[i] == maximo:
            print(lista_al[i],lista_not[i])
    return lista


def cualificacio_media(lista_al, lista_not):
    media = 0
    for j in lista_not:
        media += j
    media/=len(lista_not)
    print("La media es:", media)
    for i in range(len(lista_not)):
        if lista_not[i] >= media:
            print(lista_al[i], lista_not[i])
    return lista


def busqueda_alumne(lista_al,lista_not,nom):
   """for i in range(len(lista_al)):
        if lista_al[i] == nom:
            return lista_not[i]
    return None"""
   if nom.capitalize() in lista_al:
       return lista_not[lista_al.index(nom.capitalize())]
   else:
       return None
def ordenarNotasMayorAMenor(lista_al,lista_not):
    for k in range(len(lista_not)-1):
        for x in range(len(lista_not)-1-k):
            if lista_not[x] < lista_not[x + 1]:
                lista_not[x],lista_not[x+1]=lista_not[x+1],lista_not[x]
                lista_al[x], lista_al[x + 1] = lista_al[x + 1], lista_al[x]
                
lista_al = ['Pere','Pau','Anna','Andrea','Pol','Nil','Montserrat','Gerard']
lista_not =[4.3, 5.6, 5.9, 9.7, 2.6, 6.8, 8.8, 2.4]
lista = []

print("\n=============================================")
print("============ Menu ===========================")
print("=============================================\n")
print("======= 1. Listado de aprovados  ============")
print("======= 2. Cantidad de aprovados ============")
print("======= 3. Nota Maxima  =====================")
print("======= 4. calif superior a la media ========")
print("======= 5. Busqueda de alumno por nombre ====")
print("======= 6. Ordenar de mayor a menor ====")
print("======= 7. salida ===========================\n")
print("=============================================\n")

while True:
    opcio = input("\nIntroduce una opcion:  ")
    if opcio == '1':
        aprovats(lista_al, lista_not)
    if opcio == '2':
        suma = num_aprovats(lista_not)
        print("la  cantidad de aprovados es: ", suma)
    if opcio == '3':
        max_nota(lista_al, lista_not)
    if opcio == '4':
        cualificacio_media(lista_al, lista_not)
    if opcio == '5':
        nom = input("Introduce el nombre del estudiante: ")
        nota = busqueda_alumne(lista_al,lista_not,nom)
        #if nota!=None: print("AL nota es: ,nota) else : print("la nota es none")
        print("la nota del alumno buscado es: ", nota)
    if opcio == '6':
        ordenarNotasMayorAMenor(lista_al, lista_not)
        print(lista_al)
        print(lista_not)
    if opcio == '7':
        break