dicc = {}


def billetes(bi):
    while bi != 0:
        if bi >= 500:
            div = bi // 500
            bi = bi % 500
            dicc['billetes 500'] = [div]
        elif bi >= 200:
            div = bi // 200
            bi = bi % 200
            dicc['billetes 200'] = [div]
        elif bi >= 100:
            div = bi // 100
            bi = bi % 100
            dicc['billetes 100'] = [div]
        elif bi >= 50:
            div = bi // 50
            bi = bi % 50
            dicc['billetes 50'] = [div]
        elif bi >= 20:
            div = bi // 20
            bi = bi % 20
            dicc['billetes 20'] = [div]
        elif bi >= 10:
            div = bi // 10
            bi = bi % 10
            dicc['billetes 10'] = [div]
        elif bi >= 5:
            div = bi // 5
            bi = bi % 5
            dicc['billetes 5'] = [div]
        elif bi >= 2:
            div = bi // 2
            bi = bi % 2
            dicc['monedas 2'] = [div]
        elif bi >= 1:
            div = bi // 1
            bi = bi % 1
            dicc['monedas 1'] = [div]


bi = int(input("Introduce un valor: "))
billetes(bi)
print(dicc)