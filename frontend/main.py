import customtkinter as ctk
import os
from login_frame import LoginFrame
from home_screen import HomeScreen
from register_frame import RegisterFrame
from forgot_password_frame import ForgotPasswordFrame
from profile_screen import ProfileScreen
import requests


class Main:
    def __init__(self):
        # Configuração inicial
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.assets_dir = os.path.join(self.base_dir, "assets")
        self.api_key = "HZggsOOEiOiWrnsS5vxzHwgygzuMJm7WHYPV6CIG"  # Adicionado: Chave da API

        # Configurar a janela principal
        self.app = ctk.CTk()
        self.app.title("NutriTrack")

        # self.app.resizable(False, False)

        # Definir o ícone do aplicativo usando wm_iconbitmap
        icon_path = os.path.join(self.assets_dir, "dieta.ico")
        if os.path.exists(icon_path):
            self.app.wm_iconbitmap(icon_path)
        else:
            print(f"Ícone não encontrado: {icon_path}")

        # Inicializar os frames
        self.frames = {}
        self.current_frame = None

        # Criar todos os frames
        self.create_frames()

        # Exibir a tela inicial (Login)
        self.show_frame("login")

    def set_window_size(self, width, height):
        """Define o tamanho da janela, considerando apenas o espaço necessário."""
        # Obter largura e altura total da tela
        largura_tela = self.app.winfo_screenwidth()
        altura_tela = self.app.winfo_screenheight()

        # Calcula posição central
        pos_x = (largura_tela - width) // 2
        pos_y = (altura_tela - height) // 2  # Remove a altura da barra de tarefas aqui

        # Define o tamanho e a posição da janela
        self.app.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

    def create_frames(self):
        """Precarrega todos os frames com tamanhos consistentes."""
        # Frame de Login
        self.frames["login"] = {
            "frame": LoginFrame(self.app, self),
            "width": 600,
            "height": 440
        }
        # Frame de Home com integração da API
        self.frames["home"] = {
            "frame": HomeScreen(self.app, self, self.api_key),  # Adicionado: Chave da API
            "width": 1366,
            "height": 768
        }
        # Frame de Registro
        self.frames["register"] = {
            "frame": RegisterFrame(self.app, self),
            "width": 600,
            "height": 440
        }
        # Frame de Recuperação de Senha
        self.frames["forgot_password"] = {
            "frame": ForgotPasswordFrame(self.app, self),
            "width": 600,
            "height": 440
        }
        # Frame de Perfil
        self.frames["profile"] = {
            "frame": ProfileScreen(self.app, self, {
                "name": "John Doe",
                "gender": "Male",
                "age": "25",
                "height": "175",
                "weight": "70",
            }),
            "width": 500,
            "height": 400
        }

    def show_frame(self, frame_name):
        """Exibe o frame especificado e ajusta a janela."""
        if self.current_frame == frame_name:
            return

        if self.current_frame:
            self.frames[self.current_frame]["frame"].pack_forget()

        frame_data = self.frames[frame_name]
        self.set_window_size(frame_data["width"], frame_data["height"])

        frame_data["frame"].pack(expand=True, fill="both")
        self.current_frame = frame_name

    def show_login_frame(self):
        self.show_frame("login")

    def show_home_frame(self):
        self.show_frame("home")

    def show_register_frame(self):
        self.show_frame("register")

    def show_forgot_password_frame(self):
        self.show_frame("forgot_password")

    def show_profile_frame(self):
        self.show_frame("profile")

    def run(self):
        """Inicia o loop principal do aplicativo."""
        self.app.mainloop()
    


if __name__ == "__main__":
    app = Main()
    app.run()
