def exercicio_1_4(a, b):
    """
    Calcula a divisão entre dois números de forma recursiva.

    Parâmetros:
        a: Dividendo
        b: Divisor

    Retorno:
        None se o b for menor ou igual a zero
        0 se o b for maior que o a
        Se não retorna o resultado da divisão.
    """
    if b <= 0:
        return None
    if a < b or a == 0:
        return 0
    result = exercicio_1_4(a-b, b)
    return result + 1