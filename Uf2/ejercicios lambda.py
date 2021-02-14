lista=[-1,2,3,4,5,6,-7,8,-9,10,11]
listanegativos=filter(lambda x:x<0,lista)
print(list(listanegativos))

lst = [('caramelos','30','100'), ('manzanas','10','200'), ('peras','20','300')]
lst.sort(key=lambda x:x[1])
print(lst)




# def funcion(x):
#     return x<0
# listanegativos=filter(funcion,lista)
#
#
# creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
# print(list(filter(lambda x: x[0].lower() in 'aeiou', creature_names)))