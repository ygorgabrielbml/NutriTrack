import customtkinter as ctk
from PIL import Image, ImageTk
import os
from tkinter import messagebox


class HomeScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configurar tamanho da janela ligeiramente maior
        largura_janela = 1240  # Largura maior que o padrão
        altura_janela = 720  # Altura maior que o padrão

        # Centralizar a janela
        largura_tela = self.controller.app.winfo_screenwidth()
        altura_tela = self.controller.app.winfo_screenheight()

        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2

        self.controller.app.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        # Caminho para a imagem do botão
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.profile_image_path = os.path.join(self.base_dir, "assets", "profile_icon.png")
        self.profile_image = ctk.CTkImage(Image.open(self.profile_image_path), size=(40, 40))

        # Header com botão circular
        self.header_frame = ctk.CTkFrame(self, height=50, fg_color="#333333", corner_radius=0)
        self.header_frame.pack(side="top", fill="x")

        self.header_label = ctk.CTkLabel(
            self.header_frame, text="NutriTrack", font=("Century Gothic", 18), text_color="white"
        )
        self.header_label.pack(side="left", padx=20, pady=10)

        self.profile_button = ctk.CTkButton(
            self.header_frame, text="", width=40, height=40, fg_color="transparent",
            hover_color="#777777", corner_radius=20, command=self.go_to_profile,
            image=self.profile_image
        )
        self.profile_button.pack(side="right", padx=20, pady=5)

        # Conteúdo principal
        self.title_label = ctk.CTkLabel(
            master=self, text="Welcome to NutriTrack", font=("Century Gothic", 30), anchor="center"
        )
        self.title_label.pack(pady=30)

        # Campo de pesquisa
        self.search_entry = ctk.CTkEntry(master=self, width=400, placeholder_text="Search for food items")
        self.search_entry.pack(pady=10)

        self.search_button = ctk.CTkButton(
            master=self, text="Search", command=self.search_food, width=200
        )
        self.search_button.pack(pady=10)

        # Botão para exibir histórico
        self.history_button = ctk.CTkButton(
            master=self, text="View History", command=self.show_history, width=200
        )
        self.history_button.pack(pady=20)

        # Botão para exibir gráfico
        self.graph_button = ctk.CTkButton(
            master=self, text="View Graph", command=self.show_graph, width=200
        )
        self.graph_button.pack(pady=20)

    def search_food(self):
        """Função chamada ao clicar em 'Search'."""
        search_term = self.search_entry.get()
        if search_term:
            messagebox.showinfo("Search", f"Searching for: {search_term}")
            # Aqui você pode adicionar a lógica de busca usando APIs
        else:
            messagebox.showwarning("Input Error", "Please enter a food item to search!")

    def show_history(self):
        """Função chamada ao clicar em 'View History'."""
        messagebox.showinfo("History", "Displaying food search history...")
        # Aqui você pode adicionar lógica para exibir o histórico

    def show_graph(self):
        """Função chamada ao clicar em 'View Graph'."""
        messagebox.showinfo("Graph", "Displaying food consumption graph...")
        # Aqui você pode adicionar lógica para exibir gráficos

    def go_to_profile(self):
        """Função chamada ao clicar no botão de perfil."""
        self.controller.show_profile_frame()
