from tkinter import *
from tkinter import ttk
from util import encontrar_usuario
from src.front.popups.simple_popup import simple_popup

class Iniciar_sesion():
    def __init__(self):
        self.root = Tk()
        self.root.title("Iniciar sesión")
        #self.root.geometry("200x200")
        self.root.resizable(False,False)

        self.usuario = StringVar()
        self.contrasena = StringVar()

        self.marco = ttk.Frame(self.root, padding=(10, 10, 10, 10))
        self.user = ttk.Label(self.marco, text="Usuario:", padding=(5, 5))
        self.passw = ttk.Label(self.marco, text="Contraseña:", padding=(5, 5))

        self.txtuser = ttk.Entry(self.marco, textvariable=self.usuario, width=30)
        self.txtpassw = ttk.Entry(self.marco, textvariable=self.contrasena, show="*", width=30)

        self.btn1 = ttk.Button(self.marco, text="Iniciar sesión", command=self.iniciar_sesion)
        self.btn2 = ttk.Button(self.marco, text="Cancelar", command=self.root.destroy)

        self.marco.grid(column=0, row=0)
        self.user.grid(column=0, row=0)
        self.txtuser.grid(column=1, row=0, columnspan=2)
        self.passw.grid(column=0, row=1)
        self.txtpassw.grid(column=1, row=1, columnspan=2)
        self.btn1.grid(column=1, row=4)
        self.btn2.grid(column=2, row=4)

        self.root.mainloop()
    
    def iniciar_sesion(self):
        usuario = encontrar_usuario(self.usuario.get(), self.contrasena.get())
        if self.usuario.get() == "" or self.contrasena.get() == "":
            simple_popup(self, self.root, "Error", "Te has olvidado de rellenar algún campo.")
        elif usuario == False:
            simple_popup(self, self.root, "Error", "Usuario o contraseña incorrectos")
        # print("Usuario:", self.usuario.get())
        # print("Contraseña:", self.contrasena.get())
        # self.root.destroy()
    
#Iniciar_sesion()