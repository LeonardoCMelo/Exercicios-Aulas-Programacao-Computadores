import math

def exercicio_3_3_2(ini, fim):
    limite_divisor = int(math.sqrt(fim))
    
    return [n for n in range(ini, fim + 1) 
            if [d for d in range(2, limite_divisor + 1) if n % d == 0]]
