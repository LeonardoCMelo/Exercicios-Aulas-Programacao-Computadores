def exercicio_1(n: int):
    """
    Gera uma lista de tuplas contendo números inteiros de 1 a n e seus respectivos quadrados.

    Args:
        n (int): O número inteiro limite superior do intervalo (inclusivo).

    Returns:
        list[tuple[int, int]]: Lista de tuplas (x, x²) para cada inteiro x de 1 até n.
        None: Se n for nulo ou negativo.
    """
    if n<=0:
        lista = None
    else:
        lista = []
        for i in range(1,n+1):
            lista.append((i, i**2))
    return lista
