def exercicio_2(L : list[int]):
    """Realiza a média da soma dos elementos de uma lista

    Args:
        L (list[int]): Lista de números a serem somados.
    
    Returns:
        float | None: A média da soma dos elementos da lista.
            Retorna None se a lista estiver vazia
    """
    if len(L) == 0:
        return None
    
    soma = 0
    media = 0.0

    for i in L:
        soma += i
    
    media = soma/len(L)
    
    return media