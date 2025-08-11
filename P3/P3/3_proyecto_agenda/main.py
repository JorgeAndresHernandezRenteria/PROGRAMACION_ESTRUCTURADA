import agenda 

def main():

    conexionBD = agenda.conectar()
    if conexionBD is not None:
        agenda_contactos = {}
        salir = False 
        
        while not salir:  

            agenda.borrarPantalla()
            opcion = agenda.menu_principal() 
            
            if opcion == "1":
                agenda.agregar_contacto(agenda_contactos)

            elif opcion == "2":
                agenda.mostrar_contactos(agenda_contactos)

            elif opcion == "3":
                agenda.buscar_contactos(agenda_contactos)

            elif opcion == "4":
                agenda.modificar_contacto(agenda_contactos)

            elif opcion == "5":
                agenda.eliminar_contacto(agenda_contactos)

            elif opcion == "6":
                print("\n\t🚪 Terminaste la ejecución del SW 🚪")
                agenda.esperarTecla()
                salir = True  
                
            else:
             print("\n\t❌ Opción inválida. Vuelva a intentarlo")
             agenda.esperarTecla()
        
    conexionBD.close() 

if __name__ == "__main__":
    main ()