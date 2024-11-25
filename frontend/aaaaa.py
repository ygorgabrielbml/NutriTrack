import customtkinter as ctk
import requests

class ProfileScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user_data = self.get_userdata()  # Dados do usuário fornecidos ao registrar

        # Configurar a janela
        largura_janela = 600
        altura_janela = 500

        largura_tela = parent.winfo_screenwidth()
        altura_tela = parent.winfo_screenheight()

        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2

        parent.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        # Título
        self.title_label = ctk.CTkLabel(self, text="Profile", font=("Century Gothic", 30, "bold"))
        self.title_label.pack(pady=20)

        # Criar um frame central para informações do usuário
        self.info_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#333333", width=500)
        self.info_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Exibir informações do usuário em colunas
        self.name_label = self.create_info_label("Name", self.user_data["nome"])
        self.name_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.gender_label = self.create_info_label("Gender", self.user_data["genero"])
        self.gender_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.age_label = self.create_info_label("Age", self.user_data["idade"])
        self.age_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.height_label = self.create_info_label("Height", f"{self.user_data['altura']} cm")
        self.height_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        # Campo para editar peso
        self.weight_label = ctk.CTkLabel(self.info_frame, text="Weight (kg):", font=("Century Gothic", 15))
        self.weight_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        self.weight_entry = ctk.CTkEntry(self.info_frame, width=150, justify="center")
        self.weight_entry.insert(0, str(self.user_data["peso"]))
        self.weight_entry.grid(row=4, column=1, padx=10, pady=10)

        # Botão para salvar o peso atualizado
        self.update_weight_button = ctk.CTkButton(
            self.info_frame, text="Update Weight", width=150, command=self.update_weight, fg_color="#2C7D59"
        )
        self.update_weight_button.grid(row=5, column=1, padx=10, pady=20)

        # Botões de navegação
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        # Botão para voltar à tela principal
        self.back_button = ctk.CTkButton(
            self.button_frame, text="Back to Home", width=150, command=self.controller.show_home_frame
        )
        self.back_button.grid(row=0, column=0, padx=20)

        # Botão para sair da conta
        self.logout_button = ctk.CTkButton(
            self.button_frame, text="Logout", width=150, command=self.logout_action
        )
        self.logout_button.grid(row=0, column=1, padx=20)

    def create_info_label(self, label_text, value_text):
        """Cria uma label estilizada para exibir informações."""
        label = ctk.CTkLabel(self.info_frame, text=f"{label_text}: {value_text}", font=("Century Gothic", 15))
        return label

    def update_weight(self):
        """Atualiza o peso do usuário."""
        try:
            self.update_peso()
            ctk.CTkLabel(
                self.info_frame, text="Weight updated successfully!", font=("Century Gothic", 12), text_color="green"
            ).grid(row=6, columnspan=2, pady=5)
        except ValueError:
            ctk.CTkLabel(
                self.info_frame, text="Please enter a valid weight.", font=("Century Gothic", 12), text_color="red"
            ).grid(row=6, columnspan=2, pady=5)

    def logout_action(self):
        """Função chamada ao clicar no botão de logout."""
        self.controller.show_login_frame()  # Redireciona para a tela de login

    def get_userdata(self):
        api_url = "http://127.0.0.1:5000"
        try:
            # Faz a requisição GET.
            dados_perfil = requests.get(f"{api_url}/perfil/mostrar_infos")
            
            # Verifica o status code
            if dados_perfil.status_code == 200:
                return dados_perfil.json()  # Retorna os dados em formato JSON
            
            else:
                print(f"Erro na API: {dados_perfil.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None

    def update_peso(self):
        api_url = "http://127.0.0.1:5000"
        novo_peso = float(self.weight_entry.get())
        try:
            response = requests.post(f"{api_url}/perfil/mudar_peso", json={"peso": novo_peso})
            if response.status_code == 200:
                mensagem = "peso atualizado"
            else:
                mensagem = "erro"
        except requests.exceptions.RequestException as e:
            print(f"erro: {e}")

