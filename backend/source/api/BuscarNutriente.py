import requests
import pandas as pd
import customtkinter as ctk
from BuscarAlimento import BuscarAlimento

class BuscarNutriente:
    def __init__(self, api_key, details_url="https://api.nal.usda.gov/fdc/v1/food"):
        self.api_key = api_key
        self.details_url = details_url

    def pegar_nutrientes(self, fdc_id):
        params = {"api_key": self.api_key}
        try:
            response = requests.get(url=f"{self.details_url}/{fdc_id}", params=params)
            response.raise_for_status()
            dados = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None

        dados_nutrientes = dados.get("foodNutrients", [])
        if not dados_nutrientes:
            print("Nenhum dado nutricional encontrado para este alimento.")
            return None

        nutrientes_df = pd.DataFrame(dados_nutrientes)
        return nutrientes_df

    def filtrar_colunas(self, nutrientes_df):
        colunas_desejadas = ["name", "amount", "unitName"]

        if "nutrient" in nutrientes_df.columns and "amount" in nutrientes_df.columns:
            nutrientes_processados = nutrientes_df["nutrient"].apply(pd.Series)
            nutrientes_processados["amount"] = nutrientes_df["amount"]
            nutrientes_processados = nutrientes_processados[colunas_desejadas]
            return nutrientes_processados
        else:
            print("Estrutura inesperada de dados nutricionais.")
            return None


class App(ctk.CTk):
    def __init__(self, api_key):
        super().__init__()
        self.title("Consulta Nutricional")
        self.geometry("600x400")
        self.api_key = api_key
        self.buscar_alimento = BuscarAlimento(api_key=self.api_key)
        self.buscar_nutriente = BuscarNutriente(api_key=self.api_key)

        # Widgets
        self.label = ctk.CTkLabel(self, text="Pesquise por um alimento (em inglês):")
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="Ex: Apple")
        self.entry.pack(pady=10)

        self.search_button = ctk.CTkButton(self, text="Buscar Alimentos", command=self.buscar_alimentos)
        self.search_button.pack(pady=10)

        self.results_frame = ctk.CTkFrame(self)
        self.results_frame.pack(pady=20, fill="both", expand=True)

    def buscar_alimentos(self):
        nome_alimento = self.entry.get()
        alimentos = self.buscar_alimento.encontrar_alimento(nome_alimento)

        for widget in self.results_frame.winfo_children():
            widget.destroy()

        if alimentos is not None:
            alimentos_filtrados = self.buscar_alimento.filtrar_colunas(alimentos)

            if alimentos_filtrados is not None:
                for index, row in alimentos_filtrados.iterrows():
                    alimento_button = ctk.CTkButton(
                        self.results_frame,
                        text=row["description"],
                        command=lambda fdc_id=row["fdcId"]: self.mostrar_nutrientes(fdc_id)
                    )
                    alimento_button.pack(pady=5, fill="x")
            else:
                ctk.CTkLabel(self.results_frame, text="Nenhum dado filtrado encontrado.").pack(pady=10)
        else:
            ctk.CTkLabel(self.results_frame, text="Nenhum alimento encontrado.").pack(pady=10)

    def mostrar_nutrientes(self, fdc_id):
        nutrientes_df = self.buscar_nutriente.pegar_nutrientes(fdc_id)

        if nutrientes_df is not None:
            nutrientes_processados = self.buscar_nutriente.filtrar_colunas(nutrientes_df)

            if nutrientes_processados is not None:
                for widget in self.results_frame.winfo_children():
                    widget.destroy()

                for _, row in nutrientes_processados.iterrows():
                    texto = f"{row['name']}: {row['amount']} {row['unitName']}"
                    ctk.CTkLabel(self.results_frame, text=texto).pack(pady=2, anchor="w")
            else:
                ctk.CTkLabel(self.results_frame, text="Nenhum nutriente encontrado.").pack(pady=10)
        else:
            ctk.CTkLabel(self.results_frame, text="Erro ao buscar nutrientes.").pack(pady=10)


if __name__ == "__main__":
    API_KEY = "HZggsOOEiOiWrnsS5vxzHwgygzuMJm7WHYPV6CIG"
    app = App(api_key=API_KEY)
    app.mainloop()
