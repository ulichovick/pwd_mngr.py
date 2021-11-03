import os
from .detalles_cuenta import Detallescuentas
import tkinter as tk
from tkinter import PhotoImage, ttk
from .Cuentas import cuenta
from .Cifrado import Cifrado
from .crear_cuenta import Creacioncuentas

class index:
    """
    dibuja la ventana de las cuentas,
    que al serr clickeado el boton mostrara un popup con la data de las cuentas
    """
    def __init__(
                self,
                id_usuario,
                password,
                nom_usu):
        self.dir = os.path.abspath(os.getcwd())
        print(self.dir)
        self.id_usuario = id_usuario
        self.master_password = password
        self.nombre_usuario = nom_usu
        self.data_cuenta = []
        self.data = []
        self.boton_cuentas = {}
        self.ventana_cuentas = tk.Tk()
        self.titulo = "Cuentas: " + self.nombre_usuario
        self.ventana_cuentas.title(self.titulo)
        self.ventana_cuentas.geometry("250x250")
        self.sep = os.sep
        if os.name == "nt":
            self.dir = self.dir + self.sep + "icons" + self.sep +  "key.ico" 
            self.ventana_cuentas.iconbitmap(self.dir)
        else:
            self.dir = self.dir + self.sep + "icons" + self.sep +  "key.png"
            self.img = PhotoImage(file=self.dir)
            self.ventana_cuentas.wm_iconphoto(True, self.img)
        self.frame_ops = ttk.Frame()
        self.frame_ops.grid(column=0, row=0)
        self.labelframe_operaciones = ttk.LabelFrame(self.frame_ops,text="Operaciones:")
        self.labelframe_operaciones.grid(column=1, row=0)
        self.crear_cuentas = ttk.Button(self.labelframe_operaciones,
                                        text="Nueva Cuenta",
                                        command=self.dibuja_creacuentas)
        self.crear_cuentas.grid(column=0, row=0)
        self.actualizar = ttk.Button(self.labelframe_operaciones,
                                        text="Actualizar Ventana",
                                        command=self.refresh)
        self.actualizar.grid(column=1, row=0)
        self.dibuja_botones()
        self.ventana_cuentas.mainloop()

    def dibuja_botones(self):
        """
        dibuja dinamicamente los botones de las cuentas
        """
        self.master_password = str(self.master_password)
        self.id_usuario = str(self.id_usuario)
        self.data_cuentas = cuenta(
                                master_password=self.master_password,
                                id_usuario=self.id_usuario).verificar_cuentas()
        for row in self.data_cuentas:
            sal = row[4]
            self.cifrado = Cifrado(self.master_password)
            cifrado_pass = self.cifrado.verificar_cifrado(sal)
            self.data_cuenta.append(self.cifrado.descifrado_suave(
                                                                row[0],
                                                                row[1],
                                                                row[2],
                                                                row[3], 
                                                                row[5],
                                                                row[6],
                                                                cifrado_pass))
        self.info_cuentas = self.data_cuenta
        self.i = 1
        self.j = 0
        self.k = 0
        self.frame = ttk.Frame(self.ventana_cuentas)
        self.frame.grid(column=0, row=1)
        if self.info_cuentas is not None:
            self.labelframe_cuentas = ttk.LabelFrame(self.frame,text="Cuentas")
            self.labelframe_cuentas.grid(column=0,row=1)
            for row in self.info_cuentas:
                self.labelframe_cuenta = ttk.LabelFrame(self.labelframe_cuentas)
                self.labelframe_cuenta.grid(column=self.j,row=self.i)
                self.boton_cuentas[self.i] = ttk.Button(self.labelframe_cuenta,
                                                            text=row[0],
                                                            command= lambda data=row: self.detallar(data))
                self.boton_cuentas[self.i].grid(column=0, row=0)
                self.k = self.k + 1
                self.j = self.j + 1
                if self.j > 2:
                    self.j = 0
                    self.i = self.i + 1
            self.k = 0
        else:
            pass

    def dibuja_creacuentas(self):
        self.cuenta = Creacioncuentas(
                                    self.ventana_cuentas,
                                    self.id_usuario,
                                    self.master_password)
        return self.cuenta

    def refresh(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.data_cuenta.clear()
        self.frame.grid_forget()
        self.dibuja_botones()

    def detallar(self,data):
        """
        abre una nueva ventana con los detalles de la cuenta
        """
        self.data = data
        self.detalles = Detallescuentas(
                                        self.ventana_cuentas,
                                        self.data,
                                        self.master_password)
        self.data_cuenta.clear()
