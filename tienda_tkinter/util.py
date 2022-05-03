from src.back.database import administradores

def encontrar_usuario(usuario: str, contrasena: str) -> bool:
    for i in administradores:
        if i[0] == usuario and i[1] == contrasena:
            return True
    return False