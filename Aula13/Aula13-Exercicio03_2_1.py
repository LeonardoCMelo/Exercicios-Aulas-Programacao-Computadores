def exercicio_3_2_1(ini, fim):
    resultado = []
    for n in range(ini, fim + 1):
        if n % 11 == 0:
            resultado.append(n)
    return resultado
