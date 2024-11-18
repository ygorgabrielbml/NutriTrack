from searchFood import find_food
import pandas as pd
from IPython.display import display
import requests


api_key = "HZggsOOEiOiWrnsS5vxzHwgygzuMJm7WHYPV6CIG"
base_url_search = "https://api.nal.usda.gov/fdc/v1/foods/search"
base_url_details = "https://api.nal.usda.gov/fdc/v1/food"

def get_nutrients(fdc_id):
    
    #Busca os nutrientes detalhados de um alimento usando o `fdcId`.
    params = {
        "api_key": api_key
    }
    response = requests.get(url=f"{base_url_details}/{fdc_id}", params=params)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        nutrients = data.get("foodNutrients", [])
        
        #Verifica se encontrou os dados nutricionais
        if not nutrients:
            print("Nenhum dado nutricional encontrado para este alimento.")
            return None

        # Cria o DataFrame com os nutrientes
        nutrients_df = pd.DataFrame(nutrients)

        # Verifica e processa as informações
        if "nutrient" in nutrients_df.columns and "amount" in nutrients_df.columns:
            nutrients_processed = nutrients_df["nutrient"].apply(pd.Series)
            nutrients_processed["amount"] = nutrients_df["amount"]
            nutrients_processed = nutrients_processed[["name", "amount", "unitName"]]

            print("\nTabela de nutrientes:")
            display(nutrients_processed)
            return nutrients_processed
        else:
            print("Estrutura inesperada de dados nutricionais.")
            return None
    else:
        print("Erro ao buscar detalhes nutricionais:", response.status_code)
        return None


def show_nutrients():
    
    #Função principal para pesquisar alimentos e exibir os nutrientes detalhados.
    food_input = input("Pesquise por um alimento em inglês: ")
    foods = find_food(food_input)  # Busca os alimentos

    if foods is not None:
        try:
            index = int(input("Escolha o índice do alimento para pesquisar pelos nutrientes: "))
            if index < 0 or index >= len(foods):
                raise ValueError("Índice fora do intervalo dos resultados disponíveis.")

            # Obtém o `fdcId` do alimento selecionado
            fdc_id = foods.iloc[index]["fdcId"]
            print(f"Buscando nutrientes para o alimento com fdcId: {fdc_id}")
            
            # Busca e exibe os nutrientes
            get_nutrients(fdc_id)

        except ValueError as e:
            print(f"Erro: {e}")
    else:
        print("Nenhum alimento encontrado. Tente novamente.")
        
show_nutrients()
