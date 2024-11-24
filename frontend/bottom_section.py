import customtkinter as ctk


class BottomSection(ctk.CTkFrame):
    def __init__(self, parent, width=1400, height=80):
        # Configure dimensions in the constructor
        super().__init__(parent, width=width, height=height, fg_color="#3D3D3D", corner_radius=10)

        # Adiciona widgets para a BottomSection
        self.history_label = ctk.CTkLabel(
            self, text="History", font=("Century Gothic", 15), text_color="white"
        )
        self.history_label.pack(side="left", padx=20, pady=10)

        self.favorites_label = ctk.CTkLabel(
            self, text="Favorites", font=("Century Gothic", 15), text_color="white"
        )
        self.favorites_label.pack(side="right", padx=20, pady=10)
