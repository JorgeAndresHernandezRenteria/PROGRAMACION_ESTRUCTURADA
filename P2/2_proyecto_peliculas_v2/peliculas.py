#dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)

pelicula={#sugerencia: Poner el nombre del diccionario en singular
            "nombre":"",
            "categoria":"",
            "clasificacion":"",
            "genero":"",
            "idioma":"",
          }

pelicula={}

def borrarPantalla():
 import os
 os.system("cls")

def esperarTecla():
 input("\n\tOprima cualquier tecla para continuar... ")
   
def crearPeliculas():
 borrarPantalla()
 print("\n\t\t.::Alta de Películas::.\n")
 pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})#Update es para actualizar los atributos del diccionario
 pelicula.update({"categoría":input("Ingresa la categoría: ").upper().strip()})
 pelicula.update({"clasificación":input("Ingresa la clasificación: ").upper().strip()})
 pelicula.update({"género":input("Ingresa el género: ").upper().strip()})
 pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
 print("\n\t\t:::¡LA OPERACIÓN SE REALIZÓ CON EXÍTO!:::")  

def mostrarPeliculas():
  borrarPantalla()
  print("\n\t\t.::Consultar o Mostrar la Película::.\n")
  if len(pelicula)>0:
   for i in pelicula:
    print(f"\t{(i)}:{pelicula[i]}")
  else:
   print("\t.::No hay películas en el sistema::.")

def borrarPeliculas():
  borrarPantalla()
  print("\n\t\t.::Borrar o Quitar TODAS las Película::.\n")
  resp=input("¿Deseas quitar o borrar todas las películas del sistema? (Si/No)")
  if resp=="si":
   pelicula.clear()
   print("\n\t\t:::¡LA OPERACIÓN SE REALIZÓ CON EXÍTO!:::")  
   
def agregarCaracteristicaPeliculas():
 borrarPantalla()
 print("\n\t\t.::Agregar Caracteristíca a Películas::.\n")
 atributo=input("Ingresa la nueva caracteristíca de la película: ").lower().strip()
 valor=input("Ingresa el valor de la caracteristíca de la película: ").upper().strip()
 #pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
 pelicula[atributo]=valor
 print("\n\t\t:::¡LA OPERACIÓN SE REALIZÓ CON EXÍTO!:::")  

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Característica de Películas ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
        atributo = input("\nIngresa el nombre de la característica que deseas modificar: ").lower().strip()
        if atributo in pelicula:
            nuevo_valor = input("Ingresa el nuevo valor: ").upper().strip()
            pelicula[atributo] = nuevo_valor
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        else:
            print("\n\t\t::: La característica no existe :::")
    else:
        print("\t..:: No hay películas en el sistema ::..")

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Característica de Películas ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
        atributo = input("\nIngresa el nombre de la característica que deseas borrar: ").lower().strip()
        if atributo in pelicula:
            del pelicula[atributo]
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        else:
            print("\n\t\t::: La característica no existe :::")
    else:
        print("\t..:: No hay películas en el sistema ::..")