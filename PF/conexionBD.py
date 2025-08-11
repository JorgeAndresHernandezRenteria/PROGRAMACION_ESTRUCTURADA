import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_six"
        )
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None
    
def reiniciar_tabla(nombre_tabla):
    conexion = conectar()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        # Desactivamos temporalmente las FK (claves foraneas) para evitar errores al eliminar cualquier registro de cualquier tabla
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute(f"TRUNCATE TABLE {nombre_tabla}")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        conexion.commit()
        return True
    except Error as e:
        print(f"Error al reiniciar tabla: {e}")
        conexion.rollback()
        return False
    finally:
        if conexion.is_connected():
            conexion.close()