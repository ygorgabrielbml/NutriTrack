import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image


class NutrientGraph(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#3D3D3D")

        # Título
        self.title_label = ctk.CTkLabel(
            self, text="Nutrient Graph", font=("Century Gothic", 18, "bold"), text_color="white"
        )
        self.title_label.pack(pady=10)

        # Área para exibir a imagem do gráfico
        self.graph_frame = ctk.CTkFrame(self, fg_color="#2D2D2D", corner_radius=10)
        self.graph_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.graph_label = ctk.CTkLabel(self.graph_frame, text="", anchor="center")
        self.graph_label.pack(fill="both", expand=True, padx=10, pady=10)

    def update_graph(self, nutrients):
        """Atualiza os dados nutricionais e exibe o gráfico."""
        try:
            print("\nDados recebidos (brutos):")
            print(nutrients)

            if nutrients is not None and isinstance(nutrients, pd.DataFrame) and not nutrients.empty:
                # Processar os dados com pandas
                processed_data = self._process_nutrients(nutrients)
                if not processed_data.empty:
                    # Exibir o gráfico
                    self._create_pie_chart(processed_data)
                else:
                    self.graph_label.configure(text="No valid nutrient data available.", image=None)
            else:
                self.graph_label.configure(text="No nutrient data available.", image=None)
        except Exception as e:
            self.graph_label.configure(text=f"Error processing data: {e}", image=None)

    def _process_nutrients(self, nutrients):
        """Trata os dados de nutrientes para garantir que estejam prontos para o gráfico."""
        try:
            if {"name", "amount"}.issubset(nutrients.columns):
                # Selecionar as colunas relevantes
                nutrients = nutrients[["name", "amount"]]
                nutrients = nutrients.dropna(subset=["amount"])
                nutrients = nutrients[nutrients["amount"] > 1]  # Excluir valores irrelevantes
                nutrients = nutrients.sort_values(by="amount", ascending=False)
                return nutrients

            print("Estrutura de dados não possui colunas esperadas ('name', 'amount').")
            return pd.DataFrame()
        except Exception as e:
            print(f"Erro ao processar nutrientes: {e}")
            return pd.DataFrame()

    def _create_pie_chart(self, nutrients_df):
        """Cria e exibe um gráfico de pizza com os dados nutricionais."""
        try:
            plt.figure(figsize=(6, 6))  # Define o tamanho do gráfico para maior clareza
            nutrients_df = self._combine_small_values(nutrients_df)
            labels = nutrients_df["name"]
            sizes = nutrients_df["amount"]
            colors = plt.cm.Paired.colors

            # Criar gráfico de pizza ajustado
            plt.pie(
                sizes,
                labels=labels,
                autopct=lambda p: f'{p:.1f}%' if p > 5 else '',
                startangle=90,
                colors=colors,
                textprops={'color': "black", 'fontsize': 8},  # Ajuste do tamanho do texto
                radius=0.7,  # Raio reduzido para diminuir o zoom
                labeldistance=1.1,  # Distância dos rótulos
                pctdistance=0.6  # Distância das porcentagens
            )
            plt.title("Nutritional Composition", pad=10, fontsize=12)

            # Ajustar margens do gráfico para garantir centralização
            plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)

            # Converter o gráfico para imagem
            buffer = BytesIO()
            plt.savefig(buffer, format="png", bbox_inches="tight", dpi=150)  # DPI alto para melhor qualidade
            buffer.seek(0)

            # Exibir a imagem como CTkImage
            image = Image.open(buffer)
            chart_image = ctk.CTkImage(dark_image=image, size=(350, 350))  # Tamanho padronizado da imagem

            self.graph_label.configure(image=chart_image, text="")
            self.graph_label.image = chart_image  # Manter a referência

            plt.close()
        except Exception as e:
            self.graph_label.configure(text=f"Error creating chart: {e}", image=None)

    def _combine_small_values(self, nutrients_df):
        """Combina valores pequenos em uma categoria 'Others'."""
        threshold = 5  # Limite de porcentagem para agrupar valores pequenos
        total = nutrients_df["amount"].sum()
        nutrients_df["percentage"] = (nutrients_df["amount"] / total) * 100

        main_nutrients = nutrients_df[nutrients_df["percentage"] > threshold]
        others = nutrients_df[nutrients_df["percentage"] <= threshold]

        if not others.empty:
            others_row = pd.DataFrame({
                "name": ["Others"],
                "amount": [others["amount"].sum()],
                "percentage": [others["percentage"].sum()]
            })
            main_nutrients = pd.concat([main_nutrients, others_row], ignore_index=True)

        return main_nutrients[["name", "amount"]]
