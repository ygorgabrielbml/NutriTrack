import requests
import customtkinter as ctk


class ByMe(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#3D3D3D")

        # Título do frame
        self.title_label = ctk.CTkLabel(
            self, text="By Me - Created Meals", font=("Century Gothic", 18, "bold"), text_color="white"
        )
        self.title_label.pack(pady=10)

        # Frame rolável para as refeições criadas
        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="#2D2D2D", corner_radius=10)
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Inicializa o callback para remoção de refeições
        self.remove_meal_callback = None

        # Busca inicial das refeições e atualização do frame
        meals = self.get_meals()  # Chama o método para buscar refeições
        self.update_meals(meals)  # Atualiza o frame com as refeições

    def update_meals(self, meals):
        """Atualiza o frame com as refeições criadas pelo usuário."""
        # Limpar os dados anteriores
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if meals:
            for meal in meals:
                # Frame individual para cada refeição
                meal_row = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
                meal_row.pack(fill="x", pady=5)

                # Nome da refeição
                meal_label = ctk.CTkLabel(
                    meal_row, text=meal, font=("Century Gothic", 14), text_color="white"
                )
                meal_label.pack(side="left", padx=10)

                # Botão para excluir a refeição
                delete_button = ctk.CTkButton(
                    meal_row,
                    text="Delete",
                    width=60,
                    fg_color="#FF5555",
                    text_color="white",
                    command=lambda m=meal: self.remove_meal(m),
                )
                delete_button.pack(side="right", padx=10)
        else:
            # Mensagem caso não haja refeições
            message_label = ctk.CTkLabel(
                self.scrollable_frame,
                text="No meals created yet.",
                font=("Century Gothic", 14),
                text_color="white",
            )
            message_label.pack(pady=10)

    def remove_meal(self, meal):
        """Remove uma refeição da lista chamando o callback do controlador."""
        if self.remove_meal_callback:
            self.remove_meal_callback(meal)

    def set_remove_meal_callback(self, callback):
        """Define o callback para remover refeições."""
        self.remove_meal_callback = callback

    def get_meals(self):
        """Busca as refeições criadas na API."""
        api_url = "http://127.0.0.1:5000/by_me_meals"  # URL da API
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                return response.json()  # Retorna a lista de refeições da API
            else:
                print("Erro ao buscar refeições:", response.status_code)
                return []
        except requests.RequestException as e:
            print("Erro ao conectar à API:", e)
            return []

    def refresh_meals(self):
        """Atualiza o frame com as refeições mais recentes."""
        meals = self.get_meals()  # Busca as refeições mais recentes da API
        self.update_meals(meals)  # Atualiza o frame com os dados


