def exercicio_6(L: list[tuple[int]], n: int):
    """
    Substitui o último elemento de cada tupla em uma lista por um novo valor.

    Args:
        L (list[tuple[int]]): Lista de tuplas de números inteiros.
        n (int): Valor inteiro que substituirá o último elemento de cada tupla.

    Returns:
        list[tuple[int]] | None: 
        - Uma nova lista com tuplas modificadas.
        - None se a lista de entrada estiver vazia.
    """
    if len(L) == 0:
        result = None
    else:
        result = []
        for i in L:
            if len(i) == 0:
                result.append(())
            else:
                result.append(i[:-1]+(n,))
    return result
