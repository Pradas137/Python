"""Funcion que Validad un usuario"""
def usuario(user):
    name = len(user)
    u = user.isalnum()
    if u == False:
        print("El nombre de usuario solo puede contener letras y números")
    if name < 6:
        print("El nombre de usuario debe contener al menos 6 caracteres")
    if name > 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")
    if name > 5 and name < 13 and u == True:
        return True