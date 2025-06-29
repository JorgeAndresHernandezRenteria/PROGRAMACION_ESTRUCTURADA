#Proyecto 3
#Crear un proyecto que permita gestionar (administrar) calificaciones, colocar un menú de opciones para agregar, mostrar y calcular el promedio de calificaciones.
# Notas:
# 1.- Utilizar funciones y mandar a llamar desde otro archivo.
# 2.- Utilizar listas para almacenar el nombre y 3 calificaciones de los alumnos


import calificaciones

def main():
    opcion = True
    datos=[]

    while opcion:
     calificaciones.borrarPantalla()
     opcion=calificaciones.menu_principal()#Aquí ya estamos usando una función (opcion)
     
     match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                opcion=False
                calificaciones.borrarPantalla()
                print("Terminaste la ejecución del SW")
            case _:
                opcion=True
                print("Opción inválida, vuelva a intentarlo")
                calificaciones.esperarTecla()

if __name__=="__main__":   
    main()     