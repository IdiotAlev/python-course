#tuplas
'''
()
Ordenas(La posicion no importa)
Heterogeneas (Puede almacenar distintos tipos de datos)
NO SE MODIFICAN
'''

tuplaX =("yo",10,2.4,10,True)

#consultar tupla
print(tuplaX)

#Consultar una tupla en un indice
print(tuplaX[2])

#consultar si un elemento esta en la tupla
print(4 in tuplaX)}

#consultar desde el principio de la tupla hasta el final(slidesing)
print(tuplaX[:4])

#consultar desde el final hasta el rpincipio(slidesings)
print(tuplaX[4:])

#Metodos tuplas
# count -> cuenta las veces que aparece el valor pasado por parametro en la tupla
print(tuplaX.count(10))

#index -> #buscar en la tupla el indice del valor pasado por paraelve la primera posicion q encuentre)
print(tuplaX.index(2.4))

#len(tupla) -> tamaño de la tupla pasada por parametro
print(len(tupla))

# list(tupla) -> transformar una tupla a una lista(hace una copia, no la modifica
lista = list(tuplaX)

#tuple(list)-> transforma una lista en una tupla (hace una copia no, la modifica)
listY = [1,2,3]
tupla= tuple(listY)