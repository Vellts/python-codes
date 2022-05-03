from database import productos
from util import is_list, mostrar_productos


def obtener_categorias() -> list:
    nombre_categorias: list = []
    for i in productos:
        if(i[0] not in nombre_categorias):
            nombre_categorias.append(i[0])
    return nombre_categorias


def obtener_marcas(categoria: str, is_bebida: bool = False, tipo_bebida: str = None, tipo_alcohol: str = None):
    nombre_marcas: list = []
    if (is_bebida == True):
        for i in productos:
            if tipo_bebida == "Gaseosa":
                if is_list(i):
                    if i[0] == categoria and i[1] == tipo_bebida:
                        # print(i)
                        if i[2] not in nombre_marcas:
                            nombre_marcas.append(i[2])
            elif tipo_bebida == "Alcoholica":
                # print(i)
                if is_list(i):
                    # print(i)
                    if i[0] == categoria and i[1] == tipo_bebida and i[2] == tipo_alcohol:
                        if i[3] not in nombre_marcas:
                            nombre_marcas.append(i[3])
    else:
        for i in productos:
            if(i[0] == categoria):
                if(i[1] not in nombre_marcas):
                    nombre_marcas.append(i[1])
    return nombre_marcas

def obtener_productos(categoria: str, marca: str = None, is_bebida: bool = False, tipo_bebida: str = None, tipo_alcohol: str = None):
    nombre_productos: list = []
    if is_bebida:
        if tipo_bebida == "Gaseosa":
            for i in productos:
                if is_list(i):
                    if i[0] == categoria and i[1] == tipo_bebida and i[2] == marca:
                        nombre_productos.append(i[3])
                        nombre_productos.append(i[4])
                        nombre_productos.append(i[5])
                        nombre_productos.append(i[6])
                        #[52, "Whisky 500ml", 2000, 10]
        elif tipo_bebida == "Alcoholica":
            for i in productos:
                if is_list(i):
                    if i[0] == categoria and i[1] == tipo_bebida and i[2] == tipo_alcohol and i[3] == marca:
                        nombre_productos.append(i[4])
                        nombre_productos.append(i[5])
                        nombre_productos.append(i[6])
                        nombre_productos.append(i[7])
        return nombre_productos
    elif categoria == "Carnes":
        for i in productos:
            if i[0] == categoria:
                nombre_productos.append(i[1])
                nombre_productos.append(i[2])
                nombre_productos.append(i[3])
                nombre_productos.append(i[4])
                #nombre_productos.append(i[5])
        return nombre_productos
    else:
        for i in productos:
            if(i[0] == categoria and i[1] == marca):
                nombre_productos.append(i[2])
                nombre_productos.append(i[3])
                nombre_productos.append(i[4])
                nombre_productos.append(i[5])
        return nombre_productos


def modificar_productos(categoria: str, marca: str, producto_id: int, nuevo_precio: int, is_bebida: bool = False, tipo_bebida: str = None, tipo_alcohol: str = None):
    if is_bebida:
        for i in productos:
            if tipo_bebida == "Gaseosa":
                if is_list(i):
                    if i[0] == categoria and i[1] == tipo_bebida and i[2] == marca and i[3] == producto_id:
                        i[5] = nuevo_precio
                        return i #["Bebidas", "Gaseosa", "Coca-Cola", 37, "Zero 355ml", 7000, 10]
            elif tipo_bebida == "Alcoholica":
                if is_list(i):
                    if i[0] == categoria and i[1] == tipo_bebida and i[2] == tipo_alcohol and i[3] == marca and i[4] == producto_id:
                        i[6] = nuevo_precio
                        return i
    elif categoria == "Carnes":
        for i in productos:
            if i[0] == categoria and i[1] == producto_id:
                i[4] = nuevo_precio
                return i
    else:
        for i in productos:
            if is_list(i):
                # print(i)
                if (i[0] == categoria and i[1] == marca and i[2] == producto_id):
                    #print(i[4])
                    i[4] = nuevo_precio
                    return i


def agregar_productos(categoria: str, marca: str, nombre_producto: str, precio_producto: int, is_bebida: bool = False, tipo_bebida: str = None, tipo_alcohol: str = None, kg: int = None):
    id: int

    for i in productos:
        if(is_list(i)):
            if(i[0] == categoria and i[1] == marca and i[3] == nombre_producto):
                # print(i)
                return False
            if i[0] == "Carnes":
                if i[0] == categoria and i[2] == nombre_producto:
                    return False
                else:
                    id = i[1] + 1
            else:
                if i[0] != "Bebidas":
                    # print(i)
                    id = i[2]+1
                else:
                    if i[1] == "Gaseosa":
                        # print(i)
                        id = i[3]+1
                    else:
                        # print(i)
                        id = i[4]+1
                continue     
    if is_bebida == False: #["Lacteos", "Taeq", 46, "Jamon de Pavo", 15000, 10],
        productos.append([categoria, marca, id, nombre_producto, precio_producto, 10])
    elif categoria == "Carnes": #[categoria, id, producto, kg, precio_por_kg]
        productos.append([categoria, id, nombre_producto, precio_producto, kg])
    else:
        if tipo_bebida == "Gaseosa":
            productos.append([categoria, tipo_bebida, marca, id, nombre_producto, precio_producto, 10])
        else:
            productos.append([categoria, tipo_bebida, tipo_alcohol, marca, id, nombre_producto, precio_producto, 10])
    return productos[-1]

def add_products():
    print("\nBienvenido a la página de productos. Sección [AGREGAR].\n\nCategorías: \n")
    categorias: list = obtener_categorias() #[Enlatados, Carnes, Bebidas]
    print("-> ", categorias[0])
    print("-> ", categorias[1])
    print("-> ", categorias[2])
    print("-> ", categorias[3])
    categoria: str = input("\nIngresa el nombre tal y como está.\n\n>> ")
    while categoria not in categorias:
        categoria = input("\nIngresa el nombre tal y como está.\n\n>> ")

    if categoria == "Bebidas":
        tipo_bebida: str = input("\nIngrese el tipo de bebida.\n\n-> Gaseosa\n-> Alcoholica\n\n>> ").lower()
        while tipo_bebida not in ["gaseosa", "alcoholica"]:
            tipo_bebida: str = input("\nIngrese el tipo de bebida.\n\n-> Gaseosa\n-> Alcoholica\n\n>> ").lower()
        if tipo_bebida == "gaseosa":
            marcas = obtener_marcas(categoria, True, tipo_bebida.capitalize())

            print("\nMarcas disponibles:")
            print("-> ", marcas[0])
            print("-> ", marcas[1])

            marca_producto: str = input("\nIngrese la marca de la bebida.\n\n>> ")
            while marca_producto not in marcas:
                marca_producto = input("\nIngrese la marca de la bebida.\n\n>> ")
            nombre_producto: str = input("\nIngrese la presentación del producto.\n\n>> ").capitalize()
            precio_producto: int = input("\nIngrese el precio del producto.\n\n>> ")

            while precio_producto.isnumeric() == False or int(precio_producto) < 0:
                precio_producto = input("\nIngrese el precio del producto.\n\n>> ")

            nuevo_producto: list = agregar_productos(categoria, marca_producto, nombre_producto, int(precio_producto), True, tipo_bebida.capitalize())
            
            if nuevo_producto == False:
                print(f"\n❌ -> No se ha podido agregar el producto {nombre_producto}.")
            else:
                print(f"\n✅ [{nuevo_producto[3]}] -> Se ha agregado el producto {nuevo_producto[2]} {nuevo_producto[4]}. Precio: {nuevo_producto[5]}.")
        
        elif tipo_bebida == "alcoholica":
            tipo_alcohol = input("\nIngrese el tipo de alcohol.\n\n-> Vino\n-> Cerveza\n-> Whisky\n\n>> ")
            while tipo_alcohol not in ["Vino", "Cerveza", "Whisky"]:
                tipo_alcohol = input("\nIngrese el tipo de alcohol.\n\n-> Vino\n-> Cerveza\n-> Whisky\n\n>> ")
            marcas = obtener_marcas(categoria, True, tipo_bebida.capitalize(), tipo_alcohol)

            print("\nMarcas disponibles:")
            print("-> ", marcas[0])
            print("-> ", marcas[1])
            print("-> ", marcas[2])

            marca_producto: str = input("\nIngrese la marca de la bebida.\n\n>> ")
            while marca_producto not in marcas:
                marca_producto = input("\nIngrese la marca de la bebida.\n\n>> ")

            nombre_producto: str = input("\nIngrese la presentación del producto.\n\n>> ").capitalize()
            precio_producto: int = input("\nIngrese el precio del producto.\n\n>> ")

            while precio_producto.isnumeric() == False or precio_producto < 0:
                precio_producto = input("\nIngrese el precio del producto.\n\n>> ")

            nuevo_producto: list = agregar_productos(categoria, marca_producto, nombre_producto, int(precio_producto), True, tipo_bebida.capitalize(), tipo_alcohol)
            
            if nuevo_producto == False:
                print(f"\n❌ -> No se ha podido agregar el producto {nombre_producto}.")
            else:
                print(f"\n✅ [{nuevo_producto[4]}] -> Se ha agregado el producto {nuevo_producto[3]} {nuevo_producto[5]}. Precio: {nuevo_producto[6]}.")
    
    elif categoria == "Carnes":
        nombre_carne: str = input("\nIngresa el nombre de carne.\n\n>> ").capitalize()
        peso_carne: int = input("\nIngresa el peso de la carne.\n\n>> ")

        while peso_carne.isnumeric() == False or int(peso_carne) <= 0:
            peso_carne: int = input("\nIngresa el peso de la carne.\n\n>> ")

        precio_carne: int = input("\nIngresa el precio de la carne por kg.\n\n>> ")
        while precio_carne.isnumeric() == False or int(precio_carne) <= 0:
            precio_carne: int = input("\nIngresa el peso de la carne.\n\n>> ")
        
        nuevo_producto: list = agregar_productos(categoria, None, nombre_carne, peso_carne, precio_carne, False, None, peso_carne)
        if nuevo_producto == False:
            print(f"\n❌ -> No se ha podido agregar el producto {nombre_carne}.")
        else:
            print(f"\n✅ [{nuevo_producto[1]}] -> Se ha agregado el producto {nuevo_producto[0]} {nuevo_producto[2]}. Precio-kg: {nuevo_producto[3]}.")
    else:
        marcas = obtener_marcas(categoria)

        print("\nMarcas disponibles:")
        print("-> ", marcas[0])
        print("-> ", marcas[1])
        print("-> ", marcas[2])

        marca_producto: str = input("\nIngrese la marca del producto.\n\n>> ")
        while marca_producto not in marcas:
            marca_producto = input("\nIngrese la marca del producto.\n\n>> ")
        nombre_producto: str = input("\nIngrese la presentación del producto.\n\n>> ").capitalize()
        precio_producto: int = input("\nIngrese el precio del producto.\n\n>> ")

        while precio_producto.isnumeric() == False or int(precio_producto) <= 0:
            precio_producto = input("\nIngrese el precio del producto.\n\n>> ")

        nuevo_producto: list = agregar_productos(categoria, marca_producto, nombre_producto, int(precio_producto))
        
        if nuevo_producto == False:
            print(f"\n❌ -> No se ha podido agregar el producto {nombre_producto}.")
        else:
            print(f"\n✅ [{nuevo_producto[2]}] -> Se ha agregado el producto {nuevo_producto[1]} {nuevo_producto[3]}. Precio: {nuevo_producto[4]}.")

def modify():
    print("\nBienvenido a la página de productos. Sección [MODIFICAR].\n\nCategorías: \n")
    categorias: list = obtener_categorias()
    print("-> ", categorias[0])
    print("-> ", categorias[1])
    print("-> ", categorias[2])
    print("-> ", categorias[3])
    categoria: str = input("\nIngresa el nombre tal y como está.\n\n>> ")
    
    while categoria not in categorias:
        categoria: str = input("\nIngresa el nombre tal y como está.\n\n>> ")
    
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
            mostrar_productos(productos)

            id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")

            while id_producto.isnumeric() == False or int(id_producto) not in [ids for ids in productos if isinstance(ids, int)]:
                id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")
            
            precio_producto: str = input("\nIngrese el precio del producto.\n\n>> ")

            while precio_producto.isnumeric() == False or int(precio_producto) <= 0:
                precio_producto: str = input("\nIngrese el precio del producto.\n\n>> ")

            producto_modificado = modificar_productos(categoria, marca, int(id_producto), precio_producto, True, tipo_bebida, tipo_alcohol)
            print("\n--------------------")
            print(f"Producto modificado éxitosamente.")
            print(f"ID: {producto_modificado[4]}")
            print(f"Marca: {producto_modificado[3]}")
            print(f"Presentación: {producto_modificado[5]}")
            print(f"Nuevo precio: {precio_producto}")
            print("--------------------")
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
            mostrar_productos(productos)

            id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")

            while id_producto.isnumeric() == False or int(id_producto) not in [ids for ids in productos if isinstance(ids, int)]:
                id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")
            
            precio_producto: str = input("\nIngrese el precio del producto.\n\n>> ")

            while precio_producto.isnumeric() == False or int(precio_producto) <= 0:
                precio_producto: str = input("\nIngrese el precio del producto.\n\n>> ")

            producto_modificado = modificar_productos(categoria, marca, int(id_producto), 1900, True, tipo_bebida)
            print(producto_modificado)
            print("\n--------------------")
            print(f"Producto modificado éxitosamente.")
            print(f"ID: {producto_modificado[3]}")
            print(f"Marca: {producto_modificado[2]}")
            print(f"Presentación: {producto_modificado[4]}")
            print(f"Nuevo precio: {precio_producto}")
            print("--------------------")
    elif categoria == "Carnes":
        productos = obtener_productos(categoria)
        
        print("\nProductos:\n")
        mostrar_productos(productos)

        id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")
        while id_producto.isnumeric() == False or int(id_producto) not in [ids for ids in productos if isinstance(ids, int)]:
            id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")
        
        precio_producto: str = input("\nIngrese el precio del producto.\n\n>> ")
        while precio_producto.isnumeric() == False or int(precio_producto) <= 0:
            precio_producto: str = input("\nIngrese el precio del producto.\n\n>> ")
        
        producto_modificado = modificar_productos(categoria, None, int(id_producto), 1900)
        print("\n--------------------")
        print(f"Producto modificado éxitosamente.")
        print(f"ID: {producto_modificado[1]}")
        print(f"Carne: {producto_modificado[2]}")
        print(f"Nuevo precio: {precio_producto}")
        print("--------------------")
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
        mostrar_productos(productos)

        id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")
        while id_producto.isnumeric() == False or int(id_producto) not in [ids for ids in productos if isinstance(ids, int)]:
            id_producto: str = input("\nIngrese el ID del producto.\n\n>> ")
        
        precio_producto: str = input("\nIngrese el precio del producto.\n\n>> ")
        while precio_producto.isnumeric() == False or int(precio_producto) <= 0:
            precio_producto: str = input("\nIngrese el precio del producto.\n\n>> ")

        producto_modificado = modificar_productos(categoria, marca, int(id_producto), precio_producto)
        print("\n--------------------")
        print(f"Producto modificado éxitosamente.")
        print(f"ID: {producto_modificado[2]}")
        print(f"Marca: {producto_modificado[1]}")
        print(f"Presentación: {producto_modificado[3]}")
        print(f"Nuevo precio: {precio_producto}")
        print("--------------------")
