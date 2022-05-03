from datetime import datetime, date
from random import randint
from database import administradores, cajeros

def calcular_edad(fecha):
    try:
        formatear_edad = fecha.split('/') # ['dd', 'mm', 'yyyy']
        edad_a_objeto = date(int(formatear_edad[2]), int(formatear_edad[1]), int(formatear_edad[0]))
        fecha_actual = date.today()
        edad = fecha_actual.year - edad_a_objeto.year -((fecha_actual.month, fecha_actual.day) < (edad_a_objeto.month, edad_a_objeto.day))
        if(edad < 18):
            return { 'status': False }
        elif (edad > 120):
            return { 'status': False }
        return { 'edad': edad, 'status': True }
    except:
        return { 'status': False }


def validar_fecha(fecha):
    baul_fecha: list = []
    edad_calculada: int = 0
    while True:
        if('/' in fecha and len(fecha) < 11):
            if(fecha[2] == '/' and fecha[5] == '/'):
                for i in (range(len(fecha))):
                    if(fecha[i].isnumeric() == True or fecha[i] == '/'):
                        #print(fecha[i])
                        baul_fecha.append(fecha[i])
                        continue
                    elif (fecha[i].isnumeric() == False or fecha[i] != '/'):
                        baul_fecha = []
                        fecha = input('Error. Has ingresado mal la fecha [dd/mm/yyyy]. Ejemplo: 20/02/1998.\n\n>> ')
                        break
                edad_de_baul: str = ''.join(baul_fecha)
                if(edad_de_baul == fecha):
                    obtener_edad = calcular_edad(edad_de_baul)
                    if(obtener_edad['status'] == True):
                        edad_calculada = obtener_edad['edad']
                        break
                    elif (obtener_edad['status'] == False):
                        fecha = input('Error. Has ingresado una fecha inválida. Ejemplo: 20/02/2000.\n\nFecha: ')
                        baul_fecha = []
            else:
                fecha = input('Error. Has ingresado mal la fecha [dd/mm/yyyy]. Ejemplo: 20/02/1998.\n\nFecha: ')
        else:
            fecha = input('Error. Has ingresado mal la fecha [dd/mm/yyyy]. Ejemplo: 20/02/1998.\n\nFecha: ')
    return edad_calculada

def existe_usuario(usuario: str) -> bool:
    existe: bool = False
    for i in administradores:
        if usuario == i["usuario"]:
            existe = True
    for j in cajeros:
        if usuario == j["usuario"]:
            existe = True
    return existe

def is_list(arr: list) -> bool:
    return isinstance(arr, list)

def mostrar_productos(lista: list, with_stock: bool = True) -> None:
#[52, "Whisky 500ml", 2000, 10]
    for i in range(len(lista)):
        previo = lista[i-1] if i > 0 else None
        siguiente = lista[i+1] if i < len(lista) - 1 else None
        siguiente_siguiente = lista[i+2] if i < len(lista) - 2 else None

        if (with_stock):
            if isinstance(lista[i], str) and previo != None and siguiente != None:
                print(f"[{previo}] -> {lista[i]}. ${siguiente} - Stock: {siguiente_siguiente}")
        else:
            if isinstance(lista[i], str) and previo != None and siguiente != None:
                print(f"[{previo}] -> {lista[i]}. ${siguiente}")

def generar_id_factura() -> int:
    return randint(1, 99999)

def fecha_actual() -> list[str]:
    return [f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year}", f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"]