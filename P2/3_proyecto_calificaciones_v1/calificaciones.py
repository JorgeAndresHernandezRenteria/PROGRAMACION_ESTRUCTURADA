"""
lista=[
        ["Ruben",10.0,8.9,9.2],
        ["Andrés",10.0,10.0,10.0],
        ["María",10.0,10.0,10.0]
      ] 
"""
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def menu_principal(): 
    print("\n\t\t..::: Sistema de Gestión de Calificaciones. :::..\n\n\t\t1.- Agregar\n\t\t2.- Mostrar\n\t\t3.- Cálcular Promedios\n\t\t4.- SALIR")
    opcion = input("\n\t\t Elige una opción (1-4): ")
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print("\n\t\t..::: Agregar Calificaciones :::..\n") 
    nombre=input("Nombre del Alumno: ").upper().strip()
    calificaciones=[]
    for i in range (1,4):
     bandera=True
     while bandera:
         try:
          cal=float(input(f"Calificación {i}: "))
          if cal >=0 and cal <=10:
           calificaciones.append(cal)
           bandera=False
          else:
           print("Ingrese un valor comprendido entre el 0 y el 10")
         except ValueError:
          print("Ingrese un valor númerico")
    lista.append([nombre] + calificaciones)
    print("Acción realizada con éxito")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\n\t\t..::: Mostrar Calificaciones :::..\n") 
    if len(lista)>0:
     print(f"{"Nombre":<15}{"Calific.1":<10}{"Calific.2":<10}{"Calific.3":<10}")
     print("-"*50)
     for fila in lista:
        print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
     print("-"*50)
     print(f"Son {len(lista)} alumnos")
    else: 
       print("No hay calificaiones en el Sistema")

def calcular_promedios(lista):
    borrarPantalla()
    print("\n\t\t..:::Promedios de Alumnos:::..\n") 
    if len(lista)>0:
     print(f"{"Nombre":<15}{"Promedio":<10}")
     print("-"*30)
     promedio_general=0
     for fila in lista:
        nombre=fila[0]
        promedio=(fila[1]+fila[2]+fila[3])/3
        print(f"{nombre:<15}{promedio:.2f}")
        promedio_general+=promedio
        print("-"*30)
     print(f"El promedio general del grupo es: {(promedio_general/3):.2}")
        
     print(f"Son {len(lista)} alumnos")
    else: 
       print("No hay calificaciones en el Sistema")