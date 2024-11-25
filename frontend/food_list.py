import customtkinter as ctk
from buscar_alimento import BuscarAlimento
import pandas as pd


class FoodList(ctk.CTkFrame):
    def __init__(self, parent, api_key, update_nutrient_callback):
        super().__init__(parent)
        self.configure(fg_color="#3D3D3D")

        self.buscar_alimento = BuscarAlimento(api_key)
        self.update_nutrient_callback = update_nutrient_callback

        # Frame para campo de entrada e botão
        self.search_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.search_frame.pack(fill="x", padx=10, pady=10)

        # Campo de pesquisa
        self.search_entry = ctk.CTkEntry(
            self.search_frame,
            placeholder_text="Search for foods",
            width=250,
            fg_color="#5C5C5C",
            text_color="white",
            border_color="#5C5C5C"
        )
        self.search_entry.pack(side="left", padx=5, pady=10, fill="x", expand=True)

        # Botão de pesquisa
        self.search_button = ctk.CTkButton(
            self.search_frame,
            text="Search",
            fg_color="#2ECC71",
            text_color="white",
            command=self.search_foods
        )
        self.search_button.pack(side="left", padx=5)

        # Associar a tecla Enter ao campo de pesquisa
        self.search_entry.bind("<Return>", lambda event: self.search_foods())

        # Lista de comidas em um frame rolável
        self.food_list_frame = ctk.CTkScrollableFrame(self, fg_color="#3D3D3D", width=280)
        self.food_list_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def search_foods(self):
        """Busca alimentos na API e atualiza a lista dinamicamente."""
        query = self.search_entry.get().strip()

        # Limpa os itens antigos
        for widget in self.food_list_frame.winfo_children():
            widget.destroy()

        if not query:
            self.display_message("Please enter a valid search term.")
            return

        alimentos = self.buscar_alimento.encontrar_alimento(query)

        if alimentos is not None:
            alimentos_filtrados = self.buscar_alimento.filtrar_colunas(alimentos)
            if alimentos_filtrados is not None and not alimentos_filtrados.empty:
                for _, row in alimentos_filtrados.iterrows():
                    food_name = row.get("description", "Unknown Food")
                    fdc_id = row.get("fdcId", None)
                    self.add_food_item(food_name, fdc_id)
            else:
                self.display_message("No foods found.")
        else:
            self.display_message("Error while searching for foods.")

    def add_food_item(self, food_name, fdc_id):
        """Adiciona um item representando um alimento à lista."""
        food_button = ctk.CTkButton(
            self.food_list_frame,
            text=food_name,
            font=("Century Gothic", 14),
            fg_color="#3D3D3D",
            hover_color="#555555",
            text_color="white",
            command=lambda: self.food_action(food_name, fdc_id)
        )
        food_button.pack(fill="x", pady=5, padx=5)

    def display_message(self, message):
        """Exibe uma mensagem no frame de resultados."""
        label = ctk.CTkLabel(self.food_list_frame, text=message, text_color="white")
        label.pack(pady=10)

    def food_action(self, food_name, fdc_id):
        """Ação ao clicar no botão de alimento."""
        nutrients = self.buscar_alimento.buscar_nutrientes(fdc_id)

        # Processar nutrientes para garantir que as colunas necessárias existam
        if nutrients is not None and "nutrient" in nutrients.columns and "amount" in nutrients.columns:
            nutrients_expanded = nutrients["nutrient"].apply(pd.Series)
            nutrients_expanded["amount"] = nutrients["amount"]

            if "unitName" in nutrients.columns:
                nutrients_expanded["unitName"] = nutrients["unitName"]

            nutrients = nutrients_expanded.rename(columns={"name": "name"})
            nutrients = nutrients.dropna(subset=["amount"])  # Remove linhas com valores NaN em 'amount'
            nutrients = nutrients[nutrients["amount"] > 0]  # Apenas nutrientes com valores > 0
        else:
            nutrients = pd.DataFrame()  # Retornar DataFrame vazio em caso de erro

        # Atualizar o NutrientGraph e NutrientInfo
        self.update_nutrient_callback(nutrients)

