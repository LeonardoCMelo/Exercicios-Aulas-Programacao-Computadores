def exercicio_7_2(n):
    soma = 0.0
    for i in range(1, n+1):
        soma += (2 * i - 1) / i
    return soma