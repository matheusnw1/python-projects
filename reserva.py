
assentos = [1, 2, 5, 8, 10, 15]

total_assentos = 20

livres = []

for i in range(1, total_assentos + 1):
    if i not in assentos:
        livres.append(i)

print("Assentos ocupados:", assentos)
print("Assentos livres:", livres)

reserva = 7

if reserva < 1 or reserva > total_assentos:
    print("Assento inválido")
elif reserva in assentos:
    print("Assento já ocupado")
else:
    assentos.append(reserva)
    assentos.sort()
    print("Reserva realizada")

ocupacao = (len(assentos) / total_assentos) * 100

print("\nAssentos atualizados:", assentos)
print(f"Taxa de ocupação: {ocupacao:.1f}%")
