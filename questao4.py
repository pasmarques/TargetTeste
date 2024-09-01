# Foi utilizado python por conta da estrutura de dados dicionário
# Com isso foi possível armazenar os estados e faturamentos de forma mais dinâmica


def calcular_percentual_representacao(faturamento_estados):
    # Calcula o faturamento total
    faturamento_total = sum(faturamento_estados.values())
    
    # Inicializa o dicionário para armazenar percentuais de representação
    percentuais = {}
    
    # Itera sobre cada chave (estado) e valor (faturamento) no dicionário
    for estado, faturamento in faturamento_estados.items():
        # Calcula o percentual de representação para o estado atual
        percentual = (faturamento / faturamento_total) * 100
        # Armazena o percentual no dicionário de percentuais
        percentuais[estado] = percentual
        
    return percentuais

# Definindo os valores de faturamento para cada estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula os percentuais de representação
percentual_representacao = calcular_percentual_representacao(faturamento_estados)

# Exibe os percentuais de representação para cada estado
for estado, percentual in percentual_representacao.items():
    print(f"{estado}: {percentual:.2f}%")
