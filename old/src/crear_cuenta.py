import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import messagebox
from .Cuentas import cuenta
import os
class Creacioncuentas:
    def __init__(
                self,
                ventanaprincipal,
                id_usuario,
                password):
        """
        ventana para crear cuentas nuevas
        """
        self.dir = os.path.abspath(os.getcwd())
        self.id_usuario = id_usuario
        self.master_password = password
        self.ventana_crear_cuentas = tk.Toplevel(ventanaprincipal)
        self.ventana_crear_cuentas.title("Registrar nueva cuenta")
        self.ventana_crear_cuentas.geometry("300x300")
        self.sep = os.sep
        if os.name == "nt":
            self.dir = self.dir + self.sep + "icons" + self.sep +  "key.ico" 
            self.ventana_crear_cuentas.iconbitmap(self.dir)
        else:
            self.dir = self.dir + self.sep + "icons" + self.sep +  "key.png"
            self.img = PhotoImage(file=self.dir)
            self.ventana_crear_cuentas.wm_iconphoto(True, self.img)
        self.nombre_sitio = ttk.Label(
                                    self.ventana_crear_cuentas,
                                    text="Nombre sitio:")
        self.nombre_sitio.grid(column=0, row=0)
        self.registra_sitio = tk.StringVar()
        self.entrada_sitio = ttk.Entry(
                                    self.ventana_crear_cuentas,
                                    width=25,
                                    textvariable=self.registra_sitio)
        self.entrada_sitio.grid(column=1, row=0)
        self.url_sitio = ttk.Label(
                                self.ventana_crear_cuentas,
                                text="URL sitio:")
        self.url_sitio.grid(column=0, row=1)
        self.registra_url = tk.StringVar()
        self.entrada_url = ttk.Entry(
                                    self.ventana_crear_cuentas,
                                    width=25,
                                    textvariable=self.registra_url)
        self.entrada_url.grid(column=1, row=1)
        self.login = ttk.Label(
                            self.ventana_crear_cuentas,
                            text="Usuario/Mail:")
        self.login.grid(column=0, row=2)
        self.registra_login = tk.StringVar()
        self.entrada_login = ttk.Entry(
                                    self.ventana_crear_cuentas,
                                    width=25,
                                    textvariable=self.registra_login)
        self.entrada_login.grid(column=1, row=2)
        self.pwwd = ttk.Label(
                            self.ventana_crear_cuentas,
                            text="Contraseña:")
        self.pwwd.grid(column=0, row=3)
        self.registra_pwwd = tk.StringVar()
        self.entrada_pwwd = ttk.Entry(
                                    self.ventana_crear_cuentas,
                                    width=25,
                                    show="*",
                                    textvariable=self.registra_pwwd)
        self.entrada_pwwd.grid(column=1, row=3)
        self.confirma_pwwd = ttk.Label(
                                    self.ventana_crear_cuentas,
                                    text="Confirmar contraseña:")
        self.confirma_pwwd.grid(column=0, row=4)
        self.registra_confirma_pwwd = tk.StringVar()
        self.entrada_confirma_pwwd = ttk.Entry(
                                            self.ventana_crear_cuentas,
                                            width=25,
                                            show="*",
                                            textvariable=self.registra_confirma_pwwd)
        self.entrada_confirma_pwwd.grid(column=1, row=4)
        self.boton_cancelar = ttk.Button(
                                        self.ventana_crear_cuentas,
                                        text="Cancelar",
                                        command=self.ventana_crear_cuentas.destroy)
        self.boton_cancelar.grid(column=0, row=5)
        self.boton_aceptar = ttk.Button(
                                        self.ventana_crear_cuentas,
                                        text="Aceptar",
                                        command=self.verifica_contra)
        self.boton_aceptar.grid(column=1, row=5)
        self.ventana_crear_cuentas.mainloop()

    def verifica_contra(self):
        registra_sitio = str(self.registra_sitio.get())
        registra_url = str(self.registra_url.get())
        registra_login = str(self.registra_login.get())
        registra_pwwd = str(self.registra_pwwd.get())
        confirma_pwwd = str(self.registra_confirma_pwwd.get())
        if registra_pwwd == confirma_pwwd:
            self.cuenta_nueva = cuenta(
                                    self.id_usuario,
                                    registra_sitio,
                                    registra_url,
                                    registra_login,
                                    registra_pwwd,
                                    self.master_password).crear_cuenta()
            self.mensaje_exito = messagebox.showinfo(
                                                    title="resultado",
                                                    message="¡Registro realizado con éxito! "+self.cuenta_nueva,
                                                    parent=self.ventana_crear_cuentas)
            self.ventana_crear_cuentas.destroy()
        else:
            self.mensaje_exito = messagebox.showwarning(
                                                    title="resultado",
                                                    message="¡las contraseñas no coinciden!",
                                                    parent=self.ventana_crear_cuentas)
