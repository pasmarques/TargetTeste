import json

# Abrir e carregar o arquivo JSON
with open('dados.json', 'r') as file:
    # É transformado em uma lista de dicionários
    faturamento_diario = json.load(file)
    # Cada dicionário da lista representa um dia de faturamento, onde cada dia tem a sua identificação e o faturamento daquele dia

# Filtrar apenas os dias com faturamento para calcular só os dados que interessam
# A variável valorDoDia sempre acessa o valor faturado em cada dia
valores_faturamento = [valorDoDia["valor"]
                       for valorDoDia in faturamento_diario if valorDoDia["valor"] > 0]

# Calcular o menor e o maior valor de faturamento
menor_faturamento = min(valores_faturamento)
maior_faturamento = max(valores_faturamento)

# Calcular a média mensal, ignorando dias sem faturamento
media_mensal = sum(valores_faturamento) / len(valores_faturamento)

# Contar o número de dias com faturamento superior à média mensal
# Para cada dia acima da media acrescente 1 a variável valorDoDia
dias_acima_da_media = sum(
    1 for valorDoDia in valores_faturamento if valorDoDia > media_mensal)

# Exibir os resultados
print(f"Menor faturamento em um dia do mês: {menor_faturamento:.2f}")
print(f"Maior faturamento em um dia do mês: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {
      dias_acima_da_media}")
