def exercicio_5(L: list):
    """
    Converte uma lista em uma tupla.

    Args:
        L (list): Lista contendo os elementos a serem convertidos.

    Returns:
        tuple: Tupla contendo os mesmos elementos da lista de entrada.
    """
    T = tuple()
    for i in L:
        T += (i,)
    return T
