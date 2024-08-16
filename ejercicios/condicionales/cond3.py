"""
Hacer un progrma que pida 2 numeros y se de cuenta cual de ellos
es par o si ambos los son o si los 2 lo son.
"""

num1 = int(input("ingrese numero 1"))
num1=num1%2
num2 = int(input("ingrese numero 2"))
num2 =num2%2

if (num1==0) & (num2== 0) :
    print("ambos son pares")
elif (num1==0) and (num2 != 0):
    print("primero es par")
elif (num1 !=0) and (num2 == 0):
    print("segundo es par")
else :
    print("ambos osn impares")