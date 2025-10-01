def exercicio_2_1(n, i):
    """
    Calcula o fatorial de n de forma recursiva, usando o parâmetro auxiliar i que vai de 1 até n.

    Parâmetros:
        n: número inteiro não negativo cujo fatorial será calculado.
        i: contador auxiliar da recursão (inicia em 1).

    Retorno:
        Retorna o valor de n! (fatorial de n), ou None se n < 0.
    """
    if n < 0:
        resultado = None
    elif n == 0:
        resultado = 1
    elif i == n:
        resultado = n
    else:
        resultado = i * exercicio_2_1(n, i + 1)
    return resultado