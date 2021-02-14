"""La funcion de esta prectica consiste en en un login que cuando el usuario y password son correctos,
 te accede a un menu que realiza ciertas operaciones que son llamadas por otras funciones """
import math
database={'name': '1234', 'name2': '5678', 'adrian': '9012'}
def login():
    while True:
        try:
            name = input('Enter username: ')
            pwd = input('Enter pin: ')
            username = name.isalpha()
            password = pwd.isalnum()
            if username == False:
                raise
            if password == False:
                raise
            if pwd in database[name]:
                print('Welcome', name)
            else:
                print('Invalid code')
        except Exception:
            print("El usuario solo puede tener letras")
        except:
            print("La Password de usuario solo puede contener letras y números")
        else:
            return True

def arrel_Quadrada():
    while True:
        try:
            num = int(input("escrive un numero:"))
            if num < 0:
                raise
            return math.sqrt(num)
        except:
            print("El numero es Negativo")

def division_entera():
    try:
        dividendo = int(input("escrive un dividendo"))
        divisor = int(input("escrive un divisor"))
        return dividendo/divisor
    except ZeroDivisionError:
        raise ZeroDivisionError("y no puede ser cero")

def opera_F():
    while True:
        try:
            x = int(input("introduce un numero:"))
            if x < 100:
                raise
            return x-100
        except:
            print("El numero añadido es menor que 100")

def menu():
    print("\n============================================================")
    print("============ Menu ============================================")
    print("=============================================\n===============")
    print("======= 1. Calcular l’arrel quadrada d’un número  ============")
    print("======= 2. Calcular la divisió entre dos números. ============")
    print("======= 3. Calcular el resultat de la funció: f(x)= x-100  ===")
    print("======= 4. salida ==========================================\n")
    print("=============================================\n===============")
    while True:
        opcio = input("\nIntroduce una opcion:  ")
        if opcio == '1':
            print(arrel_Quadrada())
        if opcio == '2':
            a = division_entera()
            print("el resultado de la division es: ", a)
        if opcio == '3':
            res = opera_F()
            print("el resultado de la operacion es: ", res)
        if opcio == '4':
            break
def main():
    log = login()
    if log == True:
         menu()
main()