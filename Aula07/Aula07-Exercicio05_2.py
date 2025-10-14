def exercicio_5_2(sent):
    value = int(input())
    
    if value<=0 or value == sent:
        return None
    
    menor = maior = value
    
    while value != sent:
        
        if  menor is None or menor > value:
            menor = value
        if maior is None or maior < value:
            maior = value
        
        value = int(input())
    
    return (maior, menor)

print(exercicio_5_2(-1))