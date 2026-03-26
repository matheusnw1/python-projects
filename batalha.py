
herois = [
    {"nome": "Aragorn", "classe": "Guerreiro", "hp": 100, "ataque": 85, "defesa": 60},
    {"nome": "Legolas", "classe": "Arqueiro",  "hp": 75,  "ataque": 95, "defesa": 40},
    {"nome": "Gimli",   "classe": "Barbaro",   "hp": 120, "ataque": 70, "defesa": 80},
    {"nome": "Gandalf", "classe": "Mago",      "hp": 60,  "ataque": 100,"defesa": 30},
]

def esta_vivo(heroi):
    return heroi["hp"] > 0

def receber_dano(heroi, dano):
    dano_real = dano - heroi["defesa"]
    if dano_real < 1:
        dano_real = 1
    heroi["hp"] -= dano_real
    print(f"{heroi['nome']} recebeu {dano_real} de dano!")

def atacar(atacante, alvo):
    print(f"\n{atacante['nome']} vai atacar {alvo['nome']}!")
    dano = atacante["ataque"]
    receber_dano(alvo, dano)

def status(heroi):
    print("\n--- STATUS ---")
    print(f"Nome: {heroi['nome']}")
    print(f"Classe: {heroi['classe']}")
    print(f"HP: {heroi['hp']}")
    print(f"Ataque: {heroi['ataque']}")
    print(f"Defesa: {heroi['defesa']}")
    print("--------------")

def batalha(heroi1, heroi2):
    print(f"\n⚔️ BATALHA: {heroi1['nome']} VS {heroi2['nome']} ⚔️")
    turno = 1

    while esta_vivo(heroi1) and esta_vivo(heroi2):
        print(f"\n===== TURNO {turno} =====")

        atacar(heroi1, heroi2)

        if not esta_vivo(heroi2):
            print(f"\n💀 {heroi2['nome']} foi derrotado!")
            break

        atacar(heroi2, heroi1)

        if not esta_vivo(heroi1):
            print(f"\n💀 {heroi1['nome']} foi derrotado!")
            break

        status(heroi1)
        status(heroi2)

        turno += 1

    print("\n🏁 FIM DA BATALHA!")

batalha(herois[0], herois[1])
