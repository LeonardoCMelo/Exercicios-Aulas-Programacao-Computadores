import math

def exercicio_3_3_1(ini, fim):
    resultado = []
    limite_divisor = int(math.sqrt(fim))
    
    for n in range(ini, fim + 1):
        for d in range(2, limite_divisor + 1):
            if n % d == 0:
                resultado.append(n)
                break
                
    return resultado
