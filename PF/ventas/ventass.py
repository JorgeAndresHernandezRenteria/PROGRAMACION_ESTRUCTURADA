from conexionBD import conectar
from mysql.connector import Error

def registrar_venta(usuario_id, productos_vendidos):

    conexion = conectar()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        
        # 1. Registrar la venta principal
        cursor.execute("""
            INSERT INTO ventas (fecha, total, usuario_id) 
            VALUES (NOW(), 0, %s)
        """, (usuario_id,))
        venta_id = cursor.lastrowid
        
        total_venta = 0
        
        # 2. Procesar cada producto vendido
        for producto in productos_vendidos:
            # Registrar detalle
            cursor.execute("""
                INSERT INTO detalle_venta 
                (venta_id, producto_id, cantidad, precio_unitario)
                VALUES (%s, %s, %s, %s)
            """, (venta_id, producto['id'], producto['cantidad'], producto['precio']))
            
            # Actualizar stock del producto
            cursor.execute("""
                UPDATE productos 
                SET stock = stock - %s 
                WHERE id = %s
            """, (producto['cantidad'], producto['id']))
            
            total_venta+= producto['precio'] * producto['cantidad']
        
        # 3. Actualizar total de la venta
        cursor.execute("""
            UPDATE ventas 
            SET total = %s 
            WHERE id = %s
        """, (total_venta, venta_id))
        
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al registrar venta: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion.is_connected():
            conexion.close()

def obtener_todas():
    conexion = conectar()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("""
            SELECT v.id, v.fecha, v.total, 
                   u.usuario AS vendedor,
                   GROUP_CONCAT(p.nombre SEPARATOR ', ') AS productos
            FROM ventas v
            JOIN usuarios u ON v.usuario_id = u.id
            JOIN detalle_venta dv ON v.id = dv.venta_id
            JOIN productos p ON dv.producto_id = p.id
            GROUP BY v.id
        """)
        return cursor.fetchall()
    except Error as e:
        print(f"Error al obtener ventas: {e}")
        return []
    finally:
        if conexion.is_connected():
            conexion.close()