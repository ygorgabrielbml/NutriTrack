import requests
import pandas as pd
from IPython.display import display  # Importando o display

api_key = "HZggsOOEiOiWrnsS5vxzHwgygzuMJm7WHYPV6CIG"
base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"

food_input = input("Pesquise por um alimento: ").lower().strip()
params = {
    "api_key": api_key,
    "query": [food_input],
    "pageSize": 20
} 

response = requests.get(url=base_url, params=params)
print("Status Code:", response.status_code)
if response.status_code == 200:
    data = response.json()
    data_foods = data.get("foods", [])
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
    
    """# Explode a coluna 'foodNutrients' para exibir os nutrientes em uma tabela separada
    foods_exploded = dataframe.explode("foodNutrients").reset_index(drop=True)
    nutrients_df = pd.json_normalize(foods_exploded["foodNutrients"])
    nutrients_df["fdcId"] = foods_exploded["fdcId"]  # Adiciona o fdcId para identificação
    
    # Exibe a tabela de nutrientes separadamente
    print("\nTabela de Nutrientes:")
    display(nutrients_df[["fdcId", "nutrientName", "value", "unitName"]])"""
else:
    print("Not ok")
