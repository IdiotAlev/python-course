#Escriba un programa donde cree una lista con los siguientes personajes de el sr de los anillos

"""
1. Nombre -> aragon
   Clase -> guerrero 
   Raza -> Dunan del norte
   
2. Nombre -> Legolas
   Clase -> Arqueri
   Raza -> Elfo Sindar
   
3. Nomrbe -> Gandalf
   Clase -> Mago
   Raza -> Istar 
"""
#Creando lista de personajes
personajesList=[]

#Creando los personajes como diccionarios
per1={"Nombre":"Aragon","Clase":"Guerrero","Raza":"Dunan del Norte"}
per2={"Nombre":"Legolas","Clase":"Arquero","Raza":"Elfo Sindar"}
per3={"Nombre":"Gandalf","Clase":"Mago","Raza":"Istar"}

#agragadon personajes a la lista
personajesList.append(per1)
personajesList.append(per2)
personajesList.append(per3)

#msotrando lista
print(personajesList)



