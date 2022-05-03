from database import caja, cajeros
from manipular_productos import obtener_categorias, obtener_marcas, obtener_productos
from util import fecha_actual, generar_id_factura, mostrar_productos

def verify_producto_en_caja(id_producto: int) -> list:
    for i in caja:
        if i[5] == id_producto:
            return [True, i[-2]] #[True, cantidad]
    return [False]

def agregar_producto(usuario: str, documento: int, id_producto: int, nombre_producto: str, cantidad: int, precio: int):
    for i in caja:
        if i[5] == id_producto:
            i[-2] += cantidad
            i[-1] += precio
            return i
        else:
            continue
    
    caja.append([generar_id_factura(), usuario, str(documento), fecha_actual()[0], fecha_actual()[1], id_producto, nombre_producto, cantidad, precio * cantidad])
    return caja[-1]

def agregar_caja(nombre, documento):
    print("\nInterfaz cajero. Agregar productos a la caja.")
    max_error: int = 0

    while True:
        categorias: list = obtener_categorias()

        print("\nProductos disponibles:")
        print("-> ", categorias[0])
        print("-> ", categorias[1])
        print("-> ", categorias[2])
        print("-> ", categorias[3])

        categoria: str = input("\nIngresa el nombre tal y como está.\n\n>> ")
        while categoria not in categorias:
            categoria = input("\nIngresa el nombre tal y como está.\n\n>> ")

        if categoria == "Bebidas":
            tipo_bebida: str = input("\nIngrese el tipo de bebida.\n\n-> Alcoholica\n-> Gaseosa\n\n>> ")
        
            while tipo_bebida not in ["Alcoholica", "Gaseosa"]:
                tipo_bebida: str = input("\nIngrese el tipo de bebida.\n\n-> Alcoholica\n-> Gaseosa\n\n>> ")
            if tipo_bebida == "Alcoholica":
                tipo_alcohol: str = input("\nIngrese el tipo de alcohol.\n\n-> Vino\n-> Cerveza\n-> Whisky\n\n>> ")

                while tipo_alcohol not in ["Vino", "Cerveza", "Whisky"]:
                    tipo_alcohol: str = input("\nIngrese el tipo de alcohol.\n\n-> Vino\n-> Cerveza\n-> Whisky\n\n>> ")

                marcas: list = obtener_marcas(categoria, True, tipo_bebida, tipo_alcohol)
                
                print("\nMarcas disponibles:")
                print("-> ", marcas[0])
                print("-> ", marcas[1])
                print("-> ", marcas[2])

                marca: str = input("\nIngrese la marca de la bebida.\n\n>> ")

                while marca not in marcas:
                    marca: str = input("\nIngrese la marca de la bebida.\n\n>> ")

                productos: list = obtener_productos(categoria, marca, True, tipo_bebida, tipo_alcohol)

                print("\nProductos:\n")
                mostrar_productos(productos, False)

                id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")

                while id_producto.isnumeric() == False or int(id_producto) not in [ids for ids in productos if isinstance(ids, int)]:
                    id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")
                
                producto = productos[productos.index(int(id_producto)) + 1]
                precio = productos[productos.index(int(id_producto)) + 2]
                stock = productos[productos.index(int(id_producto)) + 3]

                if verify_producto_en_caja(int(id_producto))[0]:
                    cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")
                    
                    while cantidad.isnumeric() == False or int(cantidad) <= 0 or (int(cantidad)+verify_producto_en_caja(int(id_producto))[1]) > int(stock):
                        if max_error >= 3:
                            print("\nParece que has excedido el número de intentos. Es posible que el producto que has escodigo esté sin stock.")
                            return
                        else:
                            cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")
                            max_error += 1

                    x = agregar_producto(nombre, documento, int(id_producto), producto, int(cantidad), precio)
                    print(f"\n✅ -> Se ha agregado la caja con el ID #{x[0]}. Producto: {x[6]}. Cantidad: {x[7]}")
                else:
                    cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")

                    while cantidad.isnumeric() == False or int(cantidad) <= 0 or int(cantidad) > int(stock):
                        if max_error >= 3:
                            print("\nParece que has excedido el número de intentos. Es posible que el producto que has escodigo esté sin stock.")
                            return
                        else:
                            cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")
                            max_error += 1

                    x = agregar_producto(nombre, documento, int(id_producto), producto, int(cantidad), precio)
                    print(f"\n✅ -> Se ha agregado la caja con el ID #{x[0]}. Producto: {x[6]}. Cantidad: {x[7]}")

            elif tipo_bebida == "Gaseosa":
                marcas: list = obtener_marcas(categoria, True, tipo_bebida)
                
                print("\nMarcas disponibles:")
                print("-> ", marcas[0])
                print("-> ", marcas[1])

                marca: str = input("\nIngrese la marca de la bebida.\n\n>> ")

                while marca not in marcas:
                    marca: str = input("\nIngrese la marca de la bebida.\n\n>> ")

                productos: list = obtener_productos(categoria, marca, True, tipo_bebida)

                print("\nProductos:\n")
                mostrar_productos(productos, False)

                id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")

                while id_producto.isnumeric() == False or int(id_producto) not in [ids for ids in productos if isinstance(ids, int)]:
                    id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")
                
                producto = productos[productos.index(int(id_producto)) + 1]
                precio = productos[productos.index(int(id_producto)) + 2]
                stock = productos[productos.index(int(id_producto)) + 3]

                if verify_producto_en_caja(int(id_producto))[0]:
                    cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")
                    
                    while cantidad.isnumeric() == False or int(cantidad) <= 0 or (int(cantidad)+verify_producto_en_caja(int(id_producto))[1]) > int(stock):
                        if max_error >= 3:
                            print("\nParece que has excedido el número de intentos. Es posible que el producto que has escodigo esté sin stock.")
                            return
                        else:
                            cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")
                            max_error += 1

                    x = agregar_producto(nombre, documento, int(id_producto), producto, int(cantidad), precio)
                    print(f"\n✅ -> Se ha agregado la caja con el ID #{x[0]}. Producto: {x[6]}. Cantidad: {x[7]}")
                else:
                    cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")

                    while cantidad.isnumeric() == False or int(cantidad) <= 0 or int(cantidad) > int(stock):
                        if max_error >= 3:
                            print("\nParece que has excedido el número de intentos. Es posible que el producto que has escodigo esté sin stock.")
                            return
                        else:
                            cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")
                            max_error += 1

                    x = agregar_producto(nombre, documento, int(id_producto), producto, int(cantidad), precio)
                    print(f"\n✅ -> Se ha agregado la caja con el ID #{x[0]}. Producto: {x[6]}. Cantidad: {x[7]}")

        elif categoria == "Carnes":
            productos = obtener_productos(categoria)
        
            print("\nProductos:\n")
            mostrar_productos(productos, False)

            id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")
            while id_producto.isnumeric() == False or int(id_producto) not in [ids for ids in productos if isinstance(ids, int)]:
                id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")

            producto = productos[productos.index(int(id_producto)) + 1]
            precio = productos[productos.index(int(id_producto)) + 2]
            stock = productos[productos.index(int(id_producto)) + 3]
            #print(producto, precio, stock)
            #return

            if verify_producto_en_caja(int(id_producto))[0]:
                cantidad: str = input("\nIngrese la cantidad de kg del producto.\n\n>> ")
                
                while cantidad.isnumeric() == False or int(cantidad) <= 0 or (int(cantidad)+verify_producto_en_caja(int(id_producto))[1]) > int(stock):
                    if max_error >= 3:
                        print("\nParece que has excedido el número de intentos. Es posible que el producto que has escodigo esté sin stock.")
                        return
                    else:
                        cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")
                        max_error += 1

                x = agregar_producto(nombre, documento, int(id_producto), producto, int(cantidad), precio*int(cantidad))
                print(f"\n✅ -> Se ha agregado la caja con el ID #{x[0]}. Producto: {x[6]}. Cantidad: {x[7]}")
            else:
                cantidad: str = input("\nIngrese la cantidad de kg del producto.\n\n>> ")

                while cantidad.isnumeric() == False or int(cantidad) <= 0 or int(cantidad) > int(stock):
                    if max_error >= 3:
                        print("\nParece que has excedido el número de intentos. Es posible que el producto que has escodigo esté sin stock.")
                        return
                    else:
                        cantidad: str = input("\nIngrese la cantidad de kg del producto.\n\n>> ")
                        max_error += 1

                x = agregar_producto(nombre, documento, int(id_producto), producto, int(cantidad), precio*int(cantidad))
                print(f"\n✅ -> Se ha agregado la caja con el ID #{x[0]}. Producto: {x[6]}. Cantidad: {x[7]}")

        else:
            marcas: list = obtener_marcas(categoria)
            print("\nMarcas disponibles:")
            print("-> ", marcas[0])
            print("-> ", marcas[1])
            print("-> ", marcas[2])

            marca: str = input("\nIngrese la marca del producto.\n\n>> ")
            while marca not in marcas:
                marca: str = input("\nIngrese la marca del producto.\n\n>> ")
                
            productos: list = obtener_productos(categoria, marca)

            print("\nProductos:\n")
            mostrar_productos(productos, False)

            id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")
            while id_producto.isnumeric() == False or int(id_producto) not in [ids for ids in productos if isinstance(ids, int)]:
                id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")

            producto = productos[productos.index(int(id_producto)) + 1]
            precio = productos[productos.index(int(id_producto)) + 2]
            stock = productos[productos.index(int(id_producto)) + 3]

            if verify_producto_en_caja(int(id_producto))[0]:
                cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")
                
                while cantidad.isnumeric() == False or int(cantidad) <= 0 or (int(cantidad)+verify_producto_en_caja(int(id_producto))[1]) > int(stock):
                    if max_error >= 3:
                        print("\nParece que has excedido el número de intentos. Es posible que el producto que has escodigo esté sin stock.")
                        return
                    else:
                        cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")
                        max_error += 1

                x = agregar_producto(nombre, documento, int(id_producto), producto, int(cantidad), precio)
                print(f"\n✅ -> Se ha agregado la caja con el ID #{x[0]}. Producto: {x[6]}. Cantidad: {x[7]}")
            else:
                cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")

                while cantidad.isnumeric() == False or int(cantidad) <= 0 or int(cantidad) > int(stock):
                    if max_error >= 3:
                        print("\nParece que has excedido el número de intentos. Es posible que el producto que has escodigo esté sin stock.")
                        return
                    else:
                        cantidad: str = input("\nIngrese la cantidad del producto.\n\n>> ")
                        max_error += 1

                x = agregar_producto(nombre, documento, int(id_producto), producto, int(cantidad), precio)
                print(f"\n✅ -> Se ha agregado la caja con el ID #{x[0]}. Producto: {x[6]}. Cantidad: {x[7]}")
        break

def init_caja(nombre, documento):
    while True:
        print("\nInterfaz general cajero. Selecciona una opción de las disponibles.")
        print("\n1. Agregar productos a la caja.")
        print("2. Ver caja actual.")
        print("3. Salir.")
        opcion : str = input("\n>> ")
        while opcion.isnumeric() == False or int(opcion) not in [1, 2, 3]:
            opcion : str = input("\n>> ")

        if opcion == "1":
            agregar_caja(nombre, documento)
        elif opcion == "2":
            print("\nVerificando datos...")
            if len(caja) == 0:
                print("\nNo hay productos en la caja.")
            else:
                print(f"\nProductos en la caja de [{nombre}]")
                print(f"Documento: {documento}")

                total: int = 0
                for i in caja:
                    if i[2] == documento:
                        print(f"\nID caja: #{i[0]}")
                        print(f"Fecha: {i[3]}. Hora: {i[4]}\n")
                        for j in caja:
                            if j[2] == documento:
                                print(f"[{j[5]}] -> {j[6]} - x{j[7]} - ${j[8]}")
                                total += j[8]
                        print(f"\nTotal: ${total}")
                        break
        elif opcion == "3":
            break
    return

def verificar_cajero(documento):
    existe: bool = [False]
    for i in cajeros:
        if documento == i["documento"]:
            existe = [True, i["usuario"]]
    return existe

def ver_caja():

    tipo_caja: str = input("\n¿Qué tipo de caja desea ver?\n\n1. Caja de cajero.\n2. Caja total del día.\n\n>> ")
    while tipo_caja.isnumeric() == False or int(tipo_caja) not in [1, 2]:
        tipo_caja: str = input("\n¿Qué tipo de caja desea ver?\n\n1. Caja de cajero.\n2. Caja total del día.\n\n>> ")

    if tipo_caja == "1":
        count_to_block: int = 0
        documento: str = input("\nIngresa el documento del cajero.\n\n>> ")

        documento_verificado: list = verificar_cajero(documento)

        while documento.isnumeric() == False or documento_verificado[0] == False:
            documento: str = input("\nIngresa el documento del cajero.\n\n>> ")
            documento_verificado: list = verificar_cajero(documento)
            count_to_block += 1
            if count_to_block >= 3:
                print("\nParece que has excedido el número de intentos. Es posible que el cajero que has escodigo no exista.")
                return

        print("\nVerificando datos...")
        if len(caja) == 0:
            print("\nNo hay productos en la caja.")
        else:
            print(f"\nProductos en la caja de [{documento_verificado[1]}]")
            print(f"Documento: {documento}")

            total: int = 0
            for i in caja:
                if i[2] == documento:
                    print(f"\nID caja: #{i[0]}")
                    print(f"Fecha: {i[3]}. Hora: {i[4]}\n")
                    for j in caja:
                        if j[2] == documento:
                            print(f"[{j[5]}] -> {j[6]} - x{j[7]} - ${j[8]}")
                            total += j[8]
                    print(f"\nTotal: ${total}")
                    return
            print(f"No se ha encontrado cajas para {documento_verificado[1]}.") if total == 0 else None
    elif tipo_caja == "2":
        if len(caja) == 0:
            print("\nNo hay productos en la caja.")
        else:
            cajero_ya_pasado: list = []
            documento: int = 0
            total_del_dia: int = 0
            print("----------------------------------\n")
            for i in caja:
                if i[2] != documento and i[2] not in cajero_ya_pasado:
                    documento = i[2]
                    print(f"\nFactura de [{i[1]}]") #if i[2] not in cajero_ya_pasado else print(f"\n[NUEVA] Factura de [{i[1]}]")
                    print(f"Documento: {documento}\n")

                    total: int = 0
                    for j in caja:
                        if j[2] == documento:
                            print(f"[{j[5]}] -> {j[6]} - x{j[7]} - ${j[8]}")
                            total += j[8]
                    print(f"\nTotal de la factura: ${total}")
                    print("----------------------------------\n")
                    #total_del_dia -= total if i[2] in cajero_ya_pasado else 0
                    cajero_ya_pasado.append(i[2])
                    total_del_dia += total
            print(f"\nTotal del día: ${total_del_dia}")
            return




