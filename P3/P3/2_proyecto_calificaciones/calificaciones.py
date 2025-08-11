import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def conectar():
  try:
    conexion=mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="",
      database="bd_calificaciones"
    )
    return conexion
  except Error as e:
    print(f"El error que se presento es: {e}")
    return None

def menu_principal(): 
    print("\n\t\t..::: Sistema de Gestión de Calificaciones. :::..\n\n\t\t1.- Agregar\n\t\t2.- Mostrar\n\t\t3.- Cálcular Promedios\n\t\t4.- SALIR")
    opcion = input("\n\t\t Elige una opción (1-4): ")
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    conexionBd = conectar()
    if conexionBd != None: 
        print(".:: Agregar Calificaciones ::.")
        nombre=input("Nombre del Alumno: ").upper().strip()
        calificaciones=[]
        for i in range(1,4):
            bandera=True
            while bandera:
                try:
                    cal=float(input(f"Calificación {i}:"))
                    if cal >= 0 and cal<=10:
                        calificaciones.append(cal)
                        bandera=False
                    else:
                        input("Ingrese un valor comprendido entre el 0 y el 10: ")
                        esperarTecla()
                except ValueError:
                    input("Ingrese el valor numerico")
                    esperarTecla()
        cursor = conexionBd.cursor()
        sql = ("insert into calificaciones_nombre (nombre_alumno, parcial1, parcial2, parcial3) values (%s, %s, %s, %s);")
        py = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])
        cursor.execute(sql, py)
        conexionBd.commit()
        print("Acción realizada con exito ")

def mostrar_calificaciones(lista):
    borrarPantalla()
    conexionBd = conectar()
    print("\n\t\t..::: Mostrar Calificaciones :::..\n") 

    if conexionBd != None:
     print(f"{'Nombre':<15}{'Calific.1':<10}{'Calific.2':<10}{'Calific.3':<10}{'Id':<10}")
     print("-"*50)
     cursor = conexionBd.cursor()
     cursor.execute("select * from calificaciones_nombre")
     regitros = cursor.fetchall()
     if regitros != None:
        for fila in regitros:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            print("-"*50)   
     else: 
       print("No hay calificaciones en el Sistema")
    else:
        print("La base de datos no se encuentra disponible por el momento, porfavor intentelo mas tarde")

def calcular_promedios():
    borrarPantalla()
    conexionBd = conectar()
    if conexionBd is not None:
        print(".:: Promedios Alumnos ::.\n")
        cursor = conexionBd.cursor()
        cursor.execute("SELECT nombre_alumno, parcial1, parcial2, parcial3 FROM calificaciones_nombre")
        registros = cursor.fetchall()

        if registros:
            print(f"{'Nombre':<20}{'Promedio':<10}")
            print("-" * 30)
            suma_general = 0
            for fila in registros:
                nombre = fila[0]
                promedio = (fila[1] + fila[2] + fila[3]) / 3
                suma_general += promedio
                print(f"{nombre:<20}{promedio:<10.2f}")
            promedio_general = suma_general / len(registros)
            print("-" * 30)
            print(f"{'Promedio general':<20}{promedio_general:<10.2f}")
        else:
            print("No hay calificaciones registradas.")
    else:
        print("No se pudo conectar a la base de datos.")
        
def buscar_alumno():
    borrarPantalla()
    conexionBd = conectar()
    if conexionBd is not None:
        print(":: Buscar Alumno ::\n")
        nombre = input("Ingresa el nombre del alumno a buscar: ").upper().strip()
        cursor = conexionBd.cursor()
        sql = "SELECT nombre_alumno, parcial1, parcial2, parcial3 FROM calificaciones_nombre WHERE nombre_alumno = %s"
        cursor.execute(sql, (nombre,))
        resultado = cursor.fetchone()

        if resultado:
            print(f"\n{'Nombre':<20}{'Calificación 1':<15}{'Calificación 2':<15}{'Calificación 3':<15}")
            print("-" * 65)
            print(f"{resultado[0]:<20}{resultado[1]:<15}{resultado[2]:<15}{resultado[3]:<15}")
        else:
            print("\nNo se encontró ningún alumno con ese nombre.")
    else:
        print("No se pudo conectar a la base de datos.")
    esperarTecla()