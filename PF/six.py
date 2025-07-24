import os

def borrar_pantalla():
    
    os.system('cls')

def esperar_tecla():
    
    input("\nPresione cualquier tecla para continuar...")

def menu_principal():
    
    borrar_pantalla()
    print("\n" + "=" * 50)
    print(" SISTEMA DE GESTIÓN DE INVENTARIO - NEGOCIO SIX")
    print("=" * 50)
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar stock")
    print("5. Salir")
    return input("\nSeleccione una opción: ")

def agregar_producto(inventario):
    borrar_pantalla()
    print("\n" + "=" * 50)
    print(" AGREGAR NUEVO PRODUCTO")
    print("=" * 50)
    
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    id_producto = input("ID/Código de barras: ")
    stock_critico = int(input("Stock crítico: "))
    stock_actual = int(input("Stock actual: "))
    
    nuevo_producto = [
        id_producto,
        nombre,
        precio,
        stock_critico,
        stock_actual
    ]
    
    inventario.append(nuevo_producto)
    print(f"\n✅ Producto '{nombre}' agregado exitosamente!")

def mostrar_productos(inventario):
    borrar_pantalla()
    print("\n" + "=" * 90)
    print(" INVENTARIO COMPLETO")
    print("=" * 90)
    print(f"{"ID/Código":<10}{"Nombre":<20}{"Precio":<22}{"Stock Crítico":<24}{"Stock Actual":<26}")
    print("-" * 90)
    
    for producto in inventario:
         print(f"{producto[0]:<10}"  # ID (15 caracteres, alineado izquierda)
              f"{producto[1][:18]:<20}"  # Nombre (cortado a 18 chars + 2 espacios)
              f"${producto[2]:<22.2f}"  # Precio (alineado derecha, 2 decimales)
              f"{producto[3]:<24}"  # Stock crítico
              f"{producto[4]:<26}")
        #print(f"{producto[0]:<15}{producto[1][18]:<10}${producto[2]:<10}{producto[3]:<10}{producto[4]:<10}")
    
    print("=" * 90)

def buscar_producto(inventario):
    print("\n" + "=" * 50)
    print(" BUSCAR PRODUCTO")
    print("=" * 50)
    id_buscar = input("Ingrese ID del producto: ")
    for producto in inventario:
        if producto [0] == id_buscar:
         print("\n" + "-" * 50)
         print(" PRODUCTO ENCONTRADO")
         print("-" * 50)
         print(f"ID/Código: {producto[0]}")
         print(f"Nombre: {producto[1]}")
         print(f"Precio: ${producto[2]:.2f}")
         print(f"Stock crítico: {producto[3]}")
         print(f"Stock actual: {producto[4]}")
         return producto  # Retornar el producto encontrado
    else:
      print("\n❌ Producto no encontrado!")

def actualizar_stock(inventario):
    borrar_pantalla()
    print("\n" + "=" * 50)
    print(" ACTUALIZAR STOCK DE PRODUCTO")
    print("=" * 50)
    id_buscar = input("Ingrese ID del producto: ")
    producto_encontrado = None
    for producto in inventario:
        if producto[0] == id_buscar:
         producto_encontrado = producto
         break
    if producto_encontrado:
        print(f"\nProducto encontrado: {producto_encontrado[1]}")
        print(f"Stock actual: {producto_encontrado[4]}")
        nuevo_stock = int(input("Ingrese nuevo stock: "))
        producto_encontrado[4] = nuevo_stock
        print("\n✅ Stock actualizado correctamente!")
    else:
        print("\n❌ Producto no encontrado!")