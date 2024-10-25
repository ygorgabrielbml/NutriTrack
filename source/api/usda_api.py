import requests

api_key = "HZggsOOEiOiWrnsS5vxzHwgygzuMJm7WHYPV6CIG"


food = input("Insira o nome da comida que você tem interesse: ")
url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={food}&api_key={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if "foods" in data and len(data["foods"]) > 0:
        alimentos = data
        print(alimentos)
    else:
        print("Nenhum alimento encontrado")
else:
    print(f"Erro ao se conectar com o URL: {response.status_code}")