from tkinter import *
from tkinter import ttk

def simple_popup(self, root, type, msg):
    self.error_popup = Toplevel()
    self.error_popup.geometry(f"300x100+{root.winfo_rootx()}+{root.winfo_rooty()}")
    self.error_popup.title(type)
    self.error_popup.resizable(False,False)
    self.error_popup.grab_set()
    self.error_popup.transient(root)

    self.error_label = ttk.Label(self.error_popup, text=msg).pack(side=TOP)
    self.error_boton = ttk.Button(self.error_popup, text="Aceptar", command=self.error_popup.destroy).pack(side=TOP)
    self.root.wait_window(self.error_popup)
