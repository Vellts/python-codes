from time import sleep
from util import validar_fecha, existe_usuario
from database import cajeros

def agregar_cajeros() -> None:
    nuevos_cajeros_temp: list = []
    nuevos_cajeros: list = []
    print("\nInterfaz para la manipulación de usuarios. Sección [AGREGAR]")
    
    while True:
        while True:
            nombre: str = input("\nIngresa el nombre en MAYÚSCULAS.\n\n>> ")
            while (len(nombre) < 2 or nombre.upper() != nombre):
                nombre = input("\nError. Ingresa el nombre en MAYÚSCULAS.\n\n>> ")
            
            apellido_uno: str = input("\nIngresa el primer apellido en MAYÚSCULAS.\n\n>> ")
            while (len(apellido_uno) < 2 or apellido_uno.upper() != apellido_uno):
                apellido_uno = input("\nError. Ingresa el primer apellido en MAYÚSCULAS.\n\n>> ")

            apellido_dos: str = input("\nIngresa el segundo apellido en MAYÚSCULAS.\n\n>> ")
            while (len(apellido_dos) < 2 or apellido_dos.upper() != apellido_dos):
                apellido_dos = input("\nError. Ingresa el primer apellido en MAYÚSCULAS.\n\n>> ")

            nombre_completo: str = f"{nombre.strip().capitalize()} {apellido_uno.strip().capitalize()} {apellido_dos.strip().capitalize()}"
            usuario_existente: bool = existe_usuario(nombre_completo)
            if usuario_existente:
                print("\nError. El usuario ya existe.")
                continue
            else:
                nuevos_cajeros_temp.append(nombre_completo)
                break

        documento: str = input("\nIngresa el documento.\n\n>> ")
        while (len(documento) < 2 or documento.isnumeric() == False):
            documento = input("\nError. Ingresa el documento.\n\n>> ")
        nuevos_cajeros_temp.append(documento)

        fecha_nacimiento: str = input("\nIngresa la fecha de nacimiento. Formato [dd/mm/yyyy].\n\n>> ")
        edad: str = validar_fecha(fecha_nacimiento) #25,
        nuevos_cajeros_temp.append(edad)

        contrasena: str = f"{documento}{nombre[0].strip().upper()}{apellido_uno[0].strip().lower()}*"
        nuevos_cajeros_temp.append(contrasena)

        nuevos_cajeros.append(nuevos_cajeros_temp)

        agregar_mas: str = input("\n¿Desea agregar otro cajero?\n\n[1] -> Si\n[2] -> No\n\n>> ")
        while (agregar_mas.isnumeric() == False or int(agregar_mas) not in [1, 2]):
            agregar_mas = input("\n¿Desea agregar otro cajero?\n\n[1] -> Si\n[2] -> No\n\n>> ")
        if agregar_mas == "1":
            nuevos_cajeros_temp = []
            continue
        elif agregar_mas == "2":
            for i in nuevos_cajeros:
                cajeros.append({
                    "usuario": i[0],
                    "documento": i[1],
                    "edad": i[2],
                    "contrasena": i[3]
                })
            break
    return nuevos_cajeros

def eliminar_cajeros():
    print("\nInterfaz para la manipulación de usuarios. Sección [ELIMINAR]")
    cajero_eliminado: bool = False

    while True:
        tipo_eliminacion: str = input("\n¿Qué tipo de eliminación desea realizar?\n\n1 -> Eliminar por documento\n2 -> Eliminar por nombre\n3 -> Salir\n\n>> ")
        while (tipo_eliminacion.isnumeric() == False or int(tipo_eliminacion) not in [1, 2, 3]):
            tipo_eliminacion = input("\n¿Qué tipo de eliminación desea realizar?\n\n1 -> Eliminar por documento\n2 -> Eliminar por nombre\n3 -> Salir\n\n>> ")
        
        if tipo_eliminacion == "1":
            documento: str = input("\nIngresa el documento del cajero que deseas eliminar.\n\n>> ")
            while (documento.isnumeric() == False or len(documento) < 2):
                documento = input("\nIngresa el documento del cajero que deseas eliminar.\n\n>> ")
            for i in cajeros:
                if i["documento"] == documento:
                    print(f"\n✅ -> Cajero [{i['usuario']}] con identificación [{i['documento']}] eliminado.")
                    cajeros.remove(i)
                    cajero_eliminado = True
                    break
            print("\nError. No se encontró el cajero.") if cajero_eliminado == False else None
        
        elif tipo_eliminacion == "2":
            nombre: str = input("\nIngresa el nombre del cajero que deseas eliminar: ")
            while (nombre.isalpha() == False or len(nombre) < 2):
                nombre = input("\nIngresa el nombre del cajero que deseas eliminar: ")
            for i in cajeros:
                if i["usuario"] == nombre:
                    print(f"✅ -> Cajero [{i['usuario']}] con identificación [{i['documento']}] eliminado.")
                    cajeros.remove(i)
                    cajero_eliminado = True
                    break
            print("\nError. No se encontró el cajero.") if cajero_eliminado == False else None
        elif tipo_eliminacion == "3":
            break

def obtener_cajeros():
    count: int = 0
    print("\nObteniendo cajeros...")
    print("-----------------------")
    if len(cajeros) == 0:
        print("❎ -> No se encontraron cajeros.")
        return
    else:
        for i in cajeros:
            #print(i)
            count += 1
            print(f"\nN #{count}")
            print("\nCajero:", i["usuario"])
            print("Documento:", i["documento"])
            print("Edad:", i["edad"])
            print("Contraseña:", i["contrasena"])
            sleep(0.5)
            print("-----------------------")