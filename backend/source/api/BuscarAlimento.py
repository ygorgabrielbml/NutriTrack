import pandas as pd
import requests

class BuscarAlimento:
    def __init__(self, api_key, url="https://api.nal.usda.gov/fdc/v1/foods/search"):
        self.api_key = api_key
        self.url = url

    def encontrar_alimento(self, nome_alimento):
        params = {
            "api_key": self.api_key,
            "query": nome_alimento,
            "pageSize": 10,
        }

        try:
            response = requests.get(url=self.url, params=params)
            response.raise_for_status()
            dados = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None

        dados_comidas = dados.get("foods", [])
        if not dados_comidas:
            print(f"Não encontramos esse alimento em nosso banco de dados!")
            return None

        # Converte os dados em um DataFrame pandas
        dataframe = pd.DataFrame(dados_comidas)
        return dataframe

    def filtrar_colunas(self, dataframe):
        colunas_desejadas = ["description", "fdcId", "foodCategory"]
        colunas_exibidas = [col for col in colunas_desejadas if col in dataframe.columns]

        return dataframe[colunas_exibidas]

    def mostrar_resultados(self, dataframe):
        print("Tabela Principal - Informações Básicas dos Alimentos:")
        print()

        print(dataframe)
        print()

if __name__ == "__main__":
    API_KEY = "HZggsOOEiOiWrnsS5vxzHwgygzuMJm7WHYPV6CIG"
    procurar_alimento = BuscarAlimento(api_key=API_KEY)

    nome_alimento = input("Pesquise por seu alimento em inglês: ").lower().strip()

    resultado = procurar_alimento.encontrar_alimento(nome_alimento)

    if resultado is not None:
        resultados_filtrados = procurar_alimento.filtrar_colunas(resultado)

        procurar_alimento.mostrar_resultados(resultados_filtrados)
    else:
        print("Nenhum resultado encontrado.")
