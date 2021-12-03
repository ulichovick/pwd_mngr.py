from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.stacklayout import StackLayout

class Details(StackLayout,Screen):
    """
    Ventana de detalles de cuentas
    """

    def __init__(self, **kwargs):
        super(Details, self).__init__( **kwargs)

    def custom_construct(self, data, **kwargs):
        """
        construye la ventana 
        """
        self.label_cuenta.text = "Detalles de " + data[0]

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Accounts'
        self.manager.get_screen('Accounts')
