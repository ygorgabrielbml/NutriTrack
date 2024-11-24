import customtkinter as ctk
from PIL import Image
import os
import requests


class RegisterFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Caminho para a imagem de fundo
        self.img1_path = os.path.join(controller.assets_dir, "pattern.png")
        self.img1 = ctk.CTkImage(Image.open(self.img1_path), size=(600, 440))

        # Fundo com imagem
        self.background_label = ctk.CTkLabel(self, image=self.img1, text="")
        self.background_label.pack(fill="both", expand=True)

        # Frame central
        self.frame = ctk.CTkFrame(master=self.background_label, width=320, height=450, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        self.title_label = ctk.CTkLabel(master=self.frame, text="Create Account", font=("Century Gothic", 20))
        self.title_label.place(x=50, y=20)

        # Campos de entrada
        self.name_entry = ctk.CTkEntry(master=self.frame, width=220, placeholder_text="Name")
        self.name_entry.place(x=50, y=70)

        self.password_entry = ctk.CTkEntry(master=self.frame, width=220, placeholder_text="Password", show="*")
        self.password_entry.place(x=50, y=110)

        self.confirm_password_entry = ctk.CTkEntry(
            master=self.frame, width=220, placeholder_text="Confirm Password", show="*"
        )
        self.confirm_password_entry.place(x=50, y=150)

        self.weight_entry = ctk.CTkEntry(master=self.frame, width=220, placeholder_text="Weight (kg)")
        self.weight_entry.place(x=50, y=190)

        # Menu suspenso para Gênero
        self.gender_combobox = ctk.CTkComboBox(
            master=self.frame, values=["Male", "Female"], width=220
        )
        self.gender_combobox.set("Select Gender")  # Valor padrão
        self.gender_combobox.place(x=50, y=230)

        self.age_entry = ctk.CTkEntry(master=self.frame, width=220, placeholder_text="Age")
        self.age_entry.place(x=50, y=270)

        self.height_entry = ctk.CTkEntry(master=self.frame, width=220, placeholder_text="Height (cm)")
        self.height_entry.place(x=50, y=310)

        # Botão para registrar
        self.register_button = ctk.CTkButton(
            master=self.frame, width=220, text="Register", corner_radius=6, command=self.register_action
        )
        self.register_button.place(x=50, y=360)

        # Botão para voltar ao login
        self.back_button = ctk.CTkButton(
            master=self.frame, width=220, text="Back to Login", corner_radius=6,
            command=controller.show_login_frame
        )
        self.back_button.place(x=50, y=400)

    def register_action(self):
        """Função para registrar os dados do usuário."""
        api_url = "http://127.0.0.1:5000"
        name = self.name_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        weight = self.weight_entry.get()
        gender = self.gender_combobox.get()
        age = self.age_entry.get()
        height = self.height_entry.get()

        # Validação
        if not all([name, password, confirm_password, weight, gender, age, height]):
            print("Please fill in all the fields!")
        elif gender == "Select Gender":
            print("Please select a valid gender!")
        elif password != confirm_password:
            print("Passwords do not match!")
        else:
            response = requests.post(f"{api_url}/registro", json={"usuario": name, "senha": password, "csenha": confirm_password, "peso": weight, "genero": gender, "idade": age, "altura": height})
            if response.status_code == 200:
                return "usuario registrado com sucesso"
            else:
                return "erro"