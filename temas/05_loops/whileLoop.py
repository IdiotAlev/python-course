#WhileLoop
"""
Bucle con numero indeterminado de interaciones
Necesita que se cumpla un condicion para que el loop se siga ejecutando n veces
"""

#Ejemplo 1

#Sacar raiz cuadrada de un numero
#condicion -> tiene que ser psotivo en numero

num =int(input("dijite numero"))

while num<0 : #condicion
  print("El numero no puede ser negatvio")
  num =int(input("dijite numero"))
  
import math
print(f"La raiz es: {(math.sqrt(num)):.2f}") #:.2f -> indica el numero de decimales

#ejemplo 2

#Repetir un mensaje n numero de veces
#usar variable iteradora(contador) para evaluar la condicion(se modifica dentro del mismo ciclo)

cont=0
while cont<10:
    print("Hola")
    cont+=1

cont=0
#ejercicio 3
#Imprimir los numeros del 1 al 10
#usar variable iteradora para imprimir los numeros

while cont<10:
    print(cont)
    cont+=1

