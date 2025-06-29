#Hernández Rentería Jorge Andrés 3°C Clásica.
import os
"""TAREA"""
#ejemplo 1 crear una lista de numeros e imprimir el contenido
"""os.system("cls")

numeros=[100,34]
print(numeros)

variable="["
for i in numeros:        #Estamos recorriendo la lista
    variable+=f"{i},"     #Acumulador de cadenas
    print(f"{variable}]")

variable="["
for i in range (0,len(numeros)):        #Estamos recorriendo la lista
    variable+=f"{numeros[i]},"     #Acummulador de cadenas
    print(f"{variable}]")"""

#ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
"""os.system("cls")
palabras=["UTD","2023","logo","TI","2C clasica"] #Lista
palabra_buscar=input("Dame la palabra a buscar en la lista:")
#1er forma:
if palabra_buscar in palabras: #Le estoy pidiendo que busque la palabra en mi lista
    print("Si encontro la palabra en la lista")
else:
    print("No encontro la palabra en la lista")"""

#2da forma:
"""encontro=False
cuantas=0
posiciones=[]
for i in palabras:
    if i==palabra_buscar: #If para ver si lo encuentras
        encontro=True
        cuantas+=1
        posiciones.append(palabras.index(i)) #Para ver en que posición se encuentra/Agregar la posicion encontrada de ese dato en la lista
if encontro: #Fuera del ciclo para ver lo encontró
    print("Si encontro la palabra en la lista")
else:
    print("No encontro la palabra en la lista")
print (posiciones)
"""
"""encontro=False
posiciones=[]
for i in range(0,len(palabras)): #If para ver si lo encuentras
        encontro=True
if encontro: #Fuera del ciclo para ver si lo encontró
    print("Si encontro la palabra en la lista")
else:
    print("No encontro la palabra en la lista")
print (posiciones)
"""
#ejemplo 3 añadir elementos a la lista:
#ejemplo 4 crear una lista multidimensional para almacenar los nombres y telefonos de unos contactos "Agenda":
agenda=[
         ["Carlos","6181234567"],
         ["Carlos V","6181234567"],
         ["Carlos VI","6181234567"],
       ]
print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
       print(agenda[r][c])

lista=""
for r in range(0,3):
    for c in range(0,2):
       lista+=f"{agenda[r][c]},"
    lista+="\n"
print(lista)