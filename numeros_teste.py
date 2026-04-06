
lista = [1, 5, -7, 4, 5]


def tipo(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

def valor(numero):
    if numero > 0:
        return 'Positivo'
    elif numero < 0:
        return 'Negativo'
    else:
        return 'Zero'

def dobro(numero):  
    return numero * 2
    
def quadrado(numero):
    return numero * numero

def analise(lista):
    resultado = []
    for numero in lista:
        resultado.append(f'{numero:>2} | Tipo: {tipo(numero):>6} | Valor: {valor(numero)} | Dobro: {dobro(numero):>3} | Quadrado: {quadrado(numero)}')
    return resultado

print('\n'.join(analise(lista)))
