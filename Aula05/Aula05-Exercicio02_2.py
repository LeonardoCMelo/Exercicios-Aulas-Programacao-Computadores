def exercicio_2_2(n):
    """
    Calcula o fatorial de n de forma iterativa.

    Parâmetros:
        n: número inteiro não negativo cujo fatorial será calculado.

    Retorno:
        Retorna o valor de n! (fatorial de n), ou None se n < 0.
    """
    resultado = 1
    i = 1

    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return None
    while i <= n:
        resultado *= i
        i += 1
    return resultado