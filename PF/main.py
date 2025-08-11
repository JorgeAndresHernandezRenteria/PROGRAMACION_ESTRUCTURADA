from funciones import *
from usuarios import usuarioss
from productos import productoss
from ventas import ventass
from conexionBD import reiniciar_tabla 
import getpass

#Proyecto SIX por: 
#Irvin Alfonso Solis Flores y Jorge Andrés Hernández Rentería 2°C TI Clásica

def main():
    usuario_actual = None 
    
    while True:
        if not usuario_actual:
            opcion = menu_principal()
            
            if opcion == "1":  # Login
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" INICIO DE SESIÓN")
                print("=" * 50)
                usuario = input("Usuario: ").strip()
                contrasena = getpass.getpass("Contraseña: ").strip()
                
                usuario_actual = usuarioss.autenticar_usuario(usuario, contrasena)
                if usuario_actual:
                    print(f"\nBienvenido {usuario_actual['nombre']}!")
                    esperar_tecla()
                else:
                    print("\n❌ Credenciales incorrectas")
                    esperar_tecla()
                    
            elif opcion == "2":  # Registro
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" REGISTRO DE USUARIO")
                print("=" * 50)
                nombre = input("Nombre: ").strip().title()
                apellido = input("Apellido: ").strip().title()
                usuario = input("Usuario: ").strip().lower()
                contrasena = getpass.getpass("Contraseña: ").strip()
                registrar = usuarioss.registrar_usuario(nombre, apellido, usuario, contrasena)
                if registrar:
                    print("\n✅ Usuario registrado exitosamente!")
                else:
                    print("\n❌ Error al registrar usuario")
                esperar_tecla()

            elif opcion == "3":  # Salir
                print("\n¡Hasta pronto! 🍻")
                break
                
            else:
                print("\n❌ Opción inválida")
                esperar_tecla()

        else:  # Menú principal para usuarios autenticados
            opcion = menu_inventario()
            
            if opcion == "1":  # Realizar venta
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" REGISTRAR VENTA")
                print("=" * 50)
                # Mostrar productos disponibles
                productos = productoss.listar()
                print("\nPRODUCTOS DISPONIBLES:")
                print(f"{'ID':<5}{'Nombre':<20}{'Precio':<10}{'Stock':<10}")
                print("-" * 45)
                for p in productos:
                    print(f"{p['id']:<5}{p['nombre'][:18]:<20}{formatear_precio(p['precio']):<10}{p['stock']:<10}")
                
                # Seleccionar productos
                productos_seleccionados = []
                while True:
                    try:
                        print("\n" + "-" * 50)
                        id_producto = int(input("ID del producto (presiona 0 para finalizar con la compra): "))
                        if id_producto == 0:
                            break
                            
                        producto = next((p for p in productos if p['id'] == id_producto), None)
                        if not producto:
                            print("❌ ID no válido")
                            continue
                            
                        cantidad = int(input(f"Ingresa la cantidad de {producto['nombre']} que deseas comprar ({producto['stock']} en disponibilidad): "))
                        if cantidad <= 0:
                            print("❌ La cantidad debe ser mayor que 0")
                            continue

                        if cantidad > producto['stock']:
                            print(f"❌ Stock insuficiente... (Disponible: {producto['stock']})")
                            continue
                        producto['stock'] -= cantidad    
                        productos_seleccionados.append({
                            'id': producto['id'],
                            'cantidad': cantidad,
                            'precio': producto['precio']})
                        print(f"✅ Añadido: {cantidad} x {producto['nombre']}")

                    except ValueError:
                        print("❌ Ingresa un valor numérico")
                        continue
                
                # Procesar venta
                if productos_seleccionados:
                    if ventass.registrar_venta(usuario_actual['id'], productos_seleccionados):
                        print("\n✅ Venta registrada!")
                        # Mostrar resumen
                        print("\nRESUMEN DE VENTA:")
                        print("-" * 30)
                        total = 0
                        for item in productos_seleccionados:
                            subtotal = item['cantidad'] * item['precio']
                            prod_nombre = next(p['nombre'] for p in productos if p['id'] == item['id'])
                            print(f"{item['cantidad']} x {prod_nombre}")
                            print(f"  {formatear_precio(item['precio'])} c/u = {formatear_precio(subtotal)}")
                            total += subtotal
                        print("-" * 30)
                        print(f"TOTAL: {formatear_precio(total)}")
                    else:
                        print("\n❌ Error al registrar venta")
                else:
                    print("\n⚠️ No se seleccionaron productos")
                esperar_tecla()
                            
            elif opcion == "2":  # Registrar producto
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" REGISTRO DE PRODUCTO")
                print("=" * 50)
                codigo = input("Código de barras: ").strip()
                nombre = input("Nombre del producto: ").strip().title()
                categoria = input("Categoría (Bebida/Snack): ").strip().title()
                precio = float(input("Precio unitario: $"))
                stock = int(input("Stock inicial: "))
                crearp = productoss.crear(codigo, nombre, categoria, precio, stock,usuario_actual['id'])
                if crearp:
                    print("\n✅ Producto registrado exitosamente!")
                else:
                    print("\n❌ Error al registrar producto")
                esperar_tecla()

            elif opcion == "3":  # Listar productos
                borrar_pantalla()
                print("\n" + "=" * 90)
                print(" INVENTARIO DE PRODUCTOS")
                print("=" * 90)
                print(f"{'Código':<15}{'Nombre':<20}{'Categoría':<15}{'Precio':>15}{'Stock':>10}")
                print("-" * 90)
                lista = productoss.listar()
                
                if lista:
                    for p in lista:
                        precio_fmt = formatear_precio(p['precio'])
                        print(f"{p['codigo']:<15}{p['nombre'][:18]:<20}{p['categoria']:<15}{precio_fmt:>15}{p['stock']:>10}")
                else:
                    print("No hay productos registrados")
                print("=" * 90)
                esperar_tecla()
                
            elif opcion == "4":  # Buscar producto
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" BUSCAR PRODUCTO")
                print("=" * 50)
                codigo = input("Ingrese código de barras: ").strip()
                producto = productoss.buscar(codigo)
                if producto:
                    print("\n" + "-" * 50)
                    print(f"Código: {producto['codigo']}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Categoría: {producto['categoria']}")
                    print(f"Precio: {formatear_precio(producto['precio'])}")
                    print(f"Stock: {producto['stock']} unidades")
                else:
                    print("\n❌ Producto no encontrado")
                esperar_tecla()
            
            elif opcion == "5":  # Actualizar stock
                borrar_pantalla()
                print("\n" + "=" * 50)
                print(" ACTUALIZAR STOCK")
                print("=" * 50)
                codigo = input("Código de barras: ").strip()
                nuevo_stock = int(input("Nuevo stock: "))
                actualizar = productoss.actualizar_stock(codigo, nuevo_stock)
                if actualizar:
                    print("\n✅ Stock actualizado correctamente!")
                else:
                    print("\n❌ Error al actualizar stock")
                esperar_tecla()

            elif opcion == "6":  # Menú de administración de tablas
                if usuario_actual and usuario_actual['rol'] == 'empleado':
                    while True:
                        opcion_admin = menu_admin()
                        
                        if opcion_admin == "1":  # Reiniciar tabla productos
                            if reiniciar_tabla("productos"):
                                print("\n✅ Tabla de productos reiniciada correctamente")
                            else:
                                print("\n❌ Error al reiniciar tabla")
                            esperar_tecla()
                            
                        elif opcion_admin == "2":  # Reiniciar tabla ventas
                            if reiniciar_tabla("ventas"):
                                print("\n✅ Tabla de ventas reiniciada correctamente")
                            else:
                                print("\n❌ Error al reiniciar tabla")
                            esperar_tecla()

                        elif opcion_admin == "3":  # Reiniciar tabla detalle_venta
                            if reiniciar_tabla("detalle_venta"):
                                print("\n✅ Tabla de detalle de ventas reiniciada correctamente")
                            else:
                                print("\n❌ Error al reiniciar tabla")
                            esperar_tecla()
                            
                        elif opcion_admin == "4":  # Reiniciar tabla usuarios
                            if reiniciar_tabla("usuarios"):
                                print("\n✅ Tabla de usuarios reiniciada correctamente")
                            else:
                                print("\n❌ Error al reiniciar tabla")
                            esperar_tecla()

                        elif opcion_admin == "5":  # Exportar datos de las tablas
                            borrar_pantalla()
                            print("\n" + "=" * 50)
                            print(" EXPORTAR DATOS")
                            print("=" * 50)
                            print("1. Exportar Usuarios")
                            print("2. Exportar Productos")
                            print("3. Exportar Ventas")
                            print("4. Exportar Detalle de Ventas")
                            print("5. Volver")

                            sub_opcion = input("\nSeleccione tabla a exportar: ")
                            
                            if sub_opcion == "5":
                                continue

                            tablas = {
                                "1": "usuarios",
                                "2": "productos",
                                "3": "ventas",
                                "4": "detalle_venta"
                            }

                            tabla_seleccionada = tablas.get(sub_opcion)
                            if not tabla_seleccionada:
                                print("\n❌ Opción inválida")
                                esperar_tecla()
                                continue

                            print("\nFormato de exportación:")
                            print("1. Excel")
                            print("2. PDF")
                            formato_opcion = input("Seleccione formato: ")

                            formatos = {
                                "1": "excel",
                                "2": "pdf"
                            }

                            formato = formatos.get(formato_opcion)
                            if not formato:
                                print("\n❌ Formato inválido")
                                esperar_tecla()
                                continue

                            archivo = exportar_tabla(tabla_seleccionada, formato)
                            if archivo:
                                print(f"\n✅ Tabla '{tabla_seleccionada}' exportada a {formato.upper()} correctamente")
                                print(f"Archivo: {archivo}")
                            else:
                                print("\n❌ Error al exportar los datos (es posible que no existan registros en la tabla seleccionada)")
                            
                            esperar_tecla()

                        elif opcion_admin == "6":  # Volver
                            break
                            
                        else:
                            print("\n❌ Opción inválida")
                            esperar_tecla()
                else:
                    print("\n❌ Acceso denegado: Se requiere rol de empleado")
                    esperar_tecla()
            
            elif opcion == "7":  # Cerrar sesión
                usuario_actual = None
                print("\nSesión cerrada correctamente")
                esperar_tecla()

if __name__ == "__main__":
    main()