"""Funciones de operaciones"""
def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    while True:
        try:
            c = a / b
        except ZeroDivisionError:
            c = 0
        return c