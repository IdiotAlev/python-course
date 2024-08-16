#conjuntos
'''
conjunto = set()
conjunto = {}
*No ordenados
*Heterogeneos(solo con elemntos inmutables)
*mutables
*sin repeticion
*un conjunto no puede tener otro tipo de colecciones (listas, tuplas    )
***Uso comunes***
>Introducir un string en un conjunto lo tomara como una cadena de chart
>Elimina elementos repetidos en un conjunto [solo guarda una vez en valor en el conjunto]
'''
#seteando una lista al conjunto x
conjuntoX = set([1,2,3,4])
print(conjuntoX)

#setenado una tupla a un conjunto y
conjuntoY = set((True, 18,19,False, 12.8))
print(conjuntoY)

#setenado un string al conjunto z
conjuntoZ = set(("Hola, si probadno 1,2,3"))
print(conjuntoZ)

#setenanod mas de un elemento igual en el conjunto q
conjuntoQ = set([21,19,27,True,18, 19])
print(conjuntoQ)

"""metodos de conjuntos"""

#.add
conjuntoX.add(5)

#.remove
conjuntoX.remove(4)

#.discard -> elimina el elemneto pasado x parametro
conjuntoX.discard(5)

#.clear() -> elimina todo el contenido del conjunto
conjuntoX.clear()

#in
print(3 in conjuntoX)

#len(conjunto) -> cantidad de elementos que alamacena
print(len(conjuntoX))

# a == b -> igualdad de conjuntos(pregunta si los conjuntos son iguales true o false)
print(conjuntoQ == conjuntoZ)

#hacer un conjunto inmutable (tiene que ser al momento de declararlo)
conjuntoAutos = frozenset({"MacLaren", "honda", "chevrolet"})
#conjuntoAutos.add("audi")

"""operaciones de conjuntos """

#.intersection o & (interseccion)-> devuelve los elementos que aparecen en ambos conjuntos (que los relacionan)
print(conjuntoQ.intersection(conjuntoX))#1(true y 1)
print(conjuntoQ.intersection(conjuntoZ))#0
print(conjuntoQ & conjuntoY)

#.union() o | (union) -> une todos los elementos de ambos conjuntos en un subconjunto
print(conjuntoX.union(conjuntoY))
conjuntoJ=conjuntoX | conjuntoY
print(conjuntoJ)

#.difference o - (diferencia) ->  son el conjunto de elementos que estén en A y no esten B
print(conjuntoX - conjuntoY)
conjuntoK = conjuntoX.difference(conjuntoY)
print(conjuntoK)

#.symmetric_difference o ^ (diferencia simetrica) -> conjunto de elementos que solo pertenecen a ‍ o a ‍ pero no a ambos a la vez
print(conjuntoX ^ conjuntoY)
print(conjuntoY ^ conjuntoX)
conjuntoK = conjuntoX.symmetric_difference(conjuntoY)
print(conjuntoK)

#.issubset ()->  comprueba si los elementos de un conjunto estan incluidos en otro (si es un subconjunto. True o false)
print(conjuntoQ.issubset(conjuntoX))
print(conjuntoQ.issubset(conjuntoY))
print(conjuntoQ.issubset(conjuntoZ))

#.issuperset() -> comprueba si el conjutno contiene los elementos de otros conjuntos(si es un superconjunto. True o false)

#.disjoning() -> comprueba si no tienen un elemento en comun (disconecto)
print(conjuntoZ.isdisjoint(conjuntoQ))


