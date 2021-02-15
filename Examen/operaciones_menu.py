# Este programa tiene varias funciones, que son programas realmente simples.

########################
# DECLARACIÓN DE FUNCIONES #
########################

# Función para calcular el precio final cuando se aplica un descuento.
def discounted_price(original, percent):
    return original - (original * percent / 100)


# Función para leer números. Solo hace eso, pide al usuario un número y léelo.
def read0to10():
    num = float(input("Enter a number between 0 and 10: "))
    print("The chosen number is...", num, "!")
    return num


# Función para comprobar si una letra determinada es vocal o no.
def vowel_check(character):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel = False
    maybe_vowel = character.lower()
    for i in vowels:
        if i == maybe_vowel:
            vowel = True
    return vowel


# Función para multiplicar números en una lista
def multiplier(num_list):
    result = 1
    for i in num_list:
        result = result * i
    return result


# Función que crea múltiples histogramas dada una lista
def histogram(numbers_to_multiply):
    for i in numbers_to_multiply:
        print(i * '*')


def words_filter(words_list, minimum_length):
    print('The chosen words are: \n')
    for word in words_list:
        if len(word) > minimum_length:
            print('- ', word)


def uppercase_counter(string):
    counter = 0
    for character in string:
        if character.isupper():
            counter += 1
    print('There are', counter, 'uppercase letters.')


####################
# PROGRAMA PRINCIPAL #
####################

flag_menu = False

while not flag_menu:
    print(
        "1.-EXERCISE 1. FINAL PRICE WITH DISCOUNT\n2.-EXERCISE 2. NUMBER 0-10\n3.-EXERCISE 3. VOWEL OR NOT\n"
        "4.-EXERCISE 4. LIST NUMBERS MULTIPLICATION\n5.-EXERCISE 5. HISTOGRAM\n"
        "6.-EXERCISE 6. WORDS IN ARRAY LONGER OR EQUAL THAN X\n7.-EXERCISE 7. UPPERCASE COUNTER\n"
        "8.-EXIT\nCHOOSE AN OPTION:")
    option = int(input())
    if option == 1:
        # Definir y programar una función que, dado un precio y un descuento, devuelva el precio final con descuento.
        # La función tiene dos parámetros: precio y porcentaje. Devuelve el precio final.

        print("EXERCISE 1.")

        discount = 30
        price = float(input("Enter the price: "))
        print("Final price is: ", discounted_price(price, discount))

    elif option == 2:
        # Cree una función "read0to10" que le pida al usuario un número entre 0 y 10. Si el número dado es menor
        # o superior, el programa sigue solicitando uno nuevo.
        # La función no tiene parámetros y devuelve el número dado por el usuario.

        print("EXERCISE 2")

        between = False
        while not between:
            number = read0to10()
            if 0 <= number <= 10:
                between = True
                print("That's between 0 and 10!")
            else:
                print("That's not between 0 and 10.")

    elif option == 3:
        # Escribe una función que, dado un carácter, devuelve si es vocal o no. El formato de retorno es Verdadero / Falso

        print('EXERCISE 3')

        letter = input('Please, enter a letter: ')
        print(vowel_check(letter))

    elif option == 4:
        # Escribe una función que multiplique todos los elementos de una lista. Ejemplo: [1,2,3,4] debería devolver 24

        print("EXERCISE 4")

        num1 = int(input('Please, enter a number: '))
        num2 = int(input('Please, enter a second number: '))
        num3 = int(input('Please, enter a third number: '))
        num4 = int(input('Please, enter a fourth number: '))
        nums = [num1, num2, num3, num4]
        print('The result of multiplying all the numbers is: ', multiplier(nums))

    elif option == 5:
      # Escriba un programa que tenga una función llamada "histograma".
        # Esta función obtendrá elementos de una lista de números enteros e imprimirá un histograma en la pantalla usando *.

        print("EXERCISE 4")

        nums_to_multiply = [1, 3, 5, 7, 5, 3, 1]
        histogram(nums_to_multiply)

    elif option == 6:
         # Escriba un programa que tenga una función llamada words_filter, que obtenga una matriz con palabras, un número entero y
        # devuelve las palabras de más de n caracteres.

        print("EXERCISE 5")

        words = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'nunc', 'mi', 'lectus',
                 'suscipit', 'non', 'bibendum', 'et', 'fringilla', 'ut', 'arcu', 'sed']

        limit = int(input('Enter the minimum length: '))
        words_filter(words, limit)

    elif option == 7:
        # Escriba una función que le pida al usuario una cadena y le diga cuántos caracteres en mayúscula hay.

        print("EXERCISE 6")

        phrase = input('Enter a phrase: ')
        uppercase_counter(phrase)

    else:
        flag_menu = True
        print("PROGRAM ENDED")
