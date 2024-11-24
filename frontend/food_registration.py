import customtkinter as ctk


class FoodRegistration(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#3D3D3D")

        # Título da aba
        self.title = ctk.CTkLabel(
            self, text="New Meal Registration", font=("Century Gothic", 16, "bold"), text_color="white"
        )
        self.title.pack(pady=10)

        # Campo para o nome da refeição
        self.meal_name_entry = ctk.CTkEntry(self, placeholder_text="Enter meal name", width=300)
        self.meal_name_entry.pack(pady=5, padx=10)

        # Campo de pesquisa por alimentos
        self.food_search_entry = ctk.CTkEntry(self, placeholder_text="Search for food", width=300)
        self.food_search_entry.pack(pady=5, padx=10)

        self.search_results_frame = ctk.CTkScrollableFrame(self, fg_color="#5C5C5C", corner_radius=10, height=120)
        self.search_results_frame.pack(padx=10, pady=10, fill="x")

        # Exemplo de alimentos pré-carregados
        self.example_foods = ["Yakisoba", "Salad", "Smoothie", "Grilled Chicken", "Pizza Margherita", "Avocado Toast"]

        self.display_food_results()

        # Campo e botão para número de ingredientes
        self.ingredient_count_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.ingredient_count_frame.pack(pady=10, padx=10, fill="x")

        self.ingredient_count_entry = ctk.CTkEntry(
            self.ingredient_count_frame, placeholder_text="Enter number of ingredients", width=200
        )
        self.ingredient_count_entry.pack(side="left", padx=10)

        self.generate_ingredients_button = ctk.CTkButton(
            self.ingredient_count_frame,
            text="Generate",
            command=self.generate_ingredient_fields,
            fg_color="#2ECC71",
            width=100,
        )
        self.generate_ingredients_button.pack(side="left", padx=10)

        # Frame rolável para os campos de entrada de ingredientes
        self.ingredients_scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="#5C5C5C", corner_radius=10, height=120)
        self.ingredients_scrollable_frame.pack(padx=10, pady=10, fill="x")

        # Lista para armazenar dinamicamente as entradas
        self.ingredient_entries = []

    def display_food_results(self):
        """Exibe os alimentos disponíveis na pesquisa."""
        # Limpa resultados anteriores
        for widget in self.search_results_frame.winfo_children():
            widget.destroy()

        # Adiciona os alimentos disponíveis
        for food in self.example_foods:
            food_button = ctk.CTkButton(
                self.search_results_frame,
                text=food,
                width=280,
                fg_color="#3D3D3D",
                text_color="white",
                hover_color="#555555",
                command=lambda f=food: self.add_to_ingredient_input(f),
            )
            food_button.pack(pady=5, padx=5)

    def generate_ingredient_fields(self):
        """Gera dinamicamente os campos de entrada para os ingredientes."""
        # Limpa campos anteriores
        for widget in self.ingredients_scrollable_frame.winfo_children():
            widget.destroy()
        self.ingredient_entries = []  # Resetar lista de entradas

        try:
            count = int(self.ingredient_count_entry.get())
            for _ in range(count):
                ingredient_entry = ctk.CTkEntry(
                    self.ingredients_scrollable_frame, placeholder_text="Ingredient", width=250
                )
                ingredient_entry.pack(pady=5, padx=5, anchor="w")
                self.ingredient_entries.append(ingredient_entry)  # Armazena a referência ao campo
        except ValueError:
            pass

    def add_to_ingredient_input(self, food_name):
        """Adiciona o alimento selecionado ao próximo campo de ingrediente vazio."""
        for entry in self.ingredient_entries:
            if not entry.get():  # Encontra o próximo campo vazio
                entry.insert(0, food_name)  # Insere o nome do alimento
                break
