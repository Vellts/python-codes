import sys, os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])

from src.front.iniciar_sesion import Iniciar_sesion

Iniciar_sesion()