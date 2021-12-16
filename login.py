import cx_Oracle

from menuPrincipal import *


class login:
    conexion = cx_Oracle.connect(
    user = 'escuela',
    password = '1234',
    dsn = 'localhost:1521/xe')

    cursor = conexion.cursor()
    print ("==================================================")
    print ("|=============== Bienvenido =====================|")
    usuario = input("Ingrese usuario: ")
    contraseña = input("Ingrese contraseña: ")
    print ("==================================================")


    login= '''select * from usuarios where usuario=:us and contrasena=:Con ''' 
    cursor.execute (login,us=usuario,con=contraseña)
    resultado = cursor.fetchall()
    print (len(resultado))
    if len(resultado)==1:
        print ("Ingresado correctamente")
        menuIngreso()
        
    else:
        print ("Usuario o contraseña incorrectos")
    cursor.close()
    conexion.close()

login()