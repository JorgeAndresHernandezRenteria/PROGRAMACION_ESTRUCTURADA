agenda_contactos={
                }

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def menu_principal(): 
    print("\n\t\t🗓..::: Sistema de Gestión de Agenda de Contactos :::..🗓\n\n\t\t1.- Agregar contacto\n\t\t2.- Mostrar todos los contactos\n\t\t3.- Buscar contacto por nombre\n\t\t4.- modificar contacto\n\t\t5.- Eliminar contactos\n\t\t6.- SALIR")
    opcion = input("\n\t\t Elige una opción (1-4): ")
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t..::: Agregar contacto :::..\n") 
    nombre=input("Nombre del contacto: ").upper().strip()
    if nombre in agenda:
       print("Ya existe")
    else:
     tel=input("Teléfono del contacto: ").upper().strip()
     email=input("Email del contacto: ").upper().strip()
     agenda[nombre]=[tel,email]
     print("Acción realizada con éxito")

def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t..::: Mostrar Contactos :::..\n") 
    if not agenda:
     print("No hay contactos en la agenda")
    else:
       print(f"{'Nombre':<15}{'Teléfono':<15}{'E-mail':<15}")
       print(f"-"*60)
       for nombre,datos in agenda.items():          #Nota: En i va a guardar los nombres de los atributos (En este caso los nombres)
          print(f"{nombre:<15}{datos[0]:<15}{datos[1]:<15}")
       print(f"-"*60)

def buscar_contacto(agenda):
   borrarPantalla()
   print("\n\t\t..::: Buscar Contacto :::..\n") 
   if not agenda:
      print("No hay contactos")
   else:
     nombre=input("Nombre del contacto a buscar: ").upper().strip()
     if nombre in agenda:
      print(f"{'Nombre':<15}{'Teléfono':<15}{'E-mail':<15}")
      print(f"-"*60)
    #Aquí hace referencia a la agenda, pero la doble llave es para buscar especificamene el valor que quiero.
      print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
      print(f"-"*60)
     else:
        print("No existe el contacto")

def modificar_contacto(agenda):
    borrarPantalla()
    print("Modificar Contactos")
    if not agenda:
        print("No hay contactos en la Agenda")
    else:
        nombre=input("Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
           print("Valores Actuales")
           print(f"Nombre: {nombre}\nTeléfono: {agenda[nombre][0]}\nE-mail: {agenda[nombre][1]}")
           resp=input("¿Deseas cambiar los valores? (Si/No)").lower().strip()
           if resp=="si":
              tel=input("Teléfono: ").upper().strip()
              email=input("E-mail: ").upper().strip()
              agenda[nombre]=[tel,email]
              print("Acción Realizada con éxito")
        else:
           print("Este contacto no existe")

def eliminar_contacto(agenda):
   borrarPantalla()
   print("Eliminar Contactos")
   if not agenda:
      print("No hay contactos en la Agenda")
   else:
      nombre=input("Nombre del contacto a buscar: ").upper().strip()
      if nombre in agenda:
         print("Valores Actuales")
         print(f"Nombre: {nombre}\nTeléfono: {agenda[nombre][0]}\nE-mail: {agenda[nombre][1]}")
         resp=input("¿Deseas eliminar los valores? (Si/No)").lower().strip()
         if resp=="si":
            agenda.pop(nombre)
            print("Acción Realizada con éxito")
      else:
         print("Este contacto no existe")