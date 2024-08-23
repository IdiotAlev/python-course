"""
Escriba un programa que tenga dos listas y que, a continuacion,
cree las siguientes listas(en la q no debe haber repeticiones)

>lista de elementos que aparecen en las 2 listas
>lista de elementos que aparecen en la primera lista, pero no en la segunda
>lista de elementos que aparecen en la segunda lista, pero no el la primera
>lista de elementos que aparecen en ambas listas
"""

listA=[12,43,43,2.3,2.23,5.12,"yo",12.5,"yo","tu","el",-8,-21.5]
print(listA.count(43))
listB=["el", 12,12,"ella" ,5.12,"ella","43",43,80.21,"si","yo"]

listA=list(set(listA))
print(listA.count(43))
listB=list(set(listB))

print(listA,listB)