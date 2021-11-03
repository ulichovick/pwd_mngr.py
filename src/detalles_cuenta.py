import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import messagebox
from .Cuentas import cuenta
import webbrowser
import os
class Detallescuentas:
    def __init__(
                self,
                ventanaprincipal,
                data_cuenta,
                master_password):
        """
        ventana para crear cuentas nuevas
        """
        self.dir = os.path.abspath(os.getcwd())
        self.data_cuenta = data_cuenta
        self.master_password = master_password
        self.ventana_detalles_cuentas = tk.Toplevel(ventanaprincipal)
        self.ventana_detalles_cuentas.title("Detalles " + data_cuenta[0])
        self.ventana_detalles_cuentas.geometry("300x300")
        self.sep = os.sep
        if os.name == "nt":
            self.dir = self.dir + self.sep + "icons" + self.sep +  "key.ico" 
            self.ventana_detalles_cuentas.iconbitmap(self.dir)
        else:
            self.dir = self.dir + self.sep + "icons" + self.sep +  "key.png" 
            self.img = PhotoImage(file=self.dir)
            self.ventana_detalles_cuentas.wm_iconphoto(True, self.img)
        self.nombre_sitio = ttk.Label(
                                    self.ventana_detalles_cuentas,
                                    text="Nombre sitio:")
        self.nombre_sitio.grid(column=0, row=0)
        self.registra_sitio = tk.StringVar()
        self.entrada_sitio = ttk.Entry(
                                    self.ventana_detalles_cuentas,
                                    width=25,
                                    textvariable=self.registra_sitio)
        self.entrada_sitio.grid(column=1, row=0)
        self.login = ttk.Label(
                                self.ventana_detalles_cuentas,
                                text="Usuario/Mail:")
        self.login.grid(column=0, row=1)
        self.registra_login = tk.StringVar()
        self.entrada_login = ttk.Entry(
                                    self.ventana_detalles_cuentas,
                                    width=25,
                                    textvariable=self.registra_login)
        self.entrada_login.grid(column=1, row=1)
        self.url_sitio = ttk.Label(
                            self.ventana_detalles_cuentas,
                            text="URL sitio:")
        self.url_sitio.grid(column=0, row=2)
        self.registra_url = tk.StringVar()
        self.entrada_url = ttk.Entry(
                                    self.ventana_detalles_cuentas,
                                    width=25,
                                    textvariable=self.registra_url)
        self.entrada_url.grid(column=1, row=2)
        self.pwwd = ttk.Label(
                            self.ventana_detalles_cuentas,
                            text="Contraseña:")
        self.pwwd.grid(column=0, row=3)
        self.registra_pwwd = tk.StringVar()
        self.entrada_pwwd = ttk.Entry(
                                    self.ventana_detalles_cuentas,
                                    width=25,
                                    show="*",
                                    textvariable=self.registra_pwwd)
        self.entrada_pwwd.grid(column=1, row=3)
        self.dir = os.path.abspath(os.getcwd())
        self.dir = self.dir + self.sep+"icons"+self.sep+"show.png"
        self.logo_pwwd = PhotoImage(file = self.dir)
        self.boton_mostrar_pwwd = ttk.Button(
                                            self.ventana_detalles_cuentas,
                                            image=self.logo_pwwd,
                                            width=3,
                                            command=self.mostrar_contras)
        self.boton_mostrar_pwwd.grid(column=2, row=3)
        self.dir = os.path.abspath(os.getcwd())
        self.dir = self.dir + self.sep+"icons"+self.sep+"copy.png"
        self.logo = PhotoImage(file = self.dir)
        self.copiar = ttk.Button(
                                            self.ventana_detalles_cuentas,
                                            text=" ",
                                            width=3,
                                            image=self.logo,
                                            command=self.copiar_clipb)
        self.copiar.grid(column=3, row=3)
        self.boton_borrar = ttk.Button(
                                        self.ventana_detalles_cuentas,
                                        text="Delete this",
                                        command=self.delete_this)
        self.boton_borrar.grid(column=0, row=4)
        self.boton_aceptar = ttk.Button(
                                        self.ventana_detalles_cuentas,
                                        text="Abrir",
                                        command=self.abrir_navegador)
        self.boton_aceptar.grid(column=1, row=4)
        self.boton_guardar = ttk.Button(
                                        self.ventana_detalles_cuentas,
                                        text="Actualizar",
                                        command=self.actualiza_data)
        self.boton_guardar.grid(column=1, row=5)
        self.entrada_sitio.insert(0,self.data_cuenta[0])
        self.entrada_login.insert(0,self.data_cuenta[1])
        self.entrada_url.insert(0,self.data_cuenta[2])
        self.entrada_pwwd.insert(0,self.data_cuenta[3])
        self.ventana_detalles_cuentas.mainloop()

    def actualiza_data(self):
        registra_sitio = str(self.entrada_sitio.get())
        registra_url = str(self.entrada_url.get())
        registra_login = str(self.entrada_login.get())
        registra_pwwd = str(self.entrada_pwwd.get())
        self.id_cuenta = self.data_cuenta[4]
        self.id_usuario = self.data_cuenta[5]
        self.cuenta_nueva = cuenta(
                                self.id_usuario,
                                registra_sitio,
                                registra_url,
                                registra_login,
                                registra_pwwd,
                                self.master_password).modificar_cuenta(self.id_cuenta)
        if self.cuenta_nueva == True:
            self.mensaje_exito = messagebox.showinfo(
                                        title="resultado",
                                        message="¡Actualización realizada con éxito! ",
                                        parent=self.ventana_detalles_cuentas)
            self.ventana_detalles_cuentas.destroy()
        else:
            self.mensaje_exito = messagebox.showwarning(
                                                    title="resultado",
                                                    message="¡Error al realizar la actualización!",
                                                    parent=self.ventana_detalles_cuentas)

    def mostrar_contras(self):
        """
        muestra la contraseña
        """
        self.dir = os.path.abspath(os.getcwd())
        self.dir = self.dir +self.sep+"icons"+self.sep+"hide.png"
        self.logo_show = PhotoImage(file = self.dir)
        self.entrada_pwwd.config(show="")
        self.boton_mostrar_pwwd.config(image=self.logo_show,command=self.ocultar_contras)
    
    def ocultar_contras(self):
        """
        oculta la contraseña
        """
        self.dir = os.path.abspath(os.getcwd())
        self.dir = self.dir + self.sep+"icons"+self.sep+"show.png"
        self.logo_hide = PhotoImage(file = self.dir)
        self.entrada_pwwd.config(show="*")
        self.boton_mostrar_pwwd.config(image=self.logo_hide,command=self.mostrar_contras)
    
    def copiar_clipb(self):
        """
        copia al portapapeles
        """
        self.ventana_detalles_cuentas.clipboard_clear()
        self.ventana_detalles_cuentas.clipboard_append(str(self.registra_pwwd.get()))
        self.msj_confirma_copia = ttk.Label(
                            self.ventana_detalles_cuentas,
                            text="Copiada al portapapeles")
        self.msj_confirma_copia.grid(column=1, row=6)
        self.ventana_detalles_cuentas.after(1000,self.msj_confirma_copia.destroy)
    
    def delete_this(self):
        """
        borra la cuenta actual de la base de datos
        """
        self.id_cuenta = self.data_cuenta[4]
        self.id_usuario = self.data_cuenta[5]
        self.cuenta_nueva = cuenta().borrar_cuentas(
                                                    self.id_cuenta,
                                                    self.id_usuario)
        if self.cuenta_nueva == True:
            self.mensaje_exito = messagebox.showinfo(
                                        title="resultado",
                                        message="¡Se ha borrado la cuenta! ",
                                        parent=self.ventana_detalles_cuentas)
            self.ventana_detalles_cuentas.destroy()
        else:
            self.mensaje_exito = messagebox.showwarning(
                                                    title="resultado",
                                                    message="¡Error al borrar la cuenta!",
                                                    parent=self.ventana_detalles_cuentas)
    
    def abrir_navegador(self):
        """
        abre el link en navegador
        """
        webbrowser.open(str(self.registra_url.get()))
        self.ventana_detalles_cuentas.clipboard_clear()
        self.ventana_detalles_cuentas.clipboard_append(str(self.registra_pwwd.get()))
