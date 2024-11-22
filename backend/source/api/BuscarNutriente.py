import requests
import pandas as pd
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

    def mostrar_resultados(self, nutrientes_processados):
        print("\nTabela de nutrientes:")
        print(nutrientes_processados)
        print()

if __name__ == "__main__":
    API_KEY = "HZggsOOEiOiWrnsS5vxzHwgygzuMJm7WHYPV6CIG"
    buscar_alimento = BuscarAlimento(api_key=API_KEY)

    nome_alimento = input("Pesquise por um alimento em inglês: ")
    alimentos = buscar_alimento.encontrar_alimento(nome_alimento)

    if alimentos is not None:
        alimentos_filtrados = buscar_alimento.filtrar_colunas(alimentos)

        if alimentos_filtrados is not None:
            print("\nResultados encontrados:")
            print()
            buscar_alimento.mostrar_resultados(alimentos_filtrados)

            try:
                # Seleção de índice
                index = int(input("Escolha o índice do alimento para buscar os nutrientes: "))
                if index < 0 or index >= len(alimentos_filtrados):
                    raise ValueError("Índice fora do intervalo dos resultados disponíveis.")

                # Obtém o fdcId do alimento selecionado
                fdc_id = alimentos_filtrados.iloc[index]["fdcId"]

                # Instancia a classe BuscarNutriente
                buscar_nutriente = BuscarNutriente(api_key=API_KEY)

                # Busca os nutrientes
                nutrientes_df = buscar_nutriente.pegar_nutrientes(fdc_id)
                if nutrientes_df is not None:
                    # Filtra as colunas relevantes
                    nutrientes_processados = buscar_nutriente.filtrar_colunas(nutrientes_df)
                    if nutrientes_processados is not None:
                        # Exibe os resultados
                        buscar_nutriente.mostrar_resultados(nutrientes_processados)

            except ValueError as e:
                print(f"Erro: {e}")
        else:
            print("Não foi possível filtrar os alimentos.")
    else:
        print("Nenhum alimento encontrado. Tente novamente.")
