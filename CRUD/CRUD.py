# pip install mysql-connector-python -> intstalar conector
# pip list   para saber si quedo intalado
import mysql.connector # este es el que nos ayuda comunicarnos con base de datos

# conexion de la base de datos con programacion funcional
def conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ejemplo",
        port=3307 # ojo el  que usted tenga
    )
db=conexion() # abril la conexion de la base de datos
cursor=db.cursor() # cursor es el que nos ayuda a ejecutar las consultas
db.commit() # confirmar los cambios
db.close() # cerrar la conexion
print("conexion exitosa")
#vamos a listar la  base de datos
def listar_usuario():
    db=conexion() # abril la conexion de la base de datos
    cursor=db.cursor() # cursor es el que nos ayuda a ejecutar las consultas
    cursor.execute("SELECT * FROM usuario") # ejecutar la consulta
    resultado=cursor.fetchall() # fetchall trae todos los registros
    for fila in resultado:
        print(fila)
    db.close() # cerrar la conexion
#insertar
def insertar_usuario(nombre,email):
    db=conexion()
    cursor=db.cursor()
    sql="INSERT INTO usuario(nombre,email) VALUES (%s,%s)"
    valores=(nombre,email)
    cursor.execute(sql,valores)
    db.commit()
    db.close()
insertar_usuario("pan","pan_ernandes.com")
# actualizar
def actualizar_usuario(id,nombre,email):
    db= conexion()
    cursor=db.cursor()
    cursor.execute("UPDATE usuario SET nombre =%s, email=%s WHERE id = %s;",(nombre.email,id))
    db.commit()
    print("fue actualizado exitozamente")
    db.close()
    #eliminar usuario
def eliminar_usuario():
    db.conexion()
    cursor=db.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=%s",(id,))
    db.commit()
    print("usuarios eliminados")
    db.close()
eliminar_usuario()
#insertar_usuario(nombre,email)
listar_usuario()
def menu():
    while True:
        print("bienvenido al sistema mi primer crud python")
        print("1 insertar")
        print("2 actualizar")
        print("3 eliminar")
        print("4 listar")
        print("5 salir de este menu ")
        opcion=int(input("ingrese sesion"))
        match opcion:
            case 1:
                nombre = input("ingrese el nombre del usuario:")
                email = input("ingrese el email del usuario:")
                insertar_usuario(nombre, email)
                print(f"ingresas al sistema {nombre} {email}")
            case 2:
            id = int(input("ingrese el id del usuario a actualizar:"))
            nombre = input("ingrese el nuevo nombre del usuario:")
            email = input("ingrese el nuevo email del usuario:")
            actualizar_usuario(id, nombre, email)
            print(f"ingresas al sistema {nombre} {email}")

        
        
        case 3:
            id = int(input("ingrese el id del usuario a eliminar:"))
            eliminar_usuario(id)
            print(f"Elimino del sistema {id}")
        case 4:
            listar_usuario()
        case 5:
            print("saliendo del sistema...")
            break
        case _:
            print("opcion no valida")

menu()