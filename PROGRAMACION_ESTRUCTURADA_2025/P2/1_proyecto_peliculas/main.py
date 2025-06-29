"""
Proyecto 1.
Crear un proyecto que permita gestionar (administrar) películas; colocar un menú de opciones para agregar,
eliminar, modificar, consultar, buscar y vaciar películas.
-Notas: 1.-Utilizar funciones y mandar llamar desde otro archivo.
        2.-Utilizar listas para almacenar los nombres de las películas."""

import peliculas
opcion=True
while opcion:
 print ("\n\t\t\t.::Renta de películas CINEPOLIS CLON::.\t\t\n\n1.-Agregar películas\t\t\n2.-Eliminar películas\t\t\n3.-Modificar películas\t\t\n4.-Consultar películas\t\t\n5.-Buscar películas\t\t\n6.-Vaciar películas\t\t\n7.-SALIR" )
 opcion=input("\t Elige una opción: ").upper()

 match opcion:#Match: Cadena y enteros (Solo acepta esos dos)
        case "1":
            peliculas.agregarPeliculas()
           #peliculas.esperarTecla()1
        case "2":
            peliculas.eliminarPeliculas()
            peliculas.esperarTecla() 
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()  
        case "4":
            peliculas.consultarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False 
            peliculas.borrarPantalla()   
            print("\n\t\tTerminaste la ejecucion del SW")
        case _:#significa que cualquier opcion invalida va a caer aqui 
            opcion=True
            input("\n\t\tOpción invalida vuelva a intentarlo ... por favor")