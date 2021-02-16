"""
a) Utilitzant el mètode sort o sorted, ordeneu la llista pel camp matrícula en ordre
   descendent:
    tuples_cotxes = [
    ('Vermell, '4859-A', 'A'),
    ('Blau', '2901-Z', 'M'),
    ('Gris', '1892-B', 'M')]

b) Utilitzant el mètode sort o sorted, ordeneu la llista pel camp color en ordre ascendent:
   diccionari_cotxes = [
    {'color': 'Vermell', 'matricula': '4859-A', 'canvi': 'A'},
    {'color': 'Blau', 'matricula': '2901-Z', 'canvi': 'M'},
    {'color': 'Gris', 'matricula': '1892-B', 'canvi': 'M'}]

c) En el següent diccionari apareixen les ciutats i la seva temperatura en graus kelvin i
   Celsius, utilitzant el mètode sort o sorted, ordeneu la llista pel graus Celsius en ordre
   ascendent.
    graus={
    "Londres" : (295, 22),
    "Madrid": (309, 36),
    "Barcelona": (293, 20),
    "Sevilla": (299, 26),
    "Cádiz": (303, 30),
    "Lima": (311, 38)}

d) Utilitzant les següents dades:
    diccionari_cotxes = [
    {'color': 'Vermell', 'matricula': '4859-A', 'canvi': 'A'},
    {'color': 'Blau', 'matricula': '2901-Z', 'canvi': 'M'},
    {'color': 'Gris', 'matricula': '1892-B', 'canvi': 'M'},
    {'color': 'Blanc', 'matricula': '3392-R', 'canvi': 'M'}]

    dic_compradors={
    "12345678Z": {'nom': 'Anna', 'matricula': '4859-A', 'edat': 33},
    "98765432M": {'nom': 'Carolina', 'matricula': '2901-Z', 'edat': 55},
    "23456789D": {'nom': 'Aaron', 'matricula': '1892-B', 'edat': 38},
    "33356789G": {'nom': 'Pol', 'matricula': '3392-R', 'edat': 21}}

    Creeu una funció que mostri els compradors de cotxe de canvi ‘M’
    (“manual”)ordenats per edat en ordre creixent. S’hauran de mostrar totes
    les dades del comprador en un format adequat
"""
# A)
tuples_cotxes = [("Vermell", "4859-A", "A"),("Blau", "2901-Z", "M"),("Gris", "1892-B", "M")]
ordenados = sorted(tuples_cotxes, key=lambda coche : coche[1],reverse=True)
print(" A) Utilitzant el mètode sort o sorted, ordeneu la llista pel camp matrícula en ordre descendent:")
print(ordenados)
print("-------------------------------------------------------------------------------------------------")


# B)
diccionari_cotxes = [
    {'color': 'Vermell', 'matricula': '4859-A', 'canvi': 'A'},
    {'color': 'Blau', 'matricula': '2901-Z', 'canvi': 'M'},
    {'color': 'Gris', 'matricula': '1892-B', 'canvi': 'M'}]
ordenados = sorted(diccionari_cotxes, key=lambda coche : coche['color'],reverse=False)
print(" B)Utilitzant el mètode sort o sorted, ordeneu la llista pel camp color en ordre ascendent:")
print(ordenados)
print("-------------------------------------------------------------------------------------------------")


# C)
graus={
    "Londres" : (295, 22),
    "Madrid": (309, 36),
    "Barcelona": (293, 20),
    "Sevilla": (299, 26),
    "Cádiz": (303, 30),
    "Lima": (311, 38)}
ordenados = sorted(graus.items(), key=lambda Celcius: Celcius[1][1],reverse=True)
print(" C) En el següent diccionari apareixen les ciutats i la seva temperatura en graus kelvin i "
      "Celsius, utilitzant el mètode sort o sorted, ordeneu la llista pel graus Celsius en ordre"
      "ascendent.:")
print(ordenados)
print("-------------------------------------------------------------------------------------------------")


# D)
diccionario_cotxes = [
    {'color': 'Vermell', 'matricula': '4859-A', 'canvi': 'A'},
    {'color': 'Blau', 'matricula': '2901-Z', 'canvi': 'M'},
    {'color': 'Gris', 'matricula': '1892-B', 'canvi': 'M'},
    {'color': 'Blanc', 'matricula': '3392-R', 'canvi': 'M'}]

dic_compradors={
    "12345678Z": {'nom': 'Anna', 'matricula': '4859-A', 'edat': 33},
    "98765432M": {'nom': 'Carolina', 'matricula': '2901-Z', 'edat': 55},
    "23456789D": {'nom': 'Aaron', 'matricula': '1892-B', 'edat': 38},
    "33356789G": {'nom': 'Pol', 'matricula': '3392-R', 'edat': 21}}

print(" D) Creeu una funció que mostri els compradors de cotxe de canvi ‘M’"
      "(“manual”)ordenats per edat en ordre creixent. S’hauran de mostrar totes"
      "les dades del comprador en un format adequat")
print("-------------------------------------------------------------------------------------------------")

def compradorManual(dic_compradors,diccionario_cotxes):
    lista=[]
    for mat in dic_compradors.values():
        for j in diccionari_cotxes:
            if mat["matricula"]==j["matricula"] and j["canvi"]=="M":
                lista.append(mat)
    lista=sorted(lista,key=lambda elemento: elemento["edat"],reverse=False)
    return lista
print(compradorManual(dic_compradors,diccionari_cotxes))
