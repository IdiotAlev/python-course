#Una funcion en blanco que usa la funcion pass
def funcionEnBlanco():
    pass #ignora la funcion

funcionEnBlanco(); #Llamada a la funcion

#Funcion sin argumento
def saludar():
    print("Hola")

saludar() #Llamada a la funcion

#Funcion con argumento
def saludar(nombre):
    print("Hola", nombre)

saludar("tati") #Llamada a la funcion enviando un argumento

#Funcion con varios argumentos
def sacarMedia(grade1, grade2, grade3):
    plus = grade1+grade3+grade2  
    result = plus/3
    return result 

media = sacarMedia(1000, 151, 232)
print("Resultado de la funcion media",media)

#Misma funcion optimizado 
def sacarMedia(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3)/3 

media = sacarMedia(1000, 151, 232)
print("Resultado de la funcion media optimizada",media)
'''
*Nota*
Return permite regresar el valor procesado en la funcion, si no se utilaza
la funcion retornara un none como valor
La funcion return es acompañada de un valor, puede ser una variable 
o una expresion
'''

#Funcion resta dependiendo de la posicion (sin usar keyWords Arguments)
def resta(num1,num2):
    return num1 - num2

print(resta(10,9))
print(resta(9,10))

#Funcion resta sin depender de la posicion (Usando keyWords Arguments)
def resta(num1,num2):
    return num1 - num2

print(resta(num2 =10, num1 =9)) #Se usan las keyWords en la llamada
print(resta(num2=9,num1 =10))


#Funcion con valores predeterminados
def resta(num1=10,num2=9):
    return num1 - num2

print(resta())

#Scope
'''
Se refiere a alcance que tienen las variables. Locales(dentro de funciones)
o globales (en el programa entero)
'''
#Funcion usando variables locales
def imprimirCero():
    variable =0
    print(variable)

imprimirCero()

#Funcion global
'''
Permite usar una variable global de manera local en una funcion.
Se puede usar para no tener que crear una nueva variable dentro de una funcion
'''
sis =18
def imprimirCero():
    global sis
    print(sis)

imprimirCero()

