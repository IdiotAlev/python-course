#condicional anidado
edad = int(input("dijite edad"))

if edad>0 & edad<100:
    if edad >= 18:
     print("mayor de edad")
    else:
        print("Menor de edad")
else: 
    print("edad no valida")