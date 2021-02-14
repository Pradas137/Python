def division_entera():
    try:
        dividendo = int(input("escrive un dividendo"))
        divisor = int(input("escrive un divisor"))
        return dividendo/divisor
    except ZeroDivisionError:
        raise ZeroDivisionError("y no puede ser cero")
