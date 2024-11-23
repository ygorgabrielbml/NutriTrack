import customtkinter as ctk
from PIL import Image
import os


class ForgotPasswordFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Caminho para a imagem de fundo e ícones
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.img1_path = os.path.join(self.base_dir, "assets", "pattern.png")
        self.eye_show_path = os.path.join(self.base_dir, "assets", "eye_show.png")
        self.eye_hide_path = os.path.join(self.base_dir, "assets", "eye_hide.png")

        self.img1 = ctk.CTkImage(Image.open(self.img1_path), size=(600, 440))
        self.eye_show_icon = ctk.CTkImage(Image.open(self.eye_show_path), size=(20, 20))
        self.eye_hide_icon = ctk.CTkImage(Image.open(self.eye_hide_path), size=(20, 20))

        # Fundo com imagem
        self.background_label = ctk.CTkLabel(self, image=self.img1, text="")
        self.background_label.pack(fill="both", expand=True)

        # Frame central
        self.frame = ctk.CTkFrame(master=self.background_label, width=320, height=400, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        self.title_label = ctk.CTkLabel(master=self.frame, text="Reset Password", font=("Century Gothic", 20))
        self.title_label.place(x=50, y=20)

        # Campo de Nome de Usuário
        self.username_entry = ctk.CTkEntry(master=self.frame, width=220, placeholder_text="Username")
        self.username_entry.place(x=50, y=70)

        # Campo de Nova Senha
        self.new_password_entry = ctk.CTkEntry(master=self.frame, width=190, placeholder_text="New Password", show="*")
        self.new_password_entry.place(x=50, y=110)

        # Botão "Mostrar/Ocultar" Nova Senha
        self.new_password_visible = False
        self.new_password_toggle = ctk.CTkButton(
            master=self.frame, image=self.eye_show_icon, text="",
            width=30, height=30, fg_color="transparent", hover_color="#e0e0e0",
            command=lambda: self.toggle_password_visibility(self.new_password_entry, self.new_password_toggle)
        )
        self.new_password_toggle.place(x=245, y=110)

        # Campo para Confirmar Nova Senha
        self.confirm_new_password_entry = ctk.CTkEntry(
            master=self.frame, width=190, placeholder_text="Confirm New Password", show="*"
        )
        self.confirm_new_password_entry.place(x=50, y=150)

        # Botão "Mostrar/Ocultar" Confirmar Nova Senha
        self.confirm_password_visible = False
        self.confirm_password_toggle = ctk.CTkButton(
            master=self.frame, image=self.eye_show_icon, text="",
            width=30, height=30, fg_color="transparent", hover_color="#e0e0e0",
            command=lambda: self.toggle_password_visibility(self.confirm_new_password_entry, self.confirm_password_toggle)
        )
        self.confirm_password_toggle.place(x=245, y=150)

        # Botão para redefinir senha
        self.reset_button = ctk.CTkButton(
            master=self.frame, text="Reset Password", width=220, command=self.reset_password_action
        )
        self.reset_button.place(x=50, y=200)

        # Botão para voltar ao login
        self.back_button = ctk.CTkButton(
            master=self.frame, text="Back to Login", width=220, command=controller.show_login_frame
        )
        self.back_button.place(x=50, y=250)

    def toggle_password_visibility(self, entry, toggle_button):
        """Alterna entre mostrar e ocultar senha para o campo fornecido."""
        if entry.cget("show") == "*":
            entry.configure(show="")
            toggle_button.configure(image=self.eye_hide_icon)
        else:
            entry.configure(show="*")
            toggle_button.configure(image=self.eye_show_icon)

    def reset_password_action(self):
        """Função chamada ao clicar no botão de redefinir senha."""
        username = self.username_entry.get()
        new_password = self.new_password_entry.get()
        confirm_new_password = self.confirm_new_password_entry.get()

        # Validação
        if not username or not new_password or not confirm_new_password:
            print("Please fill in all the fields!")
        elif new_password != confirm_new_password:
            print("Passwords do not match!")
        else:
            print("Password reset successfully!")
            print(f"Username: {username}, New Password: {new_password}")
            # Aqui você pode adicionar lógica para atualizar a senha no banco de dados
