import customtkinter as ctk
from login_frame import LoginFrame
from home_frame import HomeScreen
from register_frame import RegisterFrame
from forgot_password_frame import ForgotPasswordFrame
from profile_screen import ProfileScreen
import os


class LoginApp:
    def __init__(self):
        # Configuração inicial
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.assets_dir = os.path.join(self.base_dir, "assets")

        # Configurar a janela principal
        self.app = ctk.CTk()
        self.app.title("NutriTrack")

        # Definir o tamanho fixo da janela
        largura_janela = 600
        altura_janela = 440

        # Centralizar a janela na tela
        largura_tela = self.app.winfo_screenwidth()
        altura_tela = self.app.winfo_screenheight()

        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2

        self.app.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        self.user_data = {
            "name": "John Doe",  # Nome fictício para teste
            "gender": "Male",
            "age": "25",
            "height": "175",
            "weight": "70",
        }

        # Impedir redimensionamento
        self.app.resizable(False, False)

        # Inicializar a tela de login
        self.current_frame = None
        self.show_login_frame()

    def show_login_frame(self):
        """Exibe a tela de login."""
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = LoginFrame(self.app, self)
        self.current_frame.pack(expand=True, fill="both")

    def show_home_frame(self):
        """Exibe a tela de boas-vindas."""
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = HomeScreen(self.app, self)
        self.current_frame.pack(expand=True, fill="both")

    def show_register_frame(self):
        """Exibe a tela de registro."""
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = RegisterFrame(self.app, self)
        self.current_frame.pack(expand=True, fill="both")

    def show_forgot_password_frame(self):
        """Exibe a tela de recuperação de senha."""
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = ForgotPasswordFrame(self.app, self)
        self.current_frame.pack(expand=True, fill="both")
    
    def show_profile_frame(self):
        """Exibe a tela de perfil."""
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = ProfileScreen(self.app, self, self.user_data)
        self.current_frame.pack(expand=True, fill="both")

    def run(self):
        """Inicia o loop principal do aplicativo."""
        self.app.mainloop()

if __name__ == "__main__":
    app = LoginApp()
    app.run()
