def draw_triangle(n):
    if n == 0:
        return ''
    else:
        return ("*" * n + '\n') + draw_triangle(n - 1)

def main():
    num = int(input("Entra un numero: "))
    triangle = draw_triangle(num)
    print(triangle)
main()
