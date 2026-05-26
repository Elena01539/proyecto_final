#este codigo te ayuda a ver que truffis de la ciudad de cercado pasan por los lugares turisticos de dicha ciudad
import time
usuario="Maria"
contraseña="mariaelena1"
cont=0
print("1.Registrarse ")
print("2.Iniciar sesion ")
print("3.Salir")
opcion=str(input("Elija una opcion: "))
if opcion=="1":
    lista=[]
    usuario=str(input("Usuario: "))
    contraseña=str(input("Contraseña: "))
    lista.append([usuario,contraseña])
    print("Bienvenid@ ",usuario)

if opcion=="2":
    while cont<=3:
        usuario1=str(input("Ingrese su nombre de usuario: "))
        contraseña1=str(input("Ingrese su contraseña: "))
        if contraseña1==contraseña and usuario1==usuario:
            print("Bienvenido")
            break
        if contraseña1!=contraseña or usuario1!=usuario:
            print("Contraseña o usuario incorrecto,intente de nuevo:")
            cont=cont+1
            if cont>3:
                print("demasiados intentos espere un momento antes de intentar de nuevo")
                time.sleep(5)
                cont=0

if opcion=="3":
    print("Vuelva pronto ")


