"""listas"""
'''
[]
Ordenadas (La posicion importa)
Heterogeneas (Puede almacenar distintos tipos de datos)
Mutables(Agregar, borrar, modificar

*Las listas empiezan desde 0 hasta n numeros
*Una lista puede incluir otra lista
'''

#sintaxis de una lista
#Esta lista tiene 4 elementos incluyendo el 0
listaX = [True, 18, 34.9, False, "Si"]

#consultar posicion de la lista
print(listaX[4])

#consultar una lista desde la ultima posicion
print(listaX[-5])

#obteniendo una sublista
#Desde la posicion 1 hasta n+1
print(listaX[1:3])

#obteniendo una sublista
#Desde el inicio de la lista hasta n+1
print(listaX[:3])

#obteniendo una sublista
#Desde la posicion 1 hasta el final de la lista
print(listaX[1:])

#modificar lista
listaX[4]= "no"
print(listaX[4]) 

"""Metodos de una lista"""
#len(lista) -> devuelve el numero de elementos que hay en una lista
print(len(listaX))

#.insert(indice, value) -> permite agregar un elemento a la lista en el indice pasado por parametro
listaX.insert(1,8)

#.extend([]) -> permite concatenar una lista a otra(parecido a sumar listas)
listaX.extend([10,10,10,10,10])

#condicional "in" permite sbae rsi un elemento esta en la lista
print((8 in listaX) ,"hola")

#.append -> añade un nuevo elemento al final de la lista
print(listaX)
listaX.append("Por que?")
print(listaX)

#.count -> devuelve el numero de veces que se repite un elemento
print(listaX.count(18))

#.index -> devuelve la posicion del elemento pasado como parametro
print(listaX.index("no"))

#.remove -> elimina la primera posicion del elemento pasado por parametro
print(listaX)
listaX.remove(34.9)
print(listaX)

#.pop()-> elimina el elemento pasado por parametro (si el parametro esta vacio elimina la ultima posicion de la lista)
listaX.pop(2)

#.clear() -> elimina todos los elementos de la lista
print(listaX.clear(), "se borro todo")  

#.reverse() -> voltea todos los elementos de una lista
print(listaX.reverse())

#.sort()ordenar una lista(de menor a mayor)
listaX.sort()

#.sort(reverse=true) -> ordena la lista de mayor a menor
listaX.sort(reverse=True)