from manipular_productos import *
from inicio_sesion import iniciar_sesion
from manipular_cajeros import agregar_cajeros, eliminar_cajeros, obtener_cajeros
from manipular_caja import ver_caja, init_caja

def tienda():
    while True:
        print("\nBienvenido a la tienda de Pepito. Por favor, inicia sesión para identificarte.")
        print("\nSelecciona que deseas hacer:")
        print("\n1. Iniciar sesión")
        print("2. Salir")
        opcion = input("\nIngrese una opción.\n\n>> ")
        while opcion.isnumeric() == False or int(opcion) not in [1,2]:
            opcion = input("\nIngrese una opción.\n\n>> ")
        if int(opcion) == 1:
            session = iniciar_sesion()
        elif int(opcion) == 2:
            break
        while True:
            if "error" in session:
                print(session["error"])
                break
            
            if(session["is_admin"] == True):
                print(f"\nBienvenido administrador *{session['usuario']}*. Elige una opción entre las disponibles.")
                print("\n1. Agregar cajeros.")
                print("2. Eliminar cajeros.")
                print("3. Agregar productos.")
                print("4. Modificar productos.")
                print("5. Ver cajeros.")
                print("6. Ver caja.")
                print("7. Salir.")
                opcion: str = input("Ingrese una opción: ")
                while opcion.isnumeric() == False or int(opcion) not in [1, 2, 3, 4, 5, 6, 7]:
                    opcion = input("Ingrese una opción: ")
                
                if opcion == "1":
                    nuevo_cajero = agregar_cajeros()
                    print("\nLos cajeros se han agregado con éxito.")
                    for i in nuevo_cajero:
                        print("\nCajero:", i[0])
                        print("Documento:", i[1])
                        print("Edad:", i[2])
                        print("Contraseña:", i[3])
                elif opcion == "2":
                    eliminar_cajeros()
                elif opcion == "3":
                    add_products()
                elif opcion == "4":
                    modify()
                elif opcion == "5":
                    obtener_cajeros()
                elif opcion == "6":
                    ver_caja()
                elif opcion == "7":
                    break
            elif (session["is_admin"] == False):
                print(f"\nBienvenido *{session['usuario']}*. Elige una opción entre las disponibles.")
                init_caja(session['usuario'], session['documento'])
                break

tienda()