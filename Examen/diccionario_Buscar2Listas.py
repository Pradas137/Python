import random
# Una rata elige al azar entre 3 formas. La ruta 1 tiene una duración de 3 minutos. La ruta 2 tiene una duración de 5 minutos. La ruta 3 dura 7 minutos y sale de la jaula (opción correcta).
def rat(time):
    route = random.randrange(1,4)
    if route == 1:
        print("Route 1. +3 minutes")
        return rat(time + 3)
    elif route == 2:
        print("Route 2. +5 minutes")
        return rat(time + 5)
    else:
        print("Route 3. +7 minutes")
        return (time + 7)
print("Total: ", rat(0))

# Iterar diccionarios de forma recursiva
D1={1: {2: {3: 4, 5: 6}, 3: {4: 5, 6: 7}}, 2: {3: {4: 5}, 4: {6: 7}}}
def iterdict(d):
  for k,v in d.items():
     if isinstance(v, dict):
         iterdict(v)
     else:
         print (k,":",v)
iterdict(D1)

# Buscar y comparar en dos listas de forma recursiva

def search(list1, list2):
    for i in list2:
        if i == list1[0]:
            return True
    if len(list1) == 1:
        return False
    else:
        return search(list1[1:], list2)
print(search([1, 2, 4], [5, 2, 5]))
