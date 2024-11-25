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
        window_width = 1920
        window_height = 1080

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

        # Proporções para altura e largura
        total_height = 0.85  # Altura máxima ocupada
        padding = 0.03  # Espaçamento entre os frames
        half_height = (total_height - padding) / 2  # Altura de cada frame com o espaçamento considerado
        left_right_width = 0.28  # Largura dos frames do lado esquerdo e central
        center_x = 0.37  # Posição central para NutrientInfo e Favorites

        # Frames no lado esquerdo (FoodList e History)
        self.food_list = FoodList(self.main_frame)
        self.food_list.place(relx=0.05, rely=0.05, relwidth=left_right_width, relheight=half_height)

        self.history_frame = ctk.CTkFrame(self.main_frame, fg_color="#2D2D2D")
        self.history_frame.place(relx=0.05, rely=0.05 + half_height + padding, relwidth=left_right_width, relheight=half_height)

        history_label = ctk.CTkLabel(
            self.history_frame, text="History", font=("Century Gothic", 16, "bold"), text_color="white"
        )
        history_label.pack(pady=10)

        # Frames no centro (NutrientInfo e Favorites)
        self.nutrient_info = NutrientInfo(self.main_frame)
        self.nutrient_info.place(relx=center_x, rely=0.05, relwidth=left_right_width, relheight=half_height)

        self.favorites_frame = ctk.CTkFrame(self.main_frame, fg_color="#2D2D2D")
        self.favorites_frame.place(relx=center_x, rely=0.05 + half_height + padding, relwidth=left_right_width, relheight=half_height)

        favorites_label = ctk.CTkLabel(
            self.favorites_frame, text="Favorites", font=("Century Gothic", 16, "bold"), text_color="white"
        )
        favorites_label.pack(pady=10)

        # Frame no lado direito (New Meal Registration)
        self.food_registration = FoodRegistration(self.main_frame)
        self.food_registration.place(relx=0.69, rely=0.05, relwidth=0.26, relheight=total_height)  # Altura total (85%)

    def go_to_profile(self):
        """Abre a tela de perfil."""
        self.controller.show_profile_frame()
