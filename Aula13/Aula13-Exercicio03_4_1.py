import math

def exercicio_3_4_1(ini, fim):
    primos = []
    
    for n in range(ini, fim + 1):
        if n < 2: 
            continue
            
        eh_primo = True
        limite = int(math.sqrt(n))
        
        for d in range(2, limite + 1):
            if n % d == 0:
                eh_primo = False
                break
        
        if eh_primo:
            primos.append(n)
            
    return primos
