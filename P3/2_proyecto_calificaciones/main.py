"""
Proyecto calificaciones.
*Crear un proyecto que permita Gestionar (Administrar) las calificaciones de un alumno, colocar un menu de opciones para agregar, mostrar, buscar y calcular promedios de calificaciones..
"""
import calificaciones

def main():
    opcion = True
    datos=[]

    while opcion:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()
        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios()
                calificaciones.esperarTecla()
            case "4":
                opcion = False
                calificaciones.borrarPantalla()
                print("\n\tTerminaste la ejecucion del SW")
            case "5":
                calificaciones.buscar(datos)
                calificaciones.esperarTecla
            case _:
                opcion = True
                input("\n\tOpción inválida, vuelva a intentarlo.... por favor")
                
if __name__ == "__main__":
    main ()