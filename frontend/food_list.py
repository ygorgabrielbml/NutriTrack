import customtkinter as ctk
from PIL import Image
import os


class FoodList(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#3D3D3D")

        # Barra de pesquisa
        self.search_entry = ctk.CTkEntry(
            self, placeholder_text="Search for foods", width=250, height=30, fg_color="#5C5C5C",
            text_color="white", border_color="#5C5C5C"
        )
        self.search_entry.pack(pady=10)

        # Lista de comidas com os botões de coração
        self.food_list_frame = ctk.CTkScrollableFrame(self, fg_color="#3D3D3D", width=280)
        self.food_list_frame.pack(fill="both", expand=True)

        # Carregar imagem do coração
        heart_image_path = os.path.join(os.path.dirname(__file__), "assets", "heart_icon.png")
        self.heart_image = ctk.CTkImage(Image.open(heart_image_path), size=(20, 20))

        # Itens da lista de alimentos
        for food in ["Yakisoba", "Salad", "Smoothie", "Grilled Chicken"]:
            self.add_food_item(food)

    def add_food_item(self, food_name):
        """Adiciona um item como botão e um botão de coração ao lado."""
        food_row = ctk.CTkFrame(self.food_list_frame, fg_color="transparent")
        food_row.pack(fill="x", pady=5)

        # Botão representando o alimento
        food_button = ctk.CTkButton(
            food_row,
            text=food_name,
            font=("Century Gothic", 14),
            fg_color="#3D3D3D",
            hover_color="#555555",
            text_color="white",
            command=lambda: self.food_action(food_name)  # Ação ao clicar no botão
        )
        food_button.pack(side="left", padx=5, fill="x", expand=True)

        # Botão de coração ao lado
        heart_button = ctk.CTkButton(
            food_row,
            text="",
            image=self.heart_image,
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="#555555",
            command=lambda: self.toggle_favorite(food_name)  # Ação ao clicar no coração
        )
        heart_button.pack(side="right", padx=5)

    def food_action(self, food_name):
        """Ação ao clicar no botão de alimento."""
        print(f"Selected food: {food_name}")

    def toggle_favorite(self, food_name):
        """Ação ao clicar no botão de coração."""
        print(f"Favorited: {food_name}")