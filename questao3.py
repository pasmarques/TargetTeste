import json

# Supondo que o arquivo JSON tem a seguinte estrutura:
# {
#   "faturamento": [
#     {"dia": "01", "valor": 200.0},
#     {"dia": "02", "valor": 0.0},
#     {"dia": "03", "valor": 300.0},
#     # ... mais dias
#   ]
# }

def calcular_faturamento_analise(arquivo_json):
    with open(arquivo_json, 'r') as f:
        dados = json.load(f)
    
    faturamento = [dia['valor'] for dia in dados['faturamento'] if dia['valor'] > 0]
    
    if not faturamento:
        raise ValueError("Não há dados de faturamento válidos para análise.")
    
    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    
    dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)
    
    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_da_media": dias_acima_da_media
    }

# Exemplo de uso
arquivo_json = 'faturamento.json'
resultado = calcular_faturamento_analise(arquivo_json)
print(f"Menor valor de faturamento: {resultado['menor_valor']}")
print(f"Maior valor de faturamento: {resultado['maior_valor']}")