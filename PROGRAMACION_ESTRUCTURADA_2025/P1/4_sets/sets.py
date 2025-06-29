"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.

import os
os.system("cls")

paises=["México","Brasil","España","Canada","Canada"]#Lista (Puede haber valors duplicados).
print (paises)
paises={"México","Brasil","España","Canada","Canada"}#Set-Conjunto (No puede haber valors duplicados).
print (paises)
varios={True,"Cadena",23,3.1416}
print (varios)

paises.add("Mexico")
print(paises)

varios.pop()#Subprograma del tipo 2 (no recibe y regresa)
print(varios)

varios.remove("Cadena")#Subprograma 3 (recibe y ni da)
print(varios)"""

#TAREA
"""
Ejemplo: Crear un programa que solicite los email de los aljumnos de la UTD. 
Almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados."""

emails=[]
resp="si"

while resp=="si":
    emails.append(input("Escribe un email: "))
    resp=input("¿Deseas agregar otro email?").lower()

emails_set=set(emails)
emails=list(emails_set)
print(emails)