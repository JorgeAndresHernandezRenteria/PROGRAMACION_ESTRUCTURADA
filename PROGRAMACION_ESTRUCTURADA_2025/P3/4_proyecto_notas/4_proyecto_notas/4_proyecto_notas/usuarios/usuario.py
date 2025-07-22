from conexionBD import *
import datetime 

def registrar(nombre,apellidos,email,password):
    try:
     fecha=datetime.datetime.now()#Regresa la fecha actual y la guarda en la variabe "fecha"
     sql="insert into usuarios (nombre,apellidos,email,password,fecha) values(%s,%s,%s,%s,%s)"
     val=(nombre,apellidos,email,password,fecha)
     cursor.executive(sql,val)
     conexion.commit()
     return True
    except:
       return False
    
def iniciar_sesion(email,password):
   try:
      sql="select * from usuarios where email=%s and password=%s"
      val=(email,password)
      cursor.execute(sql,val)
      registro=cursor.fetchone()
      if registro:
         return registro
      else:
         return None
   except: 
      return None