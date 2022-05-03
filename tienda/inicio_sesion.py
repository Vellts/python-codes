from database import cajeros, administradores

def iniciar_sesion() -> object:
    usuario_encontrado: bool = False
    user: object = {}
    count_to_block: int = 0
    
    while usuario_encontrado == False:
        if (count_to_block > 2):
            user = {"error": "Has excedido el número de intentos. Tu cuenta ha sido bloqueada."}
            break
        else:
            usuario: str = input('\nIngresa el usuario.\n\n>> ')
            contrasena: str = input('\nIngresa la contraseña.\n\n>> ')

            while (len(usuario) < 1):
                usuario: str = input('\nError. Ingresa el usuario.\n\n>> ')
            while (len(contrasena) < 1):
                contrasena: str = input('\nError. Ingresa la contraseña.\n\n>> ')
            
            for i in administradores:
                if (usuario == i["usuario"] and contrasena == i["contrasena"]):
                    user = {
                        'usuario': usuario,
                        'contrasena': contrasena,
                        'is_admin': True,
                    }
                    usuario_encontrado = True
                else:
                    for j in cajeros:
                        if (usuario == j["usuario"] and contrasena == j["contrasena"]):
                            user = {
                                'usuario': usuario,
                                'documento': j["documento"],
                                'contrasena': contrasena,
                                'is_admin': False
                            }
                            usuario_encontrado = True
                    break
            print("\nUsuario o contraseña incorrectos. Ingrese nuevamente.")
            count_to_block += 1 if usuario_encontrado == False else 0
    return user