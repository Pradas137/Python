# Esta función crea un menú y tiene 2 argumentos:
# opciones: Todas las opciones se envían como tuplas ('Item1', 'Item2', 'Item3', etc.)
# Encabezado: por defecto, el encabezado es solo una nueva línea.
# Para declarar un encabezado, debe hacerse como menu_generator ([elementos del menú], encabezado = 'MENÚ')
# Ejemplo de llamada a función sin encabezado: menu_generator ('item1', 'item2', 'item3')
# Ejemplo de llamada de función con encabezado: menu_generator ('item1', 'item2', 'item3', header = 'MAIN MENU')
def menu_generator(*options, header="\n"):
    flag_menu = False
    while not flag_menu:
        print(header)
        for i in range(len(options)):
            print(i+1, ")", options[i])
        try:
            user_option = int(input("Elegir opcion: "))
            if 0 < user_option <= len(options):
                flag_menu = True
                return user_option
            else:
                print("Opcion Invalida.")
                flag_menu = False
        except ValueError:
            print("Eso no es un número. Intentar otra vez.")
print(menu_generator("List by ID", "List by name", "List by Stock", "Back", header='MAIN MENU'))
"""
# Esta función comprueba si una identificación personal es correcta o no.
def nif_checker():
    valid = False
    while not valid:
        try:
            # Primero, el programa le pide al usuario su ID (número + letra)
            nif = input("Por favor, introduzca aquí su DNI: ")
            if len(nif) == 9:
                # Si la longitud es correcta, se verifica el formato (8 números + letra)
                condition = 0
                # Primera comprobación. Las primeras 8 posiciones son números.
                for i in range(0, 9):
                    if nif[i].isnumeric():
                        condition += 1
                # En segundo lugar, se comprueba la última posición si es una letra.
                if nif[8].isalpha():
                    condition += 1
                # Si todas las posiciones son correctas, entonces la ID se muestra con letras mayúsculas.
                if condition == 9:
                    nif_nums = nif[:-1]
                    nif_letter = nif[-1]
                    print(nif_nums, str(nif_letter).upper())
                else:
                    print('El formato es incorrecto. Vuelva a intentarlo con el formato 12345678A')
                #print(nif)
            else:
                print('Esa identificación no tiene la longitud correcta. Debe tener 8 números.')
        except:
            print('Error inesperado.')
nif_checker()
"""
"""
Vamos a crear una función que llamaremos nuevo_telefono().
Esta función no recibirá ningún parámetro, pedirá un teléfono por consola y en caso de ser un
teléfono correcto ( 9 números), nos devolverá un string con el teléfono introducido por consola
Esta función lanzará excepciones en el caso que:
 El teléfono no tenga un formato adecuado ( 9 números).
Y nos mostrará un mensaje descriptivo del error correspondiente, volviendo a pedir un teléfono al
usuario.
"""
def new_phone():
    correct = False
    while not correct:
        try:
            # El programa intenta guardar el número como un entero.
            # Si hay alguna letra, la excepción mostrará un mensaje de error.
            phone = int(input("Entra numero de telefono: "))
            # Si la longitud es 9, entonces el número de teléfono es correcto y se muestra en la pantalla.
            if len(str(phone)) == 9:
                print('The phone is:', phone)
                correct = True
            # En caso de que la longitud sea diferente a 9, entonces el teléfono no es correcto y se muestra un mensaje de error.
            else:
                print('Ese teléfono no tiene la longitud correcta. 9 números es la longitud correcta.')
        except:
            print('¡Un número de teléfono NO PUEDE TENER NINGUNA LETRA!')
new_phone()
"""
Crearemos una función con el nombre nuevo_nif(). Que no recibirá ningún parámetro.
Al llamar a esta función, nos pedirá el numero del dni por consola y en caso de que el número sea
coorecto, calculará la letra del dni y nos devolverá este NIF con la letra en mayúscula.
Para calcular la letra:
• Crear la variable: palabra='TRWAGMYFPDXBNJZSQVHLCKE'
• La letra del dni corresponde a la posición de la lista resultado de la operación
 numerodni%23
Esta función lanzará excepciones en el caso que:
 El NIF no tenga un formato adecuado ( 8 números y una letra).
 El NIF ya exista en el diccionario dict_clientes.
Y nos mostrará un mensaje descriptivo del error correspondiente, volviendo a pedir un NIF al
usuario.
"""
def new_nif():
    customers = ['15768246K', '75315982K', '28461973W', '73914682L', '74185269B', '16739842M']
    correct = False
    while not correct:
        try:
            nif = int(input('Por favor ingrese su nif sin letras:'))
            if len(str(nif)) == 8:
                correct = True
            else:
                print('¡NIF DEBE TENER 8 CARACTERES!')
        except:
            print('¡SIN LETRAS!')

    word = 'TRWAGMYFPDXBNJZSQVHLCKE'
    position = nif % 23
    complete = (str(nif) + word[position])
    print('El nif completo es:', complete)

    for i in customers:
        if i == complete:
            print('Este nif ya existe')
            return
new_nif()
"""
Crearemos una función con el nombre nuevo_id_articulo(). Que no recibirá ningún parámetro.
Al llamar a esta función, nos pedirá un ID de artículo. Este id ha de ser numérico.
Y en caso de ser un id correcto, nos devolverá dicho ID.
Esta función lanzará excepciones en caso que:
 El ID que introduzca el usuario no sea numérico.
 El ID ya exista en el diccionario dict_articulos.
Y nos mostrará un mensaje descriptivo del error correspondiente, volviendo a pedir un ID al
usuario.
"""
def new_article_ID():
    dict_items = {0: 12345, 1: 47261, 2: 83424, 3: 84654, 4: 94164, 5: 31254}
    ask = True
    while ask:
        valid = False
        while not valid:
            try:
                new_id = int(input('Entrar ID del producto: '))
                valid = True
            except ValueError:
                print('La identificación debe contener todos los números.')
        found = False
        for i in range(0, len(dict_items)):
            if new_id == dict_items[i]:
                print('Esta identificación ya está registrada')
                found = True
        if found == False:
            return
new_article_ID()
"""
Crearemos una función con el nombre nuevo_stock_artículo(). Que no recibirá ningún
parámetro.
Al llamar a esta función, nos pedirá por consola un entero positivo, y en caso de ser correcto, nos lo
devolverá.
Esta función lanzará excepciones en caso que:
 El stock que introduzca el usuario no sea numérico o sea negativo.
Y nos mostrará un mensaje descriptivo del error correspondiente, volviendo a pedir un stock al
usuario
"""
def new_stock_item():
    valid_input = False
    while not valid_input:
        try:
            amount = int(input('Ingrese la cantidad de stock: '))
            if amount >= 0:
                print('El stock se ha actualizado a ', amount)
                valid_input = True
            else:
                print('El stock debe ser 0 o superior.')
        except ValueError:
            print('Entrada incorrecta. La cantidad debe ser un número.')
new_stock_item()

"""
Crearemos una función con el nombre nuevo_precio_artículo(). Que no recibirá ningún
parámetro.
Al llamar a esta función, nos pedirá un precio que ha de ser un entero positivo, y en caso de ser
correcto, nos lo retornará.
Esta función lanzará excepciones en caso que:
 El precio que introduzca el usuario no sea numérico o sea negativo.
Y nos mostrará un mensaje descriptivo del error correspondiente, volviendo a pedir un precio al
usuario.
"""
def new_item_price():
    valid_input = False
    while not valid_input:
        try:
            amount = int(input('Entra un precio: '))
            if amount >= 0:
                print('El precio se ha actualizado a', amount)
                valid_input = True
            else:
                print('El precio debe ser 0 o superior.')
        except ValueError:
            print('Entrada incorrecta. El precio debe ser un número entero..')
new_item_price()
"""
Crearemos una función con el nombre nuevo_nombre_articulo(). Que no recibirá ningún
parámetro.
Al llamar a esta función, nos pedirá el nombre de un artículo, y en caso de no existir, nos lo
devolverá.
Esta función lanzará excepciones en caso que:
 El nombre que introduzca el usuario ya exista en el diccionario dict_articulos.
Y nos mostrará un mensaje descriptivo del error correspondiente, volviendo a pedir un nombre al
usuario
"""
def new_item_name():
    dict_items = {0: 'sofa', 1: 'chair', 2: 'wireless charger', 3: 'car charger'}
    cool = False
    while not cool:
        try:
            name = str(input('Ingrese el nombre del artículo: '))
            cool = True
        except ValueError:
            print('El nombre debe ser una cadena sin números.')
    noice = True
    for i in dict_items:
        if dict_items[i] == name:
            print('¡Este artículo ya existe!')
            noice = False
    if noice:
        return
    else:
        new_item_name()
new_item_name()
"""
#funcion que se encarga de imprimir datos de la forma del ejemplo
"""
def imprimir_datos(cabecera, datos, pie="", titulo=""):
    print(titulo, '\n')
    data_output = ""
    for i in cabecera:
        data_output += i
        data_output += '\t' * 5
    print(data_output)
    print('*' * len(data_output) * 2)
    for row in range(0, len(datos)):
        data_output = ""
        for items in datos[row]:
            data_output += str(items)
            data_output += '\t' * 5
        print(data_output)
    if pie != "":
        print("=" * len(pie))
        print(pie)
imprimir_datos(("ID", "Name", "Stock", "Price"), [(1, 'article1', 10, 22), (2, 'article2', 12, 32), (3, 'article3', 9, 42), (4, 'article4', 6, 52)], pie="Total".ljust(68) + "1000".ljust(20))

"""
Crearemos una función:
ordenar_lista(lista, orden)
Que recibirá dos parámetros, “lista” y “orden”.
El nombre de la función y de los parámetros será exactamente igual al del enunciado.
Esta función nos retornará la lista que le pasemos por parámetro ordenada ascendentemente si el
parámetro “orden” es igual a “asc”, o descendentemente si el parámetro “orden” es igual a “des”.
Esta función lanzará excepciones en los casos:
 Que el parámetro lista no sea una lista.
 Que los valores a comparar en la lista no sean del mismo tipo.
 Que demos un valor al parámetro orden y no sea ni “des” ni “asc”.
Y en cada uno de estos casos se recogerá la excepción y se mostrará un mensaje descrptivo del
error.
"""
def ordenar_lista(lista, orden):
    # Primero, verificamos que todas las condiciones sean correctas.
    # Orden debe ser asc o des
    if orden == 'asc' or orden == 'des':
        # La variable lista debe ser una lista.
        if type(lista) == list:
            # La variable lista debe tener al menos 1 elemento
            if len(lista) > 0:
                # Y finalmente, todos los elementos de la lista deben ser del mismo tipo.
                items_type = type(lista[0])
                for i in lista:
                    if type(i) != items_type:
                        print('Todos los elementos de la lista deben ser del mismo tipo.')
                        return
            else:
                print('ERROR. La lista debe tener al menos 1 elemento.')
                return
        else:
            print('ERROR. Lista no es una lista. Inserta una lista, por favor..')
            return
    else:
        print('ERROR. Parámetro de orden incorrecto proporcionado. Debe ser "asc" o "des".')
        return
    if orden == 'asc':
        lista.sort()
    else:
        lista.sort(reverse=True)

"""
Crearemos una función:
ordenar_diccionario_por_valor(diccionario, orden, key= "")
Que recibirá 3 parámetros, “diccionario”, “orden” y “key”.
El nombre de la función y de los parámetros será exactamente igual al del enunciado.
El primer parámetro será un diccionario, que será del tipo:
{clave-1: valor-1, clave-2: valor-2, …., clave-n: valor-n}
donde los valores valor-1, valor-2, …, valor-n son tipos simples ( int, string, float )
o del tipo:
{
clave-1: diccionario-1={key-1:value-1, key-2:value-2,…,key-m:value-m},
clave-2: diccionario-2={key-1:value-1, key-2:value-2,…,key-m:value-m},
.
.
.clave-n: diccionario-n={key-1:value-1, key-2:value-2,…,key-m:value-m}
}
donde los diccionarios diccionario-1, diccionario-2,…,diccionario-n, tiene las mismas claves.
Como ejemplo de este segundo diccionario tenemos el diccionario dict_articles del ejercicio
negocio.
El segundo parámetro sólo podrá tomar los valores “asc” o “des”
El tercer parámetro será opcional con valor por defecto a “” y sólo podrá tomar como valor una de
las claves de los diccionarios diccionario-1, diccionario-2,…,diccionario-n, es decir, key-1, key2 ...key-n.
Si pasamos un diccionario del segundo tipo, es decir, diccionario de diccionarios, deberemos
especificar el parámetro key como uno de los valores key-1, key-2 ...key-n.
Es este caso la función retornará una lista con las claves del diccionario que pasamos como
parámetro [clave-1, clave-2, …,clave-n] ordenadas según el valor de la clave que hayamos
especificado como key, de forma ascendente si orden=”asc” o de forma descendente si orden=”des”
Es decir, si pasamos como parámetros dict_articles,”des”,”stock”.
dict_articles = {
4: { "Nom_article": "article4", "stock": 6, "preu": 152},
2: { "Nom_article": "article2", "stock": 12, "preu": 132},
3: { "Nom_article": "article3", "stock": 9, "preu": 642},
}
La función, nos devolverá la lista [2,3,4] ya que el stock 12 es el mayor y corresponde al id 2, el
stock 9 es el segundo mayor y corresponde al id 2, y el stock 6 es el menor y corresponde al id 4.
Si el diccionario que pasamos como parámetro es del primer tipo, no se deberá especificar el
parámetro key, sólo el parámetro orden.
En este caso la función nos retornará una lista con los id’s del diccionario ordenados por los valores
del diccionario, en orden ascendente si el parámetro orden es “asc”, o en orden descendente si el
parámetro orden es “des”.
Es decir si pasamos como parámetros “dict”,”des”.
dict = {3: 5, 4: 4, 1: 5, 2: 2}
nos devolverá la lista
[3, 1, 4, 2]
Esta función lanzará excepciones en caso de:
 Que demos un valor al parámetro key, pero los valores del diccionario no sean diccionarios.
 Que no demos un valor al parámetro key y los valores del diccionario sean diccionarios.
 Que demos un valor al parámetro key pero no exista esta key en los diccionarios que aplica.
 En cualquier caso que los valores que comparemos no sean del mismo tipo.
 Que demos un valor al parámetro orden y no sea ni “des” ni “asc”.
Y en cada uno de estos casos se recogerá la excepción y se mostrará un mensaje descrptivo del
erro
"""
def ordenar_diccionario_por_valor(diccionario, orden, key=""):
    # Comprueba si diciconario es un diccionario
    if type(diccionario) == dict:
        # Compruebe si orden es 'des' o 'asc'
        if orden == 'des' or orden == 'asc':
            # Compruebe si los elementos del diccionario también son diccionarios.
            for item in diccionario:
                if type(diccionario[item]) != dict:
                    print('Los elementos del diccionario deben ser diccionarios.')
                    return
        else:
            print('orden debe ser "asc" o "des".')
            return
    else:
        print('diccionario debe ser un diccionario.')
        return
    # Ahora, el programa comprueba si el valor de la clave se ha dado o no, y devuelve las claves del diccionario ordenadas.
    if key == "":
        if orden == 'des':
            dictionary = dict(sorted(diccionario.items(), key=lambda item: item[1].get("stock"), reverse=True))
        else:
            dictionary = dict(sorted(diccionario.items(), key=lambda item: item[1].get("stock"), reverse=False))
        print(dictionary.keys())
    else:
        try:
            if orden == 'des':
                dictionary = dict(sorted(diccionario.items(), key=lambda item: item[1].get(key), reverse=True))
            else:
                dictionary = dict(sorted(diccionario.items(), key=lambda item: item[1].get(key), reverse=False))
            print(dictionary.keys())

        # En caso de que la clave dada no esté en el diccionario, se da un error de valor de clave no válido.
        except:
            print('Valor de clave no válido.')
ordenar_diccionario_por_valor({
4: { "Nom_article": "article4", "stock": 6, "preu": 152},
2: { "Nom_article": "article2", "stock": 12, "preu": 132},
3: { "Nom_article": "article3", "stock": 9, "preu": 642},
}, 'asc')
