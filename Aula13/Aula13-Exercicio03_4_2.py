import math

def exercicio_3_4_2(ini, fim):
    return [n for n in range(ini, fim + 1) 
            if n > 1 and not [d for d in range(2, int(math.sqrt(n)) + 1) if n % d == 0]]
