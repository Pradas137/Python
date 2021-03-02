def burbuja_recursiva_diagonal_invertida(list, iteraciones, comparaciones):
    if iteraciones > len(list) - 2:
        return list
    if comparaciones > len(list[iteraciones]) - 1:
        return burbuja_recursiva_diagonal_invertida(list, iteraciones + 1, 0)
    if comparaciones < len(list[iteraciones]) - 1 and iteraciones < len(list) - 1:
        if list[iteraciones][-comparaciones] > list[iteraciones + 1][-comparaciones + 1]:
            list[iteraciones][-comparaciones], list[iteraciones + 1][-comparaciones + 1] = list[iteraciones + 1][-comparaciones + 1], list[iteraciones][-comparaciones]
    if comparaciones < len(list[iteraciones])-1 and iteraciones > 0:
        if list[iteraciones - 1][comparaciones + 1] > list[iteraciones][comparaciones]:
            list[iteraciones - 1][comparaciones + 1], list[iteraciones][comparaciones] = list[iteraciones][comparaciones], list[iteraciones - 1][comparaciones + 1]
    return burbuja_recursiva_diagonal_invertida(list, iteraciones, comparaciones + 1)


matriz = [[99, 4, 3, -1], [-5, 4, -8, 55], [33, -1, -5, -3], [-2, 6, 8, 5]]
print(burbuja_recursiva_diagonal_invertida(matriz, 2, 3))
#[[99,4,3,-1], [-5,4,-8,55], [33,-1,-5,-3], [-2, 6, 8, 5]]

