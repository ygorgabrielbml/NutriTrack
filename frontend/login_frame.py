import customtkinter as ctk
from PIL import Image
import os
import requests

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        # Carregar imagens
        self.img1_path = os.path.join(controller.assets_dir, "pattern.png")
        self.img1 = ctk.CTkImage(Image.open(self.img1_path), size=(600, 440))

        self.eye_icon_show_path = os.path.join(controller.assets_dir, "eye_show.png")
        self.eye_icon_hide_path = os.path.join(controller.assets_dir, "eye_hide.png")
        self.eye_icon_show = ctk.CTkImage(Image.open(self.eye_icon_show_path), size=(20, 20))
        self.eye_icon_hide = ctk.CTkImage(Image.open(self.eye_icon_hide_path), size=(20, 20))

        # Fundo com imagem
        self.background_label = ctk.CTkLabel(self, image=self.img1, text="")
        self.background_label.pack(fill="both", expand=True)

        # Criar o frame central
        self.frame = ctk.CTkFrame(master=self.background_label, width=320, height=360, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        self.title_label = ctk.CTkLabel(master=self.frame, text="Log into your Account", font=("Century Gothic", 20))
        self.title_label.place(x=50, y=45)

        # Entradas
        self.username_entry = ctk.CTkEntry(master=self.frame, width=220, placeholder_text="Username")
        self.username_entry.place(x=50, y=110)

        self.password_entry = ctk.CTkEntry(master=self.frame, width=185, placeholder_text="Password", show="*")
        self.password_entry.place(x=50, y=165)

        # Botão "Olho" para visualizar a senha
        self.show_password = False  # Estado inicial: senha oculta
        self.eye_button = ctk.CTkButton(
            master=self.frame, image=self.eye_icon_show, text="",
            width=30, height=30, fg_color="transparent", hover_color="#e0e0e0",
            command=self.toggle_password_visibility
        )
        self.eye_button.place(x=240, y=165)

       # Botão "Esqueceu a senha?"
        self.forgot_button = ctk.CTkButton(
        master=self.frame, text="Forget password?", font=("Century Gothic", 12),
        width=120, height=25, fg_color="transparent",
        command=controller.show_forgot_password_frame  # Redireciona para a tela de recuperação
    )
        self.forgot_button.place(x=155, y=195)


        # Botão de Login
        self.login_button = ctk.CTkButton(
            master=self.frame, width=220, text="Login", corner_radius=6, command=self.fazer_login
        )
        self.login_button.place(x=50, y=240)

        # Botão de Registro
        self.register_button = ctk.CTkButton(
            master=self.frame, width=220, text="Register", corner_radius=6,
            command=controller.show_register_frame
        )
        self.register_button.place(x=50, y=290)

    def toggle_password_visibility(self):
        """Alterna entre exibir e ocultar a senha."""
        if self.show_password:
            self.password_entry.configure(show="*")
            self.eye_button.configure(image=self.eye_icon_show)
        else:
            self.password_entry.configure(show="")
            self.eye_button.configure(image=self.eye_icon_hide)
        self.show_password = not self.show_password

    def forgot_password_action(self):
        """Função chamada ao clicar em 'Esqueceu a senha?'."""
        print("Esqueceu a senha foi clicado!")

    def fazer_login(self):
        api_url = "http://127.0.0.1:5000"
        nome = self.username_entry.get()
        senha = self.password_entry.get()
        response = requests.post(f"{api_url}/login", json={"usuario": nome, "senha": senha})
        if response.status_code == 200:
            self.controller.show_home_frame()