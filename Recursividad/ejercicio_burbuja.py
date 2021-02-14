"""def burbujaRecursiva(lista,pasadas,comparaciones,fila):
    if fila==len(lista)-1 and (pasadas>len(lista[fila])-1):
        return lista
    else:
        if (pasadas>len(lista[fila])-1):
            return burbujaRecursiva(lista,0,0,fila+1)

        if comparaciones>len(lista[fila])-2-pasadas:
            return burbujaRecursiva(lista,pasadas+1,0,fila)

        elif lista[fila][comparaciones]>lista[fila][comparaciones+1]:
            lista[fila][comparaciones],lista[fila][comparaciones+1]=lista[fila][comparaciones+1],lista[fila][comparaciones]
        return burbujaRecursiva(lista,pasadas,comparaciones+1,fila)
lista=[[3,1,2],[8,4,5],[9,-1,2],[9,-1,2],[9,-1,2],[9,-1,2]]
print(burbujaRecursiva(lista,0,0,0))"""

#1.- Programar la función recursiva de la burbuja pero aplicada a columnas.
"""[ [99 , 2 , -1 ],
  [2 , 15, -2],
  [1, 5 , -7]   ]
SOL:
[ [1 , 2 , -7 ],
  [2 , 5, -2],
  [99, 15 , -1]   ]
"""
def recursive_bubble_v3(list, iterations, comparisons):
    if iterations > len(list)-2:
        return list
    if comparisons > len(list[iterations])-1:
        return recursive_bubble_v3(list, iterations+1, 0)
    if list[iterations][comparisons] > list[iterations+1][comparisons]:
        list[iterations][comparisons], list[iterations+1][comparisons] = list[iterations + 1][comparisons], list[iterations][comparisons]
    if list[iterations-1][comparisons] > list[iterations][comparisons]:
        list[iterations-1][comparisons], list[iterations][comparisons] = list[iterations][comparisons], list[iterations-1][comparisons]
    return recursive_bubble_v3(list, iterations, comparisons + 1)
ul3 = [[99, 2, -1], [2, 15, -2], [1, 5, -7]]
print(recursive_bubble_v3(ul3, 0, 0))

#2.-Programar la función recursiva de la burbuja pero sólo aplicada a los elementos de la diagonal ( i==j, es decir, son (0,0) (1,1)...(n,n))
"""
[ [99 , 2 , -1 ],
  [2 , 15, -2],
  [1, 5 , -7]   ]
SOL:
[ [-7 , 2 , -1 ],
  [2 , 15, -2],
  [1, 5 , 99]   ]
"""
def recursive_bubble_v4(list, iterations, comparisons):
    if iterations > len(list)-2:
        return list
    if comparisons > len(list[iterations]) - 1:
        return recursive_bubble_v4(list, iterations + 1, 0)
    if comparisons < len(list[iterations])-1 and iterations < len(list)-1:
        if list[iterations][comparisons] > list[iterations+1][comparisons+1]:
            list[iterations][comparisons], list[iterations+1][comparisons+1] = list[iterations + 1][comparisons + 1], list[iterations][comparisons]
    if comparisons > 0 and iterations > 0:
        if list[iterations - 1][comparisons - 1] > list[iterations][comparisons]:
            list[iterations - 1][comparisons - 1], list[iterations][comparisons] = list[iterations][comparisons], list[iterations - 1][comparisons - 1]
    return recursive_bubble_v4(list, iterations, comparisons + 1)

ul4 = [[99, 2, -1], [2, 15, -2], [1, 5, -7]]
print(recursive_bubble_v4(ul4, 0, 0))
