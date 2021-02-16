from Examen.Operaciones_main import *
tupla1=("sumarLista", "harmonic_sum","Sub_menu","Salir")
tupla2=("Suma", "Multiplicacion","Salir")
#GENERAR MENU
def menu_generator(options, header="\n"):
    flag_menu = False
    while not flag_menu:
        print(header)
        for i in range(len(options)):
            print(i+1, ")", options[i])
        try:
            user_option = int(input("Choose an option: "))
            if 0 < user_option <= len(options):
                flag_menu = True
                return user_option
            else:
                print("Invalid option.")
                flag_menu = False
        except ValueError:
            print("That's no a number. Try again.")

#menu_generator("Suma", "Multiplicacion","Sub_menu","Salir", header='MAIN MENU')

#GENERAR SUBMENU
def submenu_generator(options, header="\n"):
    flag_menu = False
    while not flag_menu:
        print(header)
        for i in range(len(options)):
            print(i+1, ")", options[i])
        try:
            user_option = int(input("Choose an option: "))
            if 0 < user_option <= len(options):
                flag_menu = True
                return user_option
            else:
                print("Invalid option.")
                flag_menu = False
        except ValueError:
            print("That's no a number. Try again.")

#submenu_generator("sumadesc", "binario","Salir", header='MAIN MENU')

flag_principal = False
while not flag_principal:
    opcion_menu = menu_generator(tupla1,"MENU")
    if opcion_menu == 1:
            print(sumarLista([2, 4, 5, 6, 7]))
    elif opcion_menu == 2:
            print(harmonic_sum(7))
    elif opcion_menu == 3:
        print("opcion MENU2")
        flag_secundario = False
        while not flag_secundario:
            opcion_submenu = submenu_generator(tupla2,"SubMenu")
            if opcion_submenu == 1:
                print("opcion Submenu1")
            elif opcion_submenu == 2:
                print("opcion Submenu2")
            elif opcion_submenu == 3:
                salir = True
                break
    elif opcion_menu == 4:
        salir = True
        break
