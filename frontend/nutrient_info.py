import customtkinter as ctk


class NutrientInfo(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#3D3D3D")

        self.title = ctk.CTkLabel(
            self, text="Nutrients", font=("Century Gothic", 16, "bold"), text_color="white"
        )
        self.title.pack(pady=10)

        self.content = ctk.CTkLabel(
            self, text="Nutrient information will appear here", font=("Century Gothic", 14), text_color="lightgray",
            wraplength=250
        )
        self.content.pack(pady=10)
