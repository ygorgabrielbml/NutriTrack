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

        # Lista de comidas com os corações de favoritos
        self.food_list_frame = ctk.CTkScrollableFrame(self, fg_color="#3D3D3D", width=280)
        self.food_list_frame.pack(fill="both", expand=True)

        heart_image_path = os.path.join(os.path.dirname(__file__), "assets", "heart_icon.png")
        self.heart_image = ctk.CTkImage(Image.open(heart_image_path), size=(20, 20))

        for food in ["Yakisoba", "Salad", "Smoothie", "Grilled Chicken"]:
            self.add_food_item(food)

    def add_food_item(self, food_name):
        #Adiciona um item a lista com um botão de favoritos
        food_row = ctk.CTkFrame(self.food_list_frame, fg_color="transparent")
        food_row.pack(fill="x", pady=5)

        food_label = ctk.CTkLabel(food_row, text=food_name, font=("Century Gothic", 14), text_color="white")
        food_label.pack(side="left", padx=5)

        heart_button = ctk.CTkButton(
            food_row, text="", image=self.heart_image, width=30, height=30, fg_color="transparent",
            hover_color="#555555"
        )
        heart_button.pack(side="right", padx=5)
