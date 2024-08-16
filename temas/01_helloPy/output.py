#salida de datos
nombre ="fabian"
edad = 21

#convencional
saludo = "hola",nombre, "tienes", edad
print(saludo)

#format
saludo = "hola {} tines {} de edad".format(nombre,edad)
print(saludo)

#version 3.6
saludo = (f"hola {nombre}, como estas. se que tienes {edad} anos de edad")
print(saludo)

