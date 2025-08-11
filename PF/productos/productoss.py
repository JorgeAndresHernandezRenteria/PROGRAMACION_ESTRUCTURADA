from conexionBD import conectar
from datetime import datetime

def crear(codigo, nombre, categoria, precio, stock, usuario_id):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = """INSERT INTO productos 
                    (codigo, nombre, categoria, precio, stock, fecha_actualizacion, usuario_id) 
                    VALUES (%s, %s, %s, %s, %s, NOW(), %s)"""
            val = (codigo, nombre, categoria, precio, stock, usuario_id)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar producto: {e}")
            return False
        finally:
            conexion.close()
    return False

def listar():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = """SELECT id, codigo, nombre, categoria, precio, stock 
                    FROM productos ORDER BY nombre"""
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar productos: {e}")
            return []
        finally:
            conexion.close()
    return []

def buscar(codigo):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = """SELECT id, codigo, nombre, categoria, precio, stock 
                    FROM productos WHERE codigo = %s"""
            cursor.execute(sql, (codigo,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al buscar producto: {e}")
            return None
        finally:
            conexion.close()
    return None

def actualizar_stock(codigo, nuevo_stock):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = """UPDATE productos SET stock = %s, 
                    fecha_actualizacion = %s WHERE codigo = %s"""
            val = (nuevo_stock, datetime.now(), codigo)
            cursor.execute(sql, val)
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar stock: {e}")
            return False
        finally:
            conexion.close()
    return False