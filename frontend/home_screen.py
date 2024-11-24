import customtkinter as ctk
from PIL import Image
import os
from food_list import FoodList
from nutrient_info import NutrientInfo
from food_registration import FoodRegistration


class HomeScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configurar tamanho da janela
        window_width = 1400
        window_height = 900  # Altura aumentada para acomodar os frames quadrados

        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()

        pos_x = (screen_width - window_width) // 2
        pos_y = (screen_height - window_height) // 2

        parent.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

        # Carregar imagem para o botão de perfil
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.profile_image_path = os.path.join(self.base_dir, "assets", "profile_icon.png")
        self.profile_image = ctk.CTkImage(
            dark_image=Image.open(self.profile_image_path), size=(40, 40)
        )

        # Adicionar widgets à tela
        self.create_widgets()

    def create_widgets(self):
        """Cria os widgets principais."""
        # Header
        self.header_frame = ctk.CTkFrame(self, height=60, fg_color="#3D3D3D", corner_radius=0)
        self.header_frame.pack(side="top", fill="x")

        self.header_label = ctk.CTkLabel(
            self.header_frame, text="NutriTrack", font=("Century Gothic", 20, "bold"), text_color="white"
        )
        self.header_label.pack(side="left", padx=20, pady=10)

        # Botão de perfil com estilo redondo e imagem
        self.profile_button = ctk.CTkButton(
            self.header_frame,
            text="",
            width=40,
            height=40,
            fg_color="transparent",
            hover_color="#777777",
            corner_radius=20,
            command=self.go_to_profile,
            image=self.profile_image,
        )
        self.profile_button.pack(side="right", padx=20, pady=10)

        # Corpo principal
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Componentes principais
        self.food_list = FoodList(self.main_frame)
        self.food_list.place(relx=0.05, rely=0.05, relwidth=0.3, relheight=0.75)

        self.nutrient_info = NutrientInfo(self.main_frame)
        self.nutrient_info.place(relx=0.37, rely=0.05, relwidth=0.3, relheight=0.75)

        self.food_registration = FoodRegistration(self.main_frame)
        self.food_registration.place(relx=0.69, rely=0.05, relwidth=0.26, relheight=0.75)

        # Bottom section (Historico e favoritos)
        self.history_frame = ctk.CTkFrame(self.main_frame, fg_color="#3D3D3D", corner_radius=10)
        self.history_frame.place(relx=0.05, rely=0.85, relwidth=0.4, relheight=0.15)

        self.history_label = ctk.CTkLabel(
            self.history_frame, text="History", font=("Century Gothic", 18, "bold"), text_color="white"
        )
        self.history_label.pack(pady=10)

        self.favorites_frame = ctk.CTkFrame(self.main_frame, fg_color="#3D3D3D", corner_radius=10)
        self.favorites_frame.place(relx=0.55, rely=0.85, relwidth=0.4, relheight=0.15)

        self.favorites_label = ctk.CTkLabel(
            self.favorites_frame, text="Favorites", font=("Century Gothic", 18, "bold"), text_color="white"
        )
        self.favorites_label.pack(pady=10)

    def go_to_profile(self):
        """Abre a tela de perfil."""
        self.controller.show_profile_frame()
