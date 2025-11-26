import math

def exercicio_3_5_1(ini, fim):
    todos = set()
    nao_primos = set()
    
    for n in range(ini, fim + 1):
        if n < 2:
            continue
        
        todos.add(n)
        
        limite = int(math.sqrt(n))
        for d in range(2, limite + 1):
            if n % d == 0:
                nao_primos.add(n)
                break
    
    return todos - nao_primos
