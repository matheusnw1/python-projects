
usuarios = {
    "admin": "1234",
    "guilherme": "python"
}

tentativas = {}

while True:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in tentativas and tentativas[usuario] >= 3:
        print("Conta bloqueada.")
        continue

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
        break

    else:
        print("Usuário ou senha incorretos.")

        if usuario not in tentativas:
            tentativas[usuario] = 1
        else:
            tentativas[usuario] += 1

        restantes = 3 - tentativas[usuario]

        if restantes > 0:
            print(f"Tentativas restantes: {restantes}")
        else:
            print("Conta bloqueada.")
          
