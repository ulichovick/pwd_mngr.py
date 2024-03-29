from kivy.app import App
from kivy.core.window import Window
from kivy.lang import builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.stacklayout import StackLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from src.usuarios import Usuario
from accounts import Accounts
from details import Details
import kivy

Window.size = (400, 500)

class MyRoot(TabbedPanel, StackLayout,Screen):

    def verifica_usuario(self):
        usuario = self.entra_usr.text
        contra = self.entra_pwwd.text
        self.resultado = Usuario(usuario, contra).verificar_usuario()
        if self.resultado is not None:
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'Accounts'
            self.manager.get_screen('Accounts').custom_constructor(id_usu = self.resultado,pwwd = contra, usuario = usuario)
        else:
            popup = Popup(title='Error',
                content=Label(text='Usuario inexistente o contraseña incorrecta'),
                size_hint=(None, None), size=(400, 400))
            popup.open()
            self.entra_usr.text = ""
            self.entra_pwwd.text = ""

class Fuck(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(MyRoot(name='Login'))
        manager.add_widget(Accounts(name='Accounts'))
        manager.add_widget(Details(name='Details'))
        return manager

if __name__ == '__main__':
    fuck = Fuck()
    fuck.run()
