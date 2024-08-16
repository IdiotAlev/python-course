"""
Desarrollar un programa que simule el funcionamiento de
 una calculadora que pueda realizar las cuatro operaciones aritmeticas basicas (suma , resta,
 multiplicacion y division). El usuario debe especificar la operacion con el primer caracter del
 nombre de la operacion.
 
 S,s -> suma
 R,r -> resta
 P, p, M, m -> multiplicacion
 D,d -> division
 """

num1= float(input("num1"))
num2= float(input("num2"))
op= str(input("Operacion a realizar")).lower()
if op == "s" :
    print(num1+num2)
elif op == "r":
    print(num1-num2)
elif (op == "m") or (op=="p"):
    print(num1*num2)
elif (op == "d"):
    print(num1/num2)
else:
    print("ingrese una operacion valida")