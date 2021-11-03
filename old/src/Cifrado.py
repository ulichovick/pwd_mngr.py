import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Cifrado:
    def __init__(
                self,
                pwwd):
        self.pwwd = pwwd
        self.pwwd = str.encode(self.pwwd)

    def cifrar_contraseñas(self):
        """
        cifra las contraseñas con una sal aleatoria
        """
        self.salt = os.urandom(16)
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        self.key = base64.urlsafe_b64encode(self.kdf.derive(self.pwwd))
        return (self.key,
                self.salt)

    def verificar_cifrado(
                        self,
                        sal):
        """
        cifra el usuario y contraseña con la sal suministrada por el usuario
        PD: insegura, a futuro modificarla
        """
        self.salt = sal
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        self.key = base64.urlsafe_b64encode(self.kdf.derive(self.pwwd))
        return (self.key)

    def cifrado_suave(
                    self,
                    nom_cuenta,
                    login,
                    url,
                    cuenta_pwwd,
                    key):
        """
        cifra data según las credenciales del usuario
        """
        self.key = key
        self.f = Fernet(self.key)
        self.nom_cuenta = nom_cuenta
        self.login = login
        self.url = url
        self.cuenta_pwwd = cuenta_pwwd
        self.nom_cuenta = str.encode(self.nom_cuenta)
        self.login = str.encode(self.login)
        self.url = str.encode(self.url)
        self.cuenta_pwwd = str.encode(self.cuenta_pwwd)
        self.sitio = self.f.encrypt(self.nom_cuenta)
        self.login = self.f.encrypt(self.login)
        self.url = self.f.encrypt(self.url)
        self.password = self.f.encrypt(self.cuenta_pwwd)
        return (self.sitio,
                self.login,
                self.url,
                self.password)

    def descifrado_suave(
                        self,
                        nom_cuenta,
                        login,
                        url,
                        cuenta_pwwd,
                        id_cuenta,
                        id_usuario,
                        key):
        """
        descifra data según las credenciales del usuario
        """
        self.key = key
        self.f = Fernet(self.key)
        self.sitio = nom_cuenta
        self.login = login
        self.url = url
        self.password = cuenta_pwwd
        self.id_cuenta = id_cuenta
        self.id_usuario = id_usuario
        self.nom_cuenta_des = self.f.decrypt(self.sitio)
        self.login_des = self.f.decrypt(self.login)
        self.url_des = self.f.decrypt(self.url)
        self.cuenta_pwwd_des = self.f.decrypt(self.password)
        self.nom_cuenta_des = self.nom_cuenta_des.decode()
        self.login_des = self.login_des.decode()
        self.url_des = self.url_des.decode()
        self.cuenta_pwwd_des = self.cuenta_pwwd_des.decode()
        return (self.nom_cuenta_des,
                self.login_des,
                self.url_des,
                self.cuenta_pwwd_des,
                self.id_cuenta,
                self.id_usuario)
