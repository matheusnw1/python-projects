
palavras = [
    "arara",
    "banana",
    "ovo",
    "python",
    "radar",
    "nivel"
]

print("Palavras:")
for p in palavras:
    print(p)

palindromos = []
nao_palindromos = []

for p in palavras:
    if p == p[::-1]:
        palindromos.append(p)
    else:
        nao_palindromos.append(p)

quantidade = len(palindromos)

maior_palindromo = ""
for p in palindromos:
    if len(p) > len(maior_palindromo):
        maior_palindromo = p

print("\nPalíndromos:", palindromos)
print("Quantidade:", quantidade)
print("Maior palíndromo:", maior_palindromo)
print("Não palíndromos:", nao_palindromos)
