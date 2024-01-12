import sys
import os

user_="admin"                      #usuario correcto
pwd_="123"                         #contraseña correcta

contador = 0                       #cuenta la cantidad de accesos  
saldo = 2000                #saldo incial de la cuenta
opcion = 0

######## FUNCIONES ########
def depositar():   #si ingresa la opcion 1
    global saldo
    print("Ingrese cantidad a depositar: ")
    cantidad = int(input())
    saldo += cantidad
    print("Saldo actual: ", saldo)

def retirar():  #si ingresa la opcion 2
    global saldo
    print("Ingrese monto a retirar: ")
    cantidad = int(input())
    saldo -= cantidad
    print("Saldo actual: ", saldo)

def transferir():  #si ingresa la opcion 2
    global saldo
    print("Ingrese monto a transferir: ")
    cantidad = int(input())
    saldo -= cantidad
    print("Saldo transferido con exito, saldo actual: ", saldo)

def ver():  # si ingresa la opcion 4
    global saldo
    print("Saldo actual: ", saldo)
    input("Presiona Enter para continuar...")

def limpiar_consola():
    sistema_operativo = os.name
    if sistema_operativo == 'posix':  # Linux y macOS
        os.system('clear')
    elif sistema_operativo == 'nt':   # Windows
        os.system('cls')
######## FIN FUNCIONES ########

while (contador < 3):              #mientras que el contador no sea superior a 3, puede seguir intentando ingresar
    print("Usuario: ")
    user = input()                  #carga los datos ingresados
    print("Contraseña: ")
    pwd = input()                   #carga los datos ingresados
    limpiar_consola()
    
    if user == user_ and pwd == pwd_:   #verifica que coincida (si hay coincidencia)
        print("Bienvenido")             #caso correcto (ingreso)
        print(" ")
        
        while opcion !=5:
            print("-----MENU----")
            print("1.Depositar")
            print("2.Retirar ")
            print("3.Transferir ")
            print("4.Ver")
            print("5.salir")
            opcion = int(input())

            if opcion == 1:
                limpiar_consola()
                depositar()
            elif opcion == 2:
                limpiar_consola()
                retirar()
            elif opcion == 3:
                limpiar_consola()
                transferir()
            elif opcion == 4:
                limpiar_consola()
                ver()
            elif opcion == 5:
                print("saliendo")
                sys.exit()
            else:
                print("no existe esa opcion")
            contador = 4
    else:                   #si no coincide 
        print ("usuario o contraseña incorrecto")       #caso incorrecto
        if contador == 2:                           #en el caso que sea 3 los intentos hechos, bloquea la cuenta
            limpiar_consola()
            print("acceso bloqueado")
            sys.exit()  
        contador += 1  
                         

