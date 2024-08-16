"Hacer un programa que pida 3 numeros e identifique cual es el mayor"
num1= float(input("Num1"))
num2= float(input("Num2"))
num3= float(input("Num3"))

if(num1 >= num2) & (num1 >= num3):
    print(f"mayor es {num1}")
elif (num2 >= num1) & (num2 >= num3):
    print(f"mayor es {num2}")
elif (num3 >= num1) & (num3 >= num2):
    print(f"mayor es {num3}")
