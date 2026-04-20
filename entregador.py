
entregas = [
    {"entregador": "Ana", "valor": 50},
    {"entregador": "Carlos", "valor": 30},
    {"entregador": "Ana", "valor": 70},
    {"entregador": "Beatriz", "valor": 40},
    {"entregador": "Carlos", "valor": 60},
    {"entregador": "Ana", "valor": 30},
    {"entregador": "Beatriz", "valor": 90},
    {"entregador": "Daniel", "valor": 20}
]

ganhos = {}
quantidade = {}

for e in entregas:
    nome = e["entregador"]
    valor = e["valor"]

    ganhos[nome] = ganhos.get(nome, 0) + valor
    quantidade[nome] = quantidade.get(nome, 0) + 1

medias = {}

for nome in ganhos:
    medias[nome] = ganhos[nome] / quantidade[nome]

melhor = max(ganhos, key=ganhos.get)

ativos = []

for nome, qtd in quantidade.items():
    if qtd > 2:
        ativos.append(nome)

ranking = sorted(ganhos.items(), key=lambda x: x[1], reverse=True)

print("Ganhos totais:", ganhos)
print("Média por entrega:", medias)
print("Maior faturamento:", melhor)
print("Entregadores com mais de 2 entregas:", ativos)

print("\nRanking:")
for nome, valor in ranking:
    print(f"{nome}: R${valor}")
  
