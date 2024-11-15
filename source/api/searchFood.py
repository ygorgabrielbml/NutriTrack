import requests
import pandas as pd
from IPython.display import display  # Importando o display

# Configurações da API
api_key = "HZggsOOEiOiWrnsS5vxzHwgygzuMJm7WHYPV6CIG"
base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"

def buscar_alimento(food_input):
    """
    Função para buscar alimentos na API USDA e exibir informações básicas.
    
    Parâmetros:
    food_input (str): Nome do alimento a ser pesquisado.
    """
    params = {
        "api_key": api_key,
        "query": food_input.lower().strip(),
        "pageSize": 20
    } 

    # Faz a requisição para buscar alimentos
    response = requests.get(url=base_url, params=params)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        data_foods = data.get("foods", [])
        
        # Verifica se há resultados
        if not data_foods:
            print("Não encontramos esse alimento em nosso banco de dados.")
        else:
            dataframe = pd.DataFrame(data_foods)
            
            # Tabela principal com informações básicas dos alimentos
            foods = dataframe[
                [
                    "description",
                    "fdcId",
                    "foodCategory",
                    "ndbNumber"
                ]
            ]
            
            print("Tabela Principal - Informações Básicas dos Alimentos:")
            display(foods)
            
            # Bloco comentado para exibir nutrientes
            """
            # Explode a coluna 'foodNutrients' para exibir os nutrientes em uma tabela separada
            foods_exploded = dataframe.explode("foodNutrients").reset_index(drop=True)
            nutrients_df = pd.json_normalize(foods_exploded["foodNutrients"])
            nutrients_df["fdcId"] = foods_exploded["fdcId"]  # Adiciona o fdcId para identificação
            
            # Exibe a tabela de nutrientes separadamente
            print("\nTabela de Nutrientes:")
            display(nutrients_df[["fdcId", "nutrientName", "value", "unitName"]])
            """
    else:
        print("Erro ao fazer a busca:", response.status_code)

# Exemplo de uso da função
alimento = input("Pesquise por um alimento em inglês: ")
buscar_alimento(alimento)
