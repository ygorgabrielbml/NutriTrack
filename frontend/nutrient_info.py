import customtkinter as ctk
import pandas as pd


class NutrientInfo(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#3D3D3D")

        # Título do frame
        self.title_label = ctk.CTkLabel(
            self, text="Nutrient Info", font=("Century Gothic", 18, "bold"), text_color="white"
        )
        self.title_label.pack(pady=10)

        # Frame rolável para os dados de nutrientes
        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="#2D2D2D", corner_radius=10)
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def update_info(self, nutrients):
        """Atualiza a lista de nutrientes exibida no frame, filtrando nutrientes com quantidade maior que 0."""
        # Limpar os dados anteriores
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if nutrients is not None and not nutrients.empty:
            # Filtrar nutrientes com "amount" > 0
            nutrients = nutrients[nutrients["amount"] > 0]

            # Corrigir estrutura dos dados se a coluna "nutrient" existir
            if "nutrient" in nutrients.columns:
                nutrients_expanded = nutrients["nutrient"].apply(pd.Series)  # Expandir os detalhes do nutriente
                nutrients = pd.concat([nutrients, nutrients_expanded], axis=1)  # Concatenar os detalhes

            # Garantir que "name" esteja presente no DataFrame
            if "name" not in nutrients.columns:
                nutrients["name"] = nutrients.get("description", "Unnamed Nutrient")

            for _, row in nutrients.iterrows():
                nutrient_name = row.get("name", "Unnamed Nutrient")  # Obter nome do nutriente
                amount = row.get("amount", "Unknown Amount")  # Obter quantidade do nutriente

                # Frame individual para cada nutriente
                nutrient_row = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
                nutrient_row.pack(fill="x", pady=5)

                # Nome do nutriente
                nutrient_label = ctk.CTkLabel(
                    nutrient_row, text=nutrient_name, font=("Century Gothic", 14), text_color="white"
                )
                nutrient_label.pack(side="left", padx=10)

                # Quantidade do nutriente
                amount_label = ctk.CTkLabel(
                    nutrient_row, text=f"{amount}", font=("Century Gothic", 14), text_color="white"
                )
                amount_label.pack(side="right", padx=10)
        else:
            # Mensagem caso não haja nutrientes
            message_label = ctk.CTkLabel(
                self.scrollable_frame,
                text="No nutrient data available.",
                font=("Century Gothic", 14),
                text_color="white",
            )
            message_label.pack(pady=10)
