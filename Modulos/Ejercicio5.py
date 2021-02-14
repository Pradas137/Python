"""El ejercicio consiste en llamar con importaciones a los ejercicions de validacion user y password
i comprovar que funcionan"""
from Validaciones.Ejercicio3 import usuario
from Validaciones.Ejercicio4 import contrasenya

correcto=False
while correcto==False:
        nombre=input("Ingrese nombre de usuario: ")
        if usuario(nombre) == True:
            print("Usuario creado exitosamente")
            correcto=True

while correcto==True:
    contrasenia=input("Ingrese su Password: ")
    if contrasenya(contrasenia)==True:
        print("Contraseña creada exitosamente")
        correcto=False