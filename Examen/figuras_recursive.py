import random
def figuras(mat,nf,nc ):
    if (nf >=0):
        if(nf+nc >= 4):
            print(mat[nf][nc])
        else:
            print("-")
        nc=nc-1
        if(nc>=0):
            figuras(mat,nf,nc )
        else:
            print("\n")
            figuras(mat,nf-1,4)
mat=[None]*5
for i in range(0,5):
    mat[i]= [None]*5
for i in range(0,5):
    for j in range(0,5):
        mat[i][j]= random.randint(1,9)
figuras(mat,4,4)

def draw_triangle(n):
    if n == 0:
        return ''
    else:
        return ("*" * n + '\n') + draw_triangle(n - 1)

def main():
    num = int(input("Enter an integer: "))
    triangle = draw_triangle(num)
    print(triangle)
main()
