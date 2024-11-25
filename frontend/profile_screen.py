import customtkinter as ctk


class ProfileScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, user_data):
        super().__init__(parent)
        self.controller = controller
        self.user_data = user_data  # Dados do usuário fornecidos ao registrar

        # Configurar a janela
        largura_janela = 600
        altura_janela = 400  # Ajustado para caber até os botões

        largura_tela = parent.winfo_screenwidth()
        altura_tela = parent.winfo_screenheight()

        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2

        parent.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        # Criar o frame principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#2E2E2E", width=largura_janela)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Informações do usuário (alinhadas à esquerda)
        self.create_info_row("Name", self.user_data["name"], 0)
        self.create_info_row("Gender", self.user_data["gender"], 1)
        self.create_info_row("Age", self.user_data["age"], 2)
        self.create_info_row("Height", f"{self.user_data['height']} cm", 3)

        # Peso e IMC
        self.weight_value_label = self.create_info_row("Weight", f"{self.user_data['weight']} kg", 4)
        self.imc_label = self.create_info_row("IMC", self.calculate_imc(), 5)

        # Campo para atualizar o peso
        self.update_weight_label = ctk.CTkLabel(
            self.main_frame, text="Update Weight:", font=("Century Gothic", 15), text_color="#FFFFFF"
        )
        self.update_weight_label.grid(row=6, column=0, padx=20, pady=5, sticky="w")

        self.weight_entry = ctk.CTkEntry(self.main_frame, width=150, justify="center")
        self.weight_entry.insert(0, str(self.user_data["weight"]))
        self.weight_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.save_button = ctk.CTkButton(
            self.main_frame, text="Save", width=80, height=30, command=self.update_weight  # Botão menor
        )
        self.save_button.grid(row=6, column=2, padx=10, pady=5)

        # Mensagem de feedback (alinhada à esquerda)
        self.feedback_label = ctk.CTkLabel(self.main_frame, text="", font=("Century Gothic", 12))
        self.feedback_label.grid(row=7, column=0, columnspan=3, padx=20, pady=5, sticky="w")

        # Botões de navegação
        self.back_button = ctk.CTkButton(
            self.main_frame, text="Back to Home", width=120, height=30, corner_radius=6,
            command=self.controller.show_home_frame
        )
        self.back_button.grid(row=8, column=0, padx=10, pady=10, sticky="w")  # Alinhado à esquerda

        self.logout_button = ctk.CTkButton(
            self.main_frame, text="Logout", width=120, height=30, corner_radius=6,
            command=self.logout_action
        )
        self.logout_button.grid(row=8, column=1, padx=10, pady=10, sticky="w")  # Próximo ao botão Back to Home

    def create_info_row(self, label_text, value_text, row):
        """Cria uma linha estilizada para exibir informações."""
        label = ctk.CTkLabel(
            self.main_frame, text=f"{label_text}:", font=("Century Gothic", 15, "bold"), text_color="#FFFFFF"
        )
        value = ctk.CTkLabel(
            self.main_frame, text=value_text, font=("Century Gothic", 15), text_color="#AAAAAA"
        )
        label.grid(row=row, column=0, padx=20, pady=5, sticky="w")
        value.grid(row=row, column=1, padx=10, pady=5, sticky="w")
        return value

    def calculate_imc(self):
        """Calcula e retorna o IMC formatado."""
        try:
            weight = float(self.user_data["weight"])
            height_m = float(self.user_data["height"]) / 100  # Converter cm para metros
            imc = weight / (height_m ** 2)
            return f"{imc:.2f}"  # Retorna o IMC formatado
        except (ValueError, KeyError, ZeroDivisionError):
            return "Not Available"

    def update_weight(self):
        """Atualiza o peso do usuário e recalcula o IMC."""
        try:
            new_weight = float(self.weight_entry.get())
            self.user_data["weight"] = new_weight

            # Atualizar peso na interface
            self.weight_value_label.configure(text=f"{new_weight} kg")

            # Atualizar IMC
            self.imc_label.configure(text=self.calculate_imc())

            # Exibir mensagem de sucesso
            self.feedback_label.configure(
                text="Weight updated successfully!", text_color="green"
            )
        except ValueError:
            # Exibir mensagem de erro
            self.feedback_label.configure(
                text="Please enter a valid weight.", text_color="red"
            )

    def logout_action(self):
        """Função chamada ao clicar no botão de logout."""
        self.controller.show_login_frame()  # Redireciona para a tela de login
