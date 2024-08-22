#diccionarios
"""
{}
*desordenados
*tienen 2 elementos x posiscion (clave y valor) no pueden haber claves duplicadas
"""
#sintaxis y llenado de un diccionario
dicA = {"rojo":"red","azul":"blue","amarillo":"yellow"}

#imprimir diccionario
print(dicA)

#imprimir un valor del usando la clave
print(dicA["rojo"])
print(dicA["amarillo"])
print(dicA["azul"])

#añadir un elemento al diccionario 
dicA["marron"]="brown"
print(dicA)

"""funciones diccionario"""
#del() -> elimina  un elemento completo del diccionario usando la clave
del(dicA["marron"])
print(dicA)

#len() -> cuenta 

"""metodos diccionario"""
#.get -> busca un valor a partir de la clave, si no lo encuentra muestra el mensaje
print(dicA.get("morado", "no existe ese color en el diccionario"))

#.keys() -> muestra todas las claves del diccionario 
print(dicA.keys())

#.values -> muestra todos los valores del diccionario
print(dicA.values())

#.clear -> vacia el diccionario
dicA.clear()
print(dicA)

"""condicionales"""
#in -> retorna true o false si el diccionario contiene la clave en el diccionario
