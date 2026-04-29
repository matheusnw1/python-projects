
numeros = [4, 2, 1, 6, 5, 9, 8, 5, 6, 6, -1, 0, 1]

if not numeros:
    print([])
else:
    numeros_unicos = sorted(set(numeros))

    sequencias = []
    atual = [numeros_unicos[0]]

    for i in range(1, len(numeros_unicos)):
        if numeros_unicos[i] == numeros_unicos[i - 1] + 1:
            atual.append(numeros_unicos[i])
        else:
            sequencias.append(atual)
            atual = [numeros_unicos[i]]

    sequencias.append(atual)

    print("Sequências:", sequencias)
  
