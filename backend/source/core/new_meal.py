import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import sqlite3 as sq
from datetime import datetime
from source.api.searchFood1 import find_food

def create_new_meal():
    # Solicita o nome da refeição e o número de ingredientes
    meal_name = input("Insira o nome da sua nova refeição: ")
    ingredient_num = int(input("Insira o número de ingredientes que deseja adicionar à refeição: "))

    # Lista para armazenar os alimentos selecionados
    selected_foods = []

    # Loop para adicionar cada ingrediente
    for _ in range(ingredient_num):
        food_input = input("Pesquise por um alimento em inglês: ")
        foods = find_food(food_input)  # Captura o DataFrame retornado

        if foods is not None:
            # Exibe o índice e solicita que o usuário escolha um alimento
            idx = int(input("Escolha o índice do alimento para adicionar: "))
            alimento_selecionado = foods.iloc[idx]["description"]
            selected_foods.append(alimento_selecionado)
    
    # Conecta ao banco de dados
    conn = sq.connect("meal.db")
    cursor = conn.cursor()

    # Insere a refeição na tabela `meals` e obtém o `meal_id` gerado
    create_date = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO meals (meal_name, create_date)
        VALUES (?, ?)
    """, (meal_name, create_date))
    
    meal_id = cursor.lastrowid  # Obtém o ID da refeição recém-inserida

    # Insere cada ingrediente na tabela `meal_ingredients`, referenciando o `meal_id`
    for ingredient in selected_foods:
        cursor.execute("""
            INSERT INTO meal_ingredients (meal_id, ingredient)
            VALUES (?, ?)
        """, (meal_id, ingredient))

    conn.commit()
    conn.close()
    print("Refeição adicionada ao banco de dados com sucesso!")

# Exemplo de uso da função
create_new_meal()
