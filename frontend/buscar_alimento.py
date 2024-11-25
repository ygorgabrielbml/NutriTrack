import requests
import pandas as pd


class BuscarAlimento:
    def __init__(self, api_key, search_url="https://api.nal.usda.gov/fdc/v1/foods/search"):
        self.api_key = api_key
        self.search_url = search_url

    def encontrar_alimento(self, query):
        params = {"query": query, "api_key": self.api_key}
        response = requests.get(self.search_url, params=params)
        if response.status_code == 200:
            return pd.DataFrame(response.json().get("foods", []))
        return None

    def buscar_nutrientes(self, fdc_id):
        nutrient_url = f"https://api.nal.usda.gov/fdc/v1/food/{fdc_id}"
        params = {"api_key": self.api_key}
        response = requests.get(nutrient_url, params=params)
        if response.status_code == 200:
            return pd.DataFrame(response.json().get("foodNutrients", []))
        return None

    def filtrar_colunas(self, alimentos_df):
        return alimentos_df[["description", "fdcId"]]
