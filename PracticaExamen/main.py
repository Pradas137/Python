tupla_menu02 = ("Buscar Compras","Listar Compras","Crear Compra","Menu Principal")
tupla_menu011 = ("Listar por id","Listar por nombre","Listar por stock","Volver Atras")

dict_articles = {4: {"Nom_article":"Monitor Packard Bell","stock":6,"preu": 152},
 3: {"Nom_article":"Monitor Acer","stock": 12,"preu": 132},
 2: {"Nom_article":"Portatil Toshiba", "stock": 9,"preu": 642},
 1: {"Nom_article":"Portatil Acer","stock": 10,"preu": 522}
 }
dict_compres = {"AA32E": {"Data": (2020,11,1), "total_compra": 284},
 "AB37Z": {"Data": (2020,11,1), "total_compra": 674},
 "CF13U": {"Data": (2020,11,1), "total_compra": 1698},
 "KL11T": {"Data": (2020,11,1), "total_compra": 806},
 "ST234": {"Data": (2019,12,7), "total_compra": 1296}
 }
dict_clients = {"34343434A": {"nombre": "Pedro", "telefono": "666994455"},
 "78787878A": {"nombre": "Luis", "telefono": "666765432"},
 "39292939A": {"nombre": "Jose Luis", "telefono": "666232211"}
 }
cliente_compra = {"34343434A": ["AA32E", "AB37Z"], "78787878A": ["CF13U", "KL11T"],
"39292939A": ["ST234"]}

compra_article = {"AA32E": [3,4], "AB37Z": [1,4], "CF13U": [1,1,1,3], "KL11T": [1,3,4],
"ST234": [1,2,3]}

compra_client = {"AA32E": "34343434A", "AB37Z": "34343434A", "CF13U": "78787878A",
"KL11T": "78787878A","ST234": "39292939A"}

#CADA PARTE DE LOS EJERCICIOS ESTA COMENTADA

#funcion que se encarga de crear un menu de opciones atravez de una tapla ya creada.

"""def menus(tupla_menu02,cabezera=" "):
 while True:
  try:
   count = 1
   print(cabezera)
   for tupla in tupla_menu02:
    print(" " + str(count) + " -> " + tupla)
    count += 1
   opcion = input("\nElige una opcion del (1-4):")
   opcion = int(opcion)
   if opcion > len(tupla_menu02) or opcion < 1:
    raise
   opciontupla = tupla_menu02[opcion]
   print("Elegiste {} .".format(opciontupla))
  except Exception:
     print("Error elegiste un numero mallor que 4 o menor de 1")

menus(tupla_menu02)
"""

#funcion que se encarga de pedir un nif i validarlo con las especificaciones marcadas

"""def peticion_nif():
 while True:
  try:
   tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
   numeros = "1234567890"
   nif = input("Introduzca el NIF: ")
   if (len(nif) == 9) and nif[8] == tabla[nif[:8]%23]:
    return nif
   else:
    raise Exception
  except Exception:
     print("No ha introducido un NIF valido")
peticion_nif()"""

#funcion que se encarga de pedir un id nuevo i validarlo con las especificaciones marcadas y comprueva si existe
"""
def nuevo_id_articulo():
 while True:
  try:
   id = int(input("introduce un id:"))
   if id in dict_articles.keys():
    raise
   return id
  except ValueError:
    print("No cumple las condiciones")
  except:
   print("Error: ya existe")
print(nuevo_id_articulo())
"""
#funcion que se encarga de pedir un stock nuevo i validarlo con las especificaciones marcadas
"""
def nuevo_stock_artículo():
 while True:
  try:
   numero = int(input("Ingrese un numero stock:"))
   if numero >= 0:
    return ("El numero es válido", numero)
   if numero < 0:
    raise Exception
  except ValueError:
   print("La opción que ingreso no es un numero")
  except Exception:
   print("El numero es negativo")
print(nuevo_stock_artículo())
"""
#funcion que se encarga de pedir un precio de un articulo nuevo i validarlo con las especificaciones marcadas.
"""
def nuevo_precio_artículo():
 while True:
  try:
   numero = float(input("Ingrese un numero precio:"))
   if numero >= 0:
    return numero
   if numero < 0:
    raise Exception
  except ValueError:
   print("La opción que ingreso no es un numero")
  except Exception:
   print("El numero es negativo")
print(nuevo_precio_artículo())
"""
#funcion que se encarga de pedir un nuevo nombre i validarlo con las especificaciones marcadas y comprueva si existe.

"""def nuevo_nombre_articulo():
 while True:
  try:
   nombre = input("escrive el nombre del articulo")
   if nombre != dict_articles.values():
    print(nombre)
   if nombre in dict_articles.values():
    raise
  except:
   print("Error: ya existe")
nuevo_nombre_articulo()"""

#funcion que se encarga de imprimir datos de la forma del ejemplo
"""
cabecera = ("ID","Nombre","Stock","Precio")
datos = [(1,'articulo1',10,22),(2,'articulo2',12,32),(3,'articulo3',9,42),(4,'articulo4',6,52)]
pie ="Total".ljust(40)+"1000".ljust(20)
titulo = "Articulos Ordenados por Nombre"
def imprimir_datos(cabecera,datos,pie,titulo):
 print(titulo)
 print(cabecera[0].ljust(15),cabecera[1].ljust(15),cabecera[2].ljust(11),cabecera[3].ljust(12))
 print("*"*53)
 for intem in datos:
  print("|",intem[0]," "*(9-len(str(intem[0]))),"|",intem[1]," "*(9-len(intem[1])),"|",intem[2]," "*(9-len(str(intem[2]))),"|",intem[3]," "*(9-len(str(intem[3]))),"|")
 print("*"*53
 print(pie)
imprimir_datos(cabecera,datos,pie,titulo)
"""

"""
def imprimir_datos(cabecera, datos, pie="", titulo=""):
 print("{:^80}".format(titulo.upper()))
 print("*" * 80)
 for subtitulo in cabecera:
  print("{:^20}".format(subtitulo), end="")
 print("")
 print("*" * 80)
 for dato in datos:
  for elemento in dato:
   print("{:^20}".format(elemento), end="")
  print()
 print("*" * 80)
 print(pie)
 imprimir_datos(cabecera, datos, "", titulo)
"""
"""
def imprimir_datos(cabecera,datos,pie,titulo):
 print(titulo)
 print(cabecera[0].ljust(15),cabecera[1].ljust(15),cabecera[2].ljust(11),cabecera[3].ljust(12))
 print(""53)
 for intem in datos:
  print("|",intem[0]," "(9-len(str(intem[0]))),"|",intem[1]," "(9-len(intem[1])),"|",intem[2]," "(9-len(str(intem[2]))),"|",intem[3]," "(9-len(str(intem[3]))),"|")
 print(""53)
 suma=0
 for i in datos:
     suma+=i[2]*i[3]
 print(pie.ljust(40)+str(suma).ljust(20))

cabecera = ("ID", "Nombre", "Stock", "Precio")
datos = [(1, 'articulo1', 10, 22), (2, 'articulo2', 12, 32), (3, 'articulo3', 9, 42), (4, 'articulo4', 6, 52)]
pie ="Total"
titulo = "Articulos ordenados por nombre"
imprimir_datos(cabecera,datos,pie,titulo)
"""
#funcion que se encarga de ordenar datos de una lista de forma ASC o DESC y Validarlos.
"""
Lista = [54, 26, 17, 77, 31, 44, 55, 1]
orden = "ASC"
def ordenar_lista(Lista, orden):
  try:
   if type(Lista) != list:
    raise TypeError
   if orden != "ASC" and orden != "DESC":
       raise
   if orden == "ASC":
    Lista.sort(reverse=True)
    print(Lista)
   if orden == "DESC":
    Lista.sort(reverse=False)
    print(Lista)
  except TypeError:
   print("No todos los valores de la lista son iguales")
  except:
   print("No es un ASC ni un DESC")

ordenar_lista(Lista, "DESC")
"""
"""
def ordenar_lista(lista, orden):
    try:
        orden=orden.lower()
        if type(lista)!=list:
            raise TypeError
        for elemento in range(len(lista)-1):
            if type(lista[elemento])!= type(lista[elemento+1]):
                raise TypeError
        if orden!="asc" and orden!="des":
            raise ValueError
        if orden=="asc":
            lista.sort(reverse=False)
        elif orden=="des":
            lista.sort(reverse=True)
    except TypeError:
        print("Error en el tipo de dato")
    except ValueError:
        print("Valor incorrecto")
    else:
        return lista
"""
#funcion que se encarga de ordenar un (diccionario de diccionario) de manera (ASC o DESC)
# y imprimir la key en una lista.


diccionario = dict_articles
def ordenar_diccionario_por_valor(diccionario, orden, clave= ""):
  try:
   print("Diccionario original: " + str(diccionario))
   if type(diccionario) != dict:
    raise TypeError
   if orden != "ASC" and orden != "DESC":
    raise
   if orden == "ASC":
    print("Orden Ascendente")
    s = list(diccionario.items())
    s = sorted(s, key=lambda s: s[1]["stock"],reverse=True)
    print(s)
    lista=[]
    for i in s:
     lista.append(i[0])
    print(lista)
   if orden == "DESC":
    print("Orden Descendente")
    s = list(diccionario.items())
    s = sorted(s, key=lambda s: s[1]["stock"], reverse=False)
    print(s)
    lista = []
    for i in s:
     lista.append(i[0])
    print(lista)
  except TypeError:
   print("No es un diccionario")
  except KeyError:
   print("Error en la Key")
  except:
   print("No es un ASC ni un DESC")
ordenar_diccionario_por_valor(diccionario, orden="ASC" , clave= "stock")
