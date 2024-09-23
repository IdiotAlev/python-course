#forLoop
"""
>Bucle con un numero determinado de iteraciones
>Usado para colecciones
"""

#ejemplo 1
for i in [1,2,3,4,5]:
    print("hola")

#ejemplo 2    
for i in [10,7,"yo",4,True]:
    print(i)
    
#ejemplo 3 (recorrienod un dicionario)
#obteniendo la clave
dic ={"luis":12,"juan":14,"daniel":21}
for i in dic:
    print(i)
    
#obteniendo el valor
dic ={"luis":12,"juan":14,"daniel":21}
for i in dic:
    print(dic[i])
    
#obteniendo ambos
dic ={"luis":12,"juan":14,"daniel":21}
for i in dic:
    print(f"La clave es {i} y el valor es {dic[i]}")

#modo SENIOR
for i,j in dic.items():
    print(i,j)
    
#recorriendo cadenas de texto
nombre="fabian"

for i in nombre:
    print(i)

for i in "tatis":
    print(i,end=" ")