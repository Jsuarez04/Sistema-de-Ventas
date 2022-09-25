
#DECLARAMOS UN USUARIO Y UN PASSWORD PARA INGRESAR#
from tkinter import Menu


print("::: BIENVENIDO A EVA'S POS :::")
Usuarios={"master":1234, "gerente":5678}
contador = 0
#Aquí mostramos las distintas opciones a elegir para cada operación#
def Menu_principal():
    print('\t ::: BIENVENIDO :::')
    print("\t:: MENÚ PRINCIPAL ::")
    print("1. ::: ARCHIVO :::")
    print("2. ::: MOVIMIENTOS :::")
    print("3. ::: AYUDA :::")
    print("4. ::: SALIR :::")
    opcion = int(input("Ingrese el número de su opción: "))
    
    if opcion == 1:
        print("\t :: ARCHIVO ::")
        print("1. ::: USUARIOS :::")
        print("2. ::: CLIENTES :::")
        print("3. ::: PRODUCTOS :::")
        print("4. ::: CAMBIO DE USUARIO :::")
        print("5. ::: CAMBIO DE CLAVE :::")
        print("6. ::: SALIR :::")
        opcion_archivo=int(input("Ingrese el número de su opción: "))
    
        if opcion_archivo== 1:
            return Menu_Usuarios()
        
        elif opcion_archivo == 2:
            pass
        elif opcion_archivo == 6:
            return Menu_principal()    

while True:
    usuario_=input("Ingrese su nombre de usuario:")
    clave_=int(input("Ingrese su clave numerica:"))
    if usuario_ in Usuarios and clave_ == Usuarios[usuario_]:
        Menu_principal()
        break
    else:
        print("Usuario y/o contaseña incorrectos ¡Inténtelo de nuevo!...")

#Ahora pedimos al usuario ingresar el número de la operación que quiera realizar#


def Menu_Usuarios(): 
    print("1. :: AGREGAR NUEVO USUARIO ::")
    print("2. :: ELIMINAR USUARIO ::")
    print("3. :: VER USUARIOS ::")
    print("4. :: SALIR ::")
    opcion_usuario=int(input("Ingrese el número de su opción: "))
        
    if opcion_usuario==1:
        agg_us=(input("INGRESE EL NOMBRE DEL NUEVO USUARIO: ")) 
        agg_passw =(input("INGRESE LA CLAVE DEL NUEVO USUARIO: ")) 
        conf=(input("CONFIRME LA CLAVE DEL NUEVO USUARIO: ")) 
        if agg_passw==conf:
            Usuarios[agg_us] = agg_passw
            print("USUARIO AGREGADO EXITOSAMENTE")
            return Menu_Usuarios()
        else:
            print("Inténtelo de nuevo!!!")    
            return Menu_Usuarios()
    
    elif opcion_usuario == 2:
        print("***Eliminacion de Usuarios***")
        for key in Usuarios:
            contador += 1
            print(f"{contador}. {key}")
        opcion_elim = input("Ingrese el nombre del usuario que desea eliminar: ")
            
        if opcion_elim in Usuarios:
            Usuarios.pop(opcion_elim)
            print("Usuario eliminado!")
            return Menu_Usuarios()
        else:
            print("Ese usuario no esta registrado...")
            return Menu_Usuarios()
    
    elif opcion_usuario == 3:
        print("\t:::Reporte de usuarios:::")
        print("Nombre - Contraseña - Nivel de seguridad")
        for key, value in Usuarios.items():
            if key == "master" or key == "gerente":
                print(f"{key}  \t{value}  \t Alto")
            else:
                print(f"{key}  \t{value}  \t Bajo")
        Salir= input("Escribe salir para retroceder: ")
        if Salir == "salir":
            return Menu_Usuarios()

