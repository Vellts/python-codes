cajeros: list[dict] = [
    {
        "usuario": "Luis Quintana Ruiz",
        "documento": "123456789",
        "edad": "22",
        "contrasena": "123456789Lq*"
    },
    {
        "usuario": "Maria Arboleda Contreras",
        "documento": "987654321",
        "edad": "21",
        "contrasena": "987654321Ma*"
    }
]

administradores: list[dict] = [
    {
        "usuario": "admin",
        "contrasena": "1234"
    }
]

caja: list = [
    #[id_factura, usuario, documento, fecha, hora, id, producto, cantidad, total]
    [26887, 'Luis Quintana Ruiz', '123456789', '18/4/2022', '14:58:35', 52, 'Queso Parmesano Rallado Bolsa', 4, 32000],
    [35522, 'Maria Arboleda Contreras', '987654321', '18/4/2022', '15:9:28', 43, 'Pollo', 2, 8000],
    [35522, 'Maria Arboleda Contreras', '987654321', '18/4/2022', '15:9:28', 44, 'Pechuga', 5, 8000],
    [26887, 'Luis Quintana Ruiz', '123456789', '18/4/2022', '14:58:35', 60, 'Leche entera', 4, 32000],
    [35522, 'Maria Arboleda Contreras', '987654321', '18/4/2022', '15:9:28', 80, 'Carne', 7, 6000],
]

productos: list[str, int] = [
    # Numero para aumentar
    #54,
    # Enlatados [categoria, marca, id, producto, precio, stock]
    ["Enlatados", "Zenu", 1, "Lomos de Atun en Agua", 2000, 10], 
    ["Enlatados", "Zenu", 2, "Salchicha Veina Tradicional", 1800, 10], 
    ["Enlatados", "Zenu", 3, "Chorizo Santarrosano", 2800, 10],
    ["Enlatados", "VanCamp", 4, "Lomos de Atun en Agua", 3000, 10],
    ["Enlatados", "VanCamp", 5, "Sardinas en Salsa de Tomate", 3200, 10],
    ["Enlatados", "VanCamp", 6, "Sardinas en Aceite Vegetal", 3800, 10],
    ["Enlatados", "Taeq", 7, "Palmitos Organicos", 11800, 10],
    ["Enlatados", "Taeq", 8, "Palmitos Arvejas y Zanahoria Bajas en Sodio", 4400, 10],
    ["Enlatados", "Taeq", 9, "Arvejas Bajas en Sodio", 4600, 10],
    # Bebidas-Alcoholicas [categoria, tipo-alcohol, marca, id, producto, precio, stock]
    ["Bebidas", "Alcoholica", "Cerveza", "Budweiser", 10, "Lata 269ml", 4000, 10],
    ["Bebidas", "Alcoholica", "Cerveza", "Budweiser", 11, "Botella 250ml", 500, 10],
    ["Bebidas", "Alcoholica", "Cerveza", "Budweiser", 12, "Botella 355ml", 4000, 10],
    ["Bebidas", "Alcoholica", "Cerveza", "Aguila", 13, "Lata 330ml", 4000, 10],
    ["Bebidas", "Alcoholica", "Cerveza", "Aguila", 14, "Ligth Lata 330ml", 3000, 10],
    ["Bebidas", "Alcoholica", "Cerveza", "Aguila", 15, "Retornable 750ml", 4500, 10],
    ["Bebidas", "Alcoholica", "Cerveza", "Club Colombia", 16, "Negra Lata 330ml", 4000, 10],
    ["Bebidas", "Alcoholica", "Cerveza", "Club Colombia", 17, "Roja Lata 330ml", 3000, 10],
    ["Bebidas", "Alcoholica", "Cerveza", "Club Colombia", 18, "Negra Botella 330ml", 4000, 10],
    ["Bebidas", "Alcoholica", "Vino", "Las Moras", 19, "Vino Tinto Malbec 750ml", 12000, 10],
    ["Bebidas", "Alcoholica", "Vino", "Las Moras", 20, "Vino Tinto Bornarda 750ml", 14000, 10],
    ["Bebidas", "Alcoholica", "Vino", "Las Moras", 21, "Vino Tinto Reserva 750ml", 15000, 10],
    ["Bebidas", "Alcoholica", "Vino", "Calvet", 22, "Vino Blanco Celebration Brut 750ml", 20000, 10],
    ["Bebidas", "Alcoholica", "Vino", "Calvet", 23, "Vino Rose Celebration Brut 750ml", 30000, 10],
    ["Bebidas", "Alcoholica", "Vino", "Calvet", 24, "Vino Rosado D Anjou Cabernet Franc 750ml", 40000, 10],
    ["Bebidas", "Alcoholica", "Vino", "Leyda", 25, "Vino Tinto Pinot Noir 750ml", 20000, 10],
    ["Bebidas", "Alcoholica", "Vino", "Leyda", 26, "Vino Tinto Pinot Noir Reserva 750ml", 22000, 10],
    ["Bebidas", "Alcoholica", "Vino", "Leyda", 27, "Vino Blanco Sauvignon Blanc Reserva 750ml", 25000, 10],
    ["Bebidas", "Alcoholica", "Whisky", "Buchanans", 28, "Deluxe 12 Años 750ml", 70000, 10],
    ["Bebidas", "Alcoholica", "Whisky", "Buchanans", 29, "18 Años 750ml", 80000, 10],
    ["Bebidas", "Alcoholica", "Whisky", "Buchanans", 30, "Red Seal 750ml", 90000, 10],
    ["Bebidas", "Alcoholica", "Whisky", "Glenlivet", 31, "Caps Reserva 700ml", 60000, 10],
    ["Bebidas", "Alcoholica", "Whisky", "Glenlivet", 32, "Founders Reserva 700ml", 70000, 10],
    ["Bebidas", "Alcoholica", "Whisky", "Glenlivet", 33, "12 Años 700ml", 80000, 10],
    ["Bebidas", "Alcoholica", "Whisky", "Old Parr", 34, "12 Años 750ml", 90000, 10],
    ["Bebidas", "Alcoholica", "Whisky", "Old Parr", 35, "18 Años 750ml", 100000, 10],
    ["Bebidas", "Alcoholica", "Whisky", "Old Parr", 36, "12 Años Media 500ml", 45000, 10],
    # Bebidas-Gaseosas [categoria, tipo-bebida, marca, id, producto, precio, stock]
    ["Bebidas", "Gaseosa", "Coca-Cola", 37, "Zero 355ml", 5000, 10],
    ["Bebidas", "Gaseosa", "Coca-Cola", 38, "600ml", 3000, 10],
    ["Bebidas", "Gaseosa", "Coca-Cola", 39, "Lata 330ml", 2000, 10],
    ["Bebidas", "Gaseosa", "Pepsi", 40, "Lata 269ml", 1500, 10],
    ["Bebidas", "Gaseosa", "Pepsi", 41, "Pet 1.5l", 2000, 10],
    ["Bebidas", "Gaseosa", "Pepsi", 42, "Pet 2l", 3500, 10],
    # Carnes [categoria, id, producto, kg, precio_por_kg]
    ["Carnes", 43, "Pollo", 2000, 10],
    ["Carnes", 44, "Res", 2100, 10],
    ["Carnes", 45, "Pescado", 4000, 10],
    # Lacteos [categoria, marca, id, producto, precio, stock]
    ["Lacteos", "Taeq", 46, "Jamon de Pavo", 15000, 10],
    ["Lacteos", "Taeq", 47, "Queso Mozzarella Tajado", 11000, 10],
    ["Lacteos", "Taeq", 48, "Salchicha de Pavo", 12000, 10],
    ["Lacteos", "Alqueria", 49, "Queso", 10000, 10],
    ["Lacteos", "Alqueria", 50, "Leche Deslactosada", 5000, 10],
    ["Lacteos", "Alqueria", 51, "Crema de Leche Semi-Entera", 7000, 10],
    ["Lacteos", "Alpina", 52, "Queso Parmesano Rallado Bolsa", 8000, 10],
    ["Lacteos", "Alpina", 53, "Leche Entera", 5000, 10],
    ["Lacteos", "Alpina", 54, "Kumis Original Bolsa", 3000, 10]
]