import requests
import pandas as pd
from IPython.display import display  # Importando o display

# Configurações da API
api_key = "HZggsOOEiOiWrnsS5vxzHwgygzuMJm7WHYPV6CIG"
base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"

def find_food(food_input):
    """
    Função para buscar alimentos na API USDA e retornar um DataFrame com informações básicas.
    
    Parâmetros:
    food_input (str): Nome do alimento a ser pesquisado.
    
    Retorna:
    pd.DataFrame: DataFrame contendo as informações dos alimentos encontrados ou None se não houver resultados.
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
            return None
        else:
            dataframe = pd.DataFrame(data_foods)
            
            # Filtra as colunas disponíveis de forma segura
            columns_to_include = [col for col in ["description", "fdcId", "foodCategory", "ndbNumber"] if col in dataframe.columns]
            foods = dataframe[columns_to_include]
            
            print("Tabela Principal - Informações Básicas dos Alimentos:")
            display(foods)
            return foods  # Retorna o DataFrame para que possa ser manipulado externamente
    else:
        print("Erro ao fazer a busca:", response.status_code)
        return None

# Exemplo de uso da função (comentado para evitar execução ao ser importado)
#alimento = input("Pesquise por um alimento em inglês: ")
#find_food(alimento)
