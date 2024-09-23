#presentar la tabla de multiplicar de un numero ingresador por el usuario

num=int(input("ingrese numero"))

print(f"La tabla del {num} es: ")
for i in range(11):
    print(i*num)

