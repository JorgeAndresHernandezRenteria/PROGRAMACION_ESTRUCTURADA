"""
List (Array)
son colecciones o conjunto de datos/valores bajo un mismo nombre,
para acceder a los valores se hace con un indíce númerico.
Nota: sus valores si son modificables
La lista es una colección ordenada y 
modificable. Permite miembros duplicados.

"""
#Hernández Rentería Jorge Andrés 3°C Clásica.
import os
os.system("cls")

#Funciones más comunes en las listas

paises=["Mexico","Brasil","España","Canada"]
numeros=[23,45,8,24,23,56]
varios=["hola",3.1416,33,True]

#Imprimir el contenido de una lista
print (paises)
print (numeros)
print (varios)

#Recorrer una lista e imprimir el contenido
#1er forma:
for i in paises:
    print (i)

lista='['
for i in paises:
    lista=lista+f"[{i}]" #ó  lista+=f"{i},"
print (lista+"]")

#2da forma:
for i in range(0,4):
    print (paises[i])

    lista='['
for i in range (paises):
    lista=lista+f"[{i}]" #ó  lista+=f"{i},"
print (lista+"]")

#Dar la vuelta a las listas
varios.reverse()
print(varios)
paises.reverse
print (paises)
numeros.reverse
print (numeros)

#Buscar un elemento dentro de una lista
print ("España" in paises )

#Insertar, añadir, agregar un elemento a una lista
os.system("cls")
print(paises)

#1er forma:
paises.append("México")
print(paises)

#2da forma:
paises.insert(1,"México")
print(paises)

#Borrar, eliminar, quitar, suprimir un elemento de la lista
paises.append("México")
print(paises)

#1er forma:
paises.pop(0)
print(paises)

#2da forma:
paises.remove("México")
print(paises)

paises.sort()

#Obtener el indíce o la posición en la cuál se encuentra un elemento
os.system("cls")
print(paises)

paises.index("Canada") #index es un subprograma 

posicion=paises.index("Canada")
print(posicion)
 
#Contar el número de veces que un elemento se encuentra en una lista
os.system("cls")
print(paises)

cuantas=numeros.count(45)#Subprograma que manda o recibe un parametro y regresa un valor de tipo entero
print(cuantas)

cuantas=numeros.count(23)
print(cuantas)

cuantas=numeros.count(233)
print(cuantas)

#Unir el contenido de una lista en otra
os.system("cls")
print(numeros)

numeros2=[100,200]
print(numeros2)

#Crear un programa que una las listas número 1 y 2 e imprima el contenido de la lista resultante en forma descendente

numeros.extend(numeros2)
print(numeros)

numeros.sort()
numeros.reverse()
print (numeros)