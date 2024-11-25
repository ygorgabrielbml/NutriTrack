import sqlite3 as sq
from datetime import datetime
from BuscarAlimento import BuscarAlimento  # Importando a classe BuscarAlimento fornecida

class GerenciadorRefeicoes:
    def __init__(self, banco_dados="backend/source/models/database.db", api_key="HZggsOOEiOiWrnsS5vxzHwgygzuMJm7WHYPV6CIG"):
        """
        Inicializa o gerenciador de refeições e a classe BuscarAlimento.
        """
        self.banco_dados = banco_dados
        self.buscar_alimento = BuscarAlimento(api_key=api_key)

    def criar_refeicao(self):
        """
        Cria uma nova refeição com ingredientes escolhidos pelo usuário.
        """
        # Solicita o nome da refeição e o número de ingredientes
        nome_refeicao = input("Insira o nome da sua nova refeição: ")
        while True:
            try:
                num_ingredientes = int(input("Insira o número de ingredientes que deseja adicionar à refeição: "))
                break
            except ValueError:
                print("Por favor, insira uma quantidade válida: ")
        # Lista para armazenar os alimentos selecionados
        ingredientes_selecionados = []

        # Loop para adicionar cada ingrediente
        for _ in range(num_ingredientes):
            alimento_input = input("Pesquise por um alimento em inglês: ")
            alimentos = self.buscar_alimento.encontrar_alimento(alimento_input)

            if alimentos is not None:
                # Filtra os resultados e exibe as colunas desejadas
                alimentos_filtrados = self.buscar_alimento.filtrar_colunas(alimentos)
                print("\nResultados encontrados:")
                self.buscar_alimento.mostrar_resultados(alimentos_filtrados)

                # Solicita ao usuário que escolha um alimento
                try:
                    idx = int(input("Escolha o índice do alimento para adicionar: "))
                    ingrediente_selecionado = alimentos_filtrados.iloc[idx]["description"]
                    ingredientes_selecionados.append(ingrediente_selecionado)
                except (IndexError, ValueError):
                    print("Índice inválido. Tente novamente.")
            else:
                print("Nenhum alimento encontrado. Tente novamente.")

        # Insere a refeição e os ingredientes no banco de dados
        self._salvar_refeicao(nome_refeicao, ingredientes_selecionados)

    def _salvar_refeicao(self, nome_refeicao, ingredientes):
        """
        Salva a refeição e seus ingredientes no banco de dados.
        """
        conn = sq.connect(self.banco_dados)
        cursor = conn.cursor()

        # Insere a refeição na tabela `meals`
        data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cursor.execute("""
            INSERT INTO refeicoes (nome_refeicao, data_criacao)
            VALUES (?, ?)
        """, (nome_refeicao, data_criacao))
        
        refeicao_id = cursor.lastrowid  # Obtém o ID da refeição recém-inserida

        # Insere cada ingrediente na tabela `meal_ingredients`
        for ingrediente in ingredientes:
            cursor.execute("""
                INSERT INTO ingredientes_refeicao (refeicao_id, ingrediente)
                VALUES (?, ?)
            """, (refeicao_id, ingrediente))

        conn.commit()
        conn.close()
        print("Refeição adicionada ao banco de dados com sucesso!")


if __name__ == "__main__":
    # Inicializa o gerenciador de refeições
    gerenciador = GerenciadorRefeicoes()

    # Chama a função para criar uma nova refeição
    gerenciador.criar_refeicao()
''