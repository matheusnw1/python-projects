
vendas = [
    {"data": "2025-01-10", "valor": 500},
    {"data": "2025-01-15", "valor": 700},
    {"data": "2025-02-03", "valor": 400},
    {"data": "2025-02-20", "valor": 900},
    {"data": "2025-03-05", "valor": 1200},
    {"data": "2025-03-18", "valor": 300},
    {"data": "2025-01-25", "valor": 200}
]

faturamento_mensal = {}

for venda in vendas:
    mes = venda["data"][5:7]
    faturamento_mensal[mes] = faturamento_mensal.get(mes, 0) + venda["valor"]

mes_maior = max(faturamento_mensal, key=faturamento_mensal.get)

faturamento_total = sum(faturamento_mensal.values())

media = faturamento_total / len(faturamento_mensal)

meses_acima_media = []

for mes, valor in faturamento_mensal.items():
    if valor > media:
        meses_acima_media.append(mes)

print("Faturamento por mês:", faturamento_mensal)
print("Mês com maior faturamento:", mes_maior)
print("Faturamento total:", faturamento_total)
print("Média mensal:", media)
print("Meses acima da média:", meses_acima_media)
