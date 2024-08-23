"""
escriba un programa donde tenga una lista y que, 
a continuacion, elimine los elementos repetidos, por ultimo imprimir
la lista
"""
lista_A=[1,2,7,6,1,8,8,14,3,4,5,6,7,8]
conjuntoA = set(lista_A)
print(conjuntoA)
listaB=list(conjuntoA)
print(listaB)

"""
forma abreviada
lista=list(set(lista))
"""
