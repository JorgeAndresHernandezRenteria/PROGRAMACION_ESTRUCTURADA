from conexionBD import conectar
import hashlib
from datetime import datetime

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar_usuario(nombre, apellido, usuario, contrasena, rol="empleado"):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            contrasena_hash = hash_password(contrasena)
            sql = """INSERT INTO usuarios 
                    (nombre, apellido, usuario, contrasena, rol, fecha_registro) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (nombre, apellido, usuario, contrasena_hash, rol, datetime.now())
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return False
        finally:
            conexion.close()
    return False

def autenticar_usuario(usuario, contrasena):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            contrasena_hash = hash_password(contrasena)
            sql = """SELECT id, nombre, apellido, rol 
                    FROM usuarios WHERE usuario = %s AND contrasena = %s"""
            cursor.execute(sql, (usuario, contrasena_hash))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al autenticar: {e}")
            return None
        finally:
            conexion.close()
    return None