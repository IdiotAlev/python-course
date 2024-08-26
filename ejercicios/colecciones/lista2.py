"""
Escriba un programa que tenga dos listas y que, a continuacion,
cree las siguientes listas(en la q no debe haber repeticiones)

>lista de elementos que aparecen en las 2 listas *
>lista de elementos que aparecen en la primera lista, pero no en la segunda * 
>lista de elementos que aparecen en la segunda lista, pero no el la primera *
>lista de elementos que aparecen en ambas listas
"""
#creacion de listas
listA=[12,43,43,2.3,2.23,5.12,"yo",12.5,"yo","tu","el",-8,-21.5]
listB=["el", 12,12,"ella" ,5.12,"ella","43",43,80.21,"si","yo"]

#listas a conjuntos
conjA=set(listA)
conjB=set(listB)

#operacion intesection
shw=list(conjA & conjB)
print(f"Lista de elementos en ambas listas:\n{shw}")

#operacion difference
shw=list(conjA - conjB)
print(f"Lista de elementos que estan en la primera,lista pero no en la segunda:\n{shw}")

#"" "" ""
shw=list(conjB - conjA)
print(f"Lista de elementos que estan en la segunda lista, pero no en la primera:\n{shw}")

#operacion union
shw=(conjA | conjB)
print(f"Lista de elementos de ambas listas:\n{shw}")

"""
convierto las listas en un conjunto que vuelvo a convertir en lista(para eliminar los elemntos repetdidos)
listA=list(set(listA))
listB=list(set(listB))
print(listA,listB)
"""
