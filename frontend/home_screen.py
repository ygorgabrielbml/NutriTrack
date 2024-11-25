import requests
import customtkinter as ctk
from PIL import Image
import os
from food_list import FoodList
from nutrient_graph import NutrientGraph
from nutrient_info import NutrientInfo
from food_registration import FoodRegistration
from by_me import ByMe


class HomeScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, api_key):
        super().__init__(parent)
        self.controller = controller
        self.api_key = api_key  # Chave da API para os componentes
        self.user_meals = []  # Lista para armazenar as refeições criadas pelo usuário

        # Configurar tamanho da janela
        window_width = 1366
        window_height = 768

        # Obter dimensões da tela e calcular posição central
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        pos_x = (screen_width - window_width) // 2
        pos_y = (screen_height - window_height) // 2
        parent.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

        # Carregar imagem do botão de perfil
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

        # Botão de perfil
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

        # Proporções de layout
        total_height = 0.9  # Altura máxima ocupada
        padding = 0.03  # Espaçamento entre os frames
        half_height = (total_height - padding) / 2  # Altura de cada frame
        left_right_width = 0.28  # Largura dos frames laterais
        center_x = 0.37  # Posição do centro para NutrientGraph e NutrientInfo

        # Frames no lado esquerdo (FoodList e By Me)
        self.food_list = FoodList(self.main_frame, self.api_key, self.update_nutrient_data)
        self.food_list.place(relx=0.05, rely=0.05, relwidth=left_right_width, relheight=half_height)

        self.by_me_frame = ByMe(self.main_frame)
        self.by_me_frame.set_remove_meal_callback(self.remove_meal)
        self.by_me_frame.place(relx=0.05, rely=0.05 + half_height + padding, relwidth=left_right_width, relheight=half_height)

        # Frames no centro (NutrientGraph e NutrientInfo)
        self.nutrient_graph = NutrientGraph(self.main_frame)
        self.nutrient_graph.place(relx=center_x, rely=0.05, relwidth=left_right_width, relheight=half_height)

        self.nutrient_info = NutrientInfo(self.main_frame)
        self.nutrient_info.place(relx=center_x, rely=0.05 + half_height + padding, relwidth=left_right_width, relheight=half_height)

        # Frame no lado direito (New Meal Registration)
        self.food_registration = FoodRegistration(self.main_frame, self.api_key)  # Passa a chave da API aqui
        self.food_registration.place(relx=0.72, rely=0.05, relwidth=0.26, relheight=0.9)  # Altura total
        

    def update_nutrient_data(self, nutrients):
        """Atualiza tanto o gráfico de nutrientes quanto a lista de informações."""
        self.nutrient_graph.update_graph(nutrients)
        self.nutrient_info.update_info(nutrients)

    def add_meal(self, meal):
        """Adiciona uma refeição criada pelo usuário."""
        if meal not in self.user_meals:
            self.user_meals.append(meal)
        self.by_me_frame.update_meals(self.user_meals)

    def remove_meal(self, meal):
        """Remove uma refeição criada pelo usuário."""
        if meal in self.user_meals:
            self.user_meals.remove(meal)
        self.by_me_frame.update_meals(self.user_meals)

    def go_to_profile(self):
        """Abre a tela de perfil."""
        self.controller.show_profile_frame()


