peliculas=[]

def borrarPantalla():
 import os
 os.system("cls")

def esperarTecla():
 input("\n\tOprima cualquier tecla para continuar... ")
   
def agregarPeliculas():
 borrarPantalla()
 print("\n\t\t.::Agregar Películas::.")
 peliculas.append(input("Ingresa el nombre: ").upper().strip())#Strip es una función de manejo de cadenas que quita espacios al inicio y al final.
 print("\n\t:::¡LA OPERACIÓN SE REALIZÓ CON EXÍTO!:::")  

def consultarPeliculas():
 borrarPantalla()
 print("\n\t\t.::Consultar o mostrar todas las películas::.")
 if len(peliculas)>0:
  for i in range (0,len(peliculas)):
   print(f"\n\t\t{i+1}:{peliculas[i]}")
 else:
   print(".::No hay películas en el sistema::.")
   
def vaciarPeliculas():
 borrarPantalla()
 print("\n\t\t.::Limpiar o borrar TODAS las películas::.")
 resp=input("¿Deseas borrar todas las películas? (Si/No): ").lower()
 if resp=="si":
  peliculas.clear()
  print("\n\t:::¡LA OPERACIÓN SE REALIZÓ CON EXÍTO!:::") 

def buscarPeliculas():
 borrarPantalla()
 print("\n\t\t.::Buscar una Película::.\n")
 pelicula_buscar=input("Ingresa el nombre de la película a buscar: ").upper().strip()
 if not (pelicula_buscar in peliculas):
  print("\n\t.::No hay ninguna película con este nombre::.")
 else:
  encontro=0
  for i in range (0,len(peliculas)):
   if pelicula_buscar==peliculas[i]:
    print(f"\n\tLa película {pelicula_buscar} si la tenemos y esta en el casillero: {i+1}")
    encontro+=1
  print(f"\t\nTenemos {encontro} película(s) con este título")

def modificarPeliculas():
 borrarPantalla()
 print("\n\t\t.::Modificar una Película::.\n")
 pelicula_buscar=input("Ingresa el nombre de la película a buscar: ").upper().strip()
 if not (pelicula_buscar in peliculas):
  print("\n\t.::No hay ninguna película con este nombre::.")
 else:
  encontro=0
  for i in range (0,len(peliculas)):
   if pelicula_buscar==peliculas[i]:
    resp=input("¿Deseas modificar la película? (Si/No) ").lower().strip()
    if resp=="si":
     peliculas[i]=input("\n\tIntroduzca o tecle el nuevo valor de la película: ").upper().strip()
     print(f"\n\tLa película ahora se llama{peliculas[i]} y la tenemos en el casillero: {i+1}")
     encontro+=1
  print(f"\t\nSe actualizaron {encontro} película(s) con este título")

def eliminarPeliculas():
 borrarPantalla()
 print("\n\t\t.::Borrar Películas::.\n")
 pelicula_buscar=input("Ingresa el nombre de la película a buscar: ").upper().strip()
 encontro=0
 if not (pelicula_buscar in peliculas):
  print("\n\t\t ¡No se encuentra la pelicula a buscar!")
 else:
  resp="si"
  while pelicula_buscar in peliculas and resp=="si":
      resp=input("¿Deseas quitar o borrar la pelicula del sistema (Si/No) ?").lower
      if resp=="si":
       posicion=peliculas.index(pelicula_buscar)
       print(f"\nLa pelicula que se borro es: {pelicula_buscar} y estaba en la casilla: {posicion+1}")
       peliculas.remove(pelicula_buscar)
       encontro+=1
       print("\n\t\t:::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!:::")
 # print(f"Se borró {encontro} pelicula(s) con este título") 

"""def buscarPeliculas():

 borrarPantalla
 print("\n\t\t.::Buscar películas::.")
 peli=(input("¿Cuál película estás buscando?").upper().strip())
 print(peli in peliculas)

 peliculas.reverse()
 posicion=peliculas.index(peli) 
 for i in range (0,len(peliculas)):
  print(f"\n\t\t{i+1}:{peliculas[i]}")
 print(f"El valor de {peli} lo encontro en la posicion: {i}")"""