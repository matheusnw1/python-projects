def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def exibir_relatorio(nome, notas):
    media = calcular_media(notas)
    situacao = classificar_aluno(media)
    
    print("=" * 28)
    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

def processar_turma(turma):
    for aluno in turma:
        exibir_relatorio(aluno["nome"], aluno["notas"])

turma = [
    {"nome": "Ana",    "notas": [8.0, 7.5, 9.0, 6.5]},
    {"nome": "Bruno",  "notas": [4.0, 5.5, 3.0, 6.0]},
    {"nome": "Carla",  "notas": [6.0, 5.0, 7.0, 5.5]},
]

processar_turma(turma)
