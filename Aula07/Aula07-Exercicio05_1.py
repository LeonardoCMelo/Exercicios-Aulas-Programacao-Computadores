def exercicio_5_1(n):
    maior = None
    menor = None
    for i in range(n):
        value = int(input())
        if n<=0:
            return None
        if  menor is None or menor > value:
            menor = value
        if maior is None or maior < value:
            maior = value
    return (maior, menor)