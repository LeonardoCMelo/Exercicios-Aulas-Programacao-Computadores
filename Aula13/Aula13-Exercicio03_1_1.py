def exercicio_3_1_1(ini, fim):
    resultado = []
    for numero in range(ini, fim + 1):
        if '7' in str(numero):
            resultado.append(numero)
    return resultado
