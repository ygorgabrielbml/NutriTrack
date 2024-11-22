from api import api_key
import requests

def get_food_data(food_name):
    key = api_key
    base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    params = {
        "query": food_name,
        "api_key": key,
        "pageSize": 1  # Limitando a resposta ao primeiro resultado
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data["foods"]:
            food_data = data["foods"][0]  # Pega o primeiro item dos resultados
            return food_data
        else:
            return "Alimento não encontrado."
    else:
        return f"Erro na requisição: {response.status_code}"

def main():
    food_name = input("Digite o nome do alimento que deseja buscar: ")
    food_data = get_food_data(food_name)
    
    if isinstance(food_data, dict):
        # Exibe informações do alimento (exemplo com alguns dados)
        print("Nome do Alimento:", food_data["description"])
        print("Marca:", food_data.get("brandOwner", "Desconhecida"))
        print("Nutrientes:")
        for nutrient in food_data.get("foodNutrients", []):
            print(f"{nutrient['nutrientName']}: {nutrient['value']} {nutrient['unitName']}")
    else:
        print(food_data)