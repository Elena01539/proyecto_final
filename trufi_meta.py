#este codigo te ayuda a ver que truffis de la ciudad de cercado pasan por los lugares turisticos de dicha ciudad
import time
contraseña="mariaelena1"
cont=0
while cont<=3:
    contraseña1=str(input("Ingrese su contraseña: "))
    if contraseña1==contraseña:
        print("Bienvenido")
        break
    else:
        print("Contraseña incorrecta,intente de nuevo:")
        cont=cont+1
        if cont>3:
            print("demasiados intentos espere un momento antes de intentar de nuevo")
            time.sleep(5)
            cont=0
