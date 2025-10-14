def exercicio_5_3(sent):
    
    menor = maior = None
    value = -sent
    while value != sent:

        value = int(input())
        
        if value == sent and menor is None and maior is None:
            return (sent, sent)
        if value < 0 and menor is None and maior is None:
            return None
        
        if (menor is None or menor > value) and value > 0:
            menor = value
        if (maior is None or maior < value) and value > 0:
            maior = value

    return (maior, menor)

print(exercicio_5_3(-1))