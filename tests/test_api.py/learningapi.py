import pandas as pd
import requests

url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/jose|maria"
response = requests.get(url)

# Verifique o status da resposta
print("Status Code:", response.status_code)

# Se a resposta foi bem-sucedida (código 200), exiba o conteúdo
if response.status_code == 200:
    data_json = response.json()[0]["res"]
    df = pd.DataFrame(data_json)
    print(df)
else:
    print(f"Erro na requisição: {response.status_code}")

