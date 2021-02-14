"""Funcion que Validad un password"""

def contrasenya(pwd):
    validar = False
    long = len(pwd)
    espacio = False
    mayuscula = False
    minuscula = False
    numeros = False
    y = pwd.isalnum()
    correcto = True
    for carac in pwd:
        if carac.isspace() == True:
            espacio = True
        if carac.isupper() == True:
            mayuscula = True
        if carac.islower() == True:
            minuscula = True
        if carac.isdigit() == True:
            numeros = True
    if espacio == True:
        print("La contraseña no puede contener espacios")
    else:
        validar = True
    if long < 8 and validar == True:
        print("Mínimo 8 caracteres")
        validar = False
    if mayuscula == True and minuscula == True and numeros == True and y == False and validar == True:
        validar = True
    else:
        correcto = False
    if validar == True and correcto == False:
        print("La contraseña elegida no es segura:")
        return True