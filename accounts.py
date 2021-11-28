from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.stacklayout import StackLayout
from src.Cifrado import Cifrado
from src.Cuentas import Cuenta

class Accounts(StackLayout,Screen):
    """
    Ventana de cuentas
    """

    def custom_constructor(self,id_usu = "", pwwd = "", usuario = "", **kwargs):
        """
        construye la ventana 
        """
        self.master_password = str(pwwd)
        self.id_usuario = str(id_usu)
        self.nom_usu = usuario
        self.label_usu.text = "Cuentas de " + self.nom_usu
        print(self.id_usuario)
        super(Accounts, self).__init__( **kwargs)
        self.data_cuenta = []
        self.boton_cuentas = {}
        self.dibuja_botones()

    def dibuja_botones(self):
        """
        docstring
        """
        self.id_usuario = str(self.id_usuario)
        self.data_cuentas = Cuenta(
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
        if self.info_cuentas is not None:
            for row in self.info_cuentas:
                self.boton_cuentas[self.i] = Button(text=row[0],
                                                    size_hint=(None, None),
                                                    width = 100,
                                                    height = 50
                                                    #command= lambda data=row: self.detallar(data)
                                                    )
                self.add_widget(self.boton_cuentas[self.i])
                self.k = self.k + 1
                self.j = self.j + 1
                if self.j > 2:
                    self.j = 0
                    self.i = self.i + 1
            self.k = 0
        else:
            pass

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Login'
        self.manager.get_screen('Login').resetForm()