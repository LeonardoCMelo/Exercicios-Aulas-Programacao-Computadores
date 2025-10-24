def exercicio_3(L : list[int]):
    """Encontra o menor e maior elementos de uma lista.

    Args:
        L (list[int]): Lista de números a serem avaliados.
    Returns:
        tuple[None, None] | tuple[int, int]: Uma tupla com o menor e o maior valor, nesta ordem.
            Retorna uma tupla de valores (None, None) caso a tupla esteja em branco.
    """

    if len(L) == 0:
        return (None, None)
    
    maior = menor = L[0]

    for i in L:
        if i > maior:
            maior = i
        if i < menor:
            menor = i

    return (menor, maior)