
import random
import string

letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

todos = letras + numeros + simbolos

quantidade = int(input("Quantidade de caracteres: "))

senha = "".join(random.choice(todos) for _ in range(quantidade))

tem_numero = any(c in numeros for c in senha)
tem_simbolo = any(c in simbolos for c in senha)

while not (tem_numero and tem_simbolo):

    senha = "".join(random.choice(todos) for _ in range(quantidade))

    tem_numero = any(c in numeros for c in senha)
    tem_simbolo = any(c in simbolos for c in senha)

print(f"Senha gerada: {senha}")
