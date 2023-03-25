import json

with open('dados.json', 'r') as file:
    faturamento_diario = json.load(file)

# Calcula menor e maior valor de faturamento diário
menor_valor = min(dia['valor'] for dia in faturamento_diario)
maior_valor = max(dia['valor'] for dia in faturamento_diario)

# Calcula a média de faturamento diário (excluindo dias sem faturamento)
dias_com_faturamento = [dia['valor'] for dia in faturamento_diario if dia['valor'] != 0]
media = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calcula o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = len([dia for dia in faturamento_diario if dia['valor'] > media])

print(f'Menor valor de faturamento diário: R${menor_valor:.2f}')
print(f'Maior valor de faturamento diário: R${maior_valor:.2f}')
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_da_media}')