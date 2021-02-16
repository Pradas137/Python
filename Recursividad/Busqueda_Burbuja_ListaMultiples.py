def metodo_Burbuja_recurivo(array, pasos, comparaciones):
  if len(array)-1 < pasos:
      #print(len(array)-1,"-", pasos)
      return array
  else:
    if len(array[pasos])-2 < comparaciones :
        #print(len(array[pasos])-2,"-", comparaciones)
        return metodo_Burbuja_recurivo(array, pasos + 1, 0)
    elif array[pasos][comparaciones] > array[pasos][comparaciones - 1]:
        #print(array[pasos][comparaciones],"-",array[pasos][comparaciones + 1])
        array[pasos][comparaciones], array[pasos][comparaciones + 1] = array[pasos][comparaciones + 1], array[pasos][comparaciones]
        #print(array[pasos][comparaciones],"-", array[pasos][comparaciones + 1])
    return metodo_Burbuja_recurivo(array, pasos, comparaciones + 1)

lst = [[3,1,2],[8,4,5],[9,-1,2],[9,-1,2]]
print(metodo_Burbuja_recurivo(lst,0,0))
