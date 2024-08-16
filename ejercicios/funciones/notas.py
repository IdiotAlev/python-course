'''
En este ejercicio se aplicaron los temas vistos
en la clase 1. Funciones, variables, operadores
'''
def mediaNotas(g1, g2, g3):
    media = (g1 + g2 +g3)/3
    return media


#Ingreso de notas
grade_1 = 3.2
grade_2 = 3.0
grade_3 = 3.0
media = mediaNotas(grade_1, grade_2, grade_3)
print("Fue mediocre?", media >= 3 and media <=3.2)