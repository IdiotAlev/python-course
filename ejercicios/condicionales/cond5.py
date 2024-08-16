"""
Desarrollar un progrma que simule un cajero automatico con un saldo incial de $1000
y tendra un menu con la sgtes opciones:
1.Ingresar dinero en la cuneta
2.Retirar dinero de la cuenta
3.Mostrar dinero disponible
4.Salir
"""
saldo= 1000

op= int(input("Opcion"))

if op == 1:
    ingreso=float(input("Dinero a ingresar"))
    saldo+= ingreso
    print(f"El nuevo saldo es {saldo}")
elif op == 2:
    retiro=float(input("Dinero a retirar"))
    saldo-=retiro
    print(f"El nuevo saldo es {saldo}")
elif op == 3:
    print(f"El saldo disponible es {saldo}")
else :
    print("Ha salido del prgrama")