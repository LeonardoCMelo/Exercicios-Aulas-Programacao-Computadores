def exercicio_1(L : list[int]):
    """Realiza a soma dos elementos de uma lista.

    Args:
        L (list[int]): Lista de números a serem somados.
    
    Returns:
        int | None: A soma dos elementos da lista. 
            Retorna None se a lista estiver vazia.
    """
    if len(L) == 0:
        return None
    soma = 0
    for i in L:
        soma += i
    return soma