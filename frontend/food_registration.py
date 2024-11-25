import customtkinter as ctk
from buscar_alimento import BuscarAlimento  # Importa a classe para fazer a busca na API


class FoodRegistration(ctk.CTkFrame):
    def __init__(self, parent, api_key):
        super().__init__(parent)
        self.configure(fg_color="#3D3D3D")
        self.api_key = api_key  # Chave da API
        self.buscar_alimento = BuscarAlimento(api_key)  # Instância da classe de busca

        # Título da aba
        self.title = ctk.CTkLabel(
            self, text="New Meal Registration", font=("Century Gothic", 16, "bold"), text_color="white"
        )
        self.title.pack(pady=10)

        # Campo para o nome da refeição
        self.meal_name_entry = ctk.CTkEntry(self, placeholder_text="Enter meal name", width=306)
        self.meal_name_entry.pack(pady=5, padx=10)

        # Frame para pesquisa de ingredientes (centralizado)
        self.food_search_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.food_search_frame.pack(pady=10, padx=10)

        # Campo de entrada de pesquisa
        self.food_search_entry = ctk.CTkEntry(
            self.food_search_frame,
            placeholder_text="Search for ingredients",
            width=200,
        )
        self.food_search_entry.pack(side="left", padx=(5, 5), pady=5)  # Coloca o campo de entrada à esquerda

        # Botão de pesquisa
        self.food_search_button = ctk.CTkButton(
            self.food_search_frame,
            text="Search",
            fg_color="#2ECC71",
            text_color="white",
            width=100,
            command=self.search_ingredients,
        )
        self.food_search_button.pack(side="left", padx=5, pady=5)  # Posiciona o botão à direita do campo de entrada

        # Associar a tecla Enter ao campo de pesquisa
        self.food_search_entry.bind("<Return>", lambda event: self.search_ingredients())

        # Frame rolável para exibir resultados da pesquisa
        self.search_results_frame = ctk.CTkScrollableFrame(self, fg_color="#5C5C5C", corner_radius=10, height=90)
        self.search_results_frame.pack(padx=10, pady=10, fill="x")

        # Campo e botão para número de ingredientes
        self.ingredient_count_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.ingredient_count_frame.pack(pady=5, padx=10)  # Centraliza o frame na janela principal

        self.ingredient_count_entry = ctk.CTkEntry(
            self.ingredient_count_frame, placeholder_text="Enter number of ingredients", width=200
        )
        self.ingredient_count_entry.pack(side="left", padx=(5, 5), pady=5)

        self.generate_ingredients_button = ctk.CTkButton(
            self.ingredient_count_frame,
            text="Generate",
            command=self.generate_ingredient_fields,
            fg_color="#2ECC71",
            width=100,
        )
        self.generate_ingredients_button.pack(side="left", padx=5, pady=5)

        # Centralização do frame
        self.ingredient_count_frame.pack_configure(anchor="center")

        # Frame rolável para os campos de entrada de ingredientes
        self.ingredients_scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="#5C5C5C", corner_radius=10, width=300, height=10)
        self.ingredients_scrollable_frame.pack(padx=10, pady=(5, 5), fill="x", expand=False)

        # Botão de cadastrar alimento (colocado logo após o frame de ingredientes)
        self.register_meal_button = ctk.CTkButton(
            self,
            text="Register Meal",
            fg_color="#2ECC71",
            width=300,
            height=25,
            command=self.register_meal_action,
        )
        self.register_meal_button.pack(pady=10)

        # Rótulo para mensagens de erro ou sucesso
        self.message_label = ctk.CTkLabel(self, text="", text_color="red", font=("Century Gothic", 12, "italic"))
        self.message_label.pack(pady=5)

        # Lista para armazenar dinamicamente as entradas
        self.ingredient_entries = []

    def search_ingredients(self):
        """Busca alimentos na API e exibe os resultados dinamicamente."""
        query = self.food_search_entry.get()

        # Limpa os resultados anteriores
        for widget in self.search_results_frame.winfo_children():
            widget.destroy()

        if not query.strip():
            return  # Não faz nada se o campo estiver vazio

        alimentos = self.buscar_alimento.encontrar_alimento(query)

        if alimentos is not None:
            alimentos_filtrados = self.buscar_alimento.filtrar_colunas(alimentos)
            if alimentos_filtrados is not None:
                for _, row in alimentos_filtrados.iterrows():
                    food_name = row.get("description", "Unknown Food")
                    self.add_food_result(food_name)
            else:
                self.display_message("No foods found.")
        else:
            self.display_message("Error while searching for foods.")

    def add_food_result(self, food_name):
        """Adiciona um botão representando o alimento encontrado."""
        food_button = ctk.CTkButton(
            self.search_results_frame,
            text=food_name,
            width=280,
            fg_color="#3D3D3D",
            text_color="white",
            hover_color="#555555",
            command=lambda: self.add_to_ingredient_input(food_name),
        )
        food_button.pack(pady=5, padx=5)

    def display_message(self, message, error=True):
        """Exibe uma mensagem no frame."""
        color = "red" if error else "green"
        self.message_label.configure(text=message, text_color=color)

    def generate_ingredient_fields(self):
        """Gera dinamicamente os campos de entrada para os ingredientes."""
        # Limpa campos anteriores
        for widget in self.ingredients_scrollable_frame.winfo_children():
            widget.destroy()
        self.ingredient_entries = []  # Resetar lista de entradas

        try:
            count = int(self.ingredient_count_entry.get())  # Número de ingredientes a serem gerados
            for _ in range(count):
                ingredient_entry = ctk.CTkEntry(
                    self.ingredients_scrollable_frame,
                    placeholder_text="Ingredient",
                    width=250,
                )
                # Centraliza o campo dentro do frame
                ingredient_entry.pack(pady=5, padx=5, anchor="center")
                self.ingredient_entries.append(ingredient_entry)  # Armazena a referência ao campo
        except ValueError:
            self.display_message("Invalid number of ingredients!", error=True)


    def add_to_ingredient_input(self, food_name):
        """Adiciona o alimento selecionado ao próximo campo de ingrediente vazio."""
        for entry in self.ingredient_entries:
            if not entry.get():  # Encontra o próximo campo vazio
                entry.insert(0, food_name)  # Insere o nome do alimento
                break

    def register_meal_action(self):
        """Ação para o botão Register Meal."""
        meal_name = self.meal_name_entry.get().strip()  # Remove espaços em branco
        ingredients = [entry.get() for entry in self.ingredient_entries if entry.get()]

        if not meal_name:  # Verifica se o nome da refeição está vazio
            self.display_message("Meal name cannot be empty!", error=True)
            return  # Impede a continuação da ação

        if not ingredients:  # Verifica se há ao menos um ingrediente
            self.display_message("At least one ingredient is required!", error=True)
            return  # Impede a continuação da ação

        # Caso os dados estejam corretos
        self.display_message(f"Meal '{meal_name}' registered successfully!", error=False)

        print(f"Meal Name: {meal_name}")
        print(f"Ingredients: {ingredients}")
