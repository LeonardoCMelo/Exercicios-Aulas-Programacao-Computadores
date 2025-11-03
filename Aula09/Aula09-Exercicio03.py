def exercicio_3(tupla: tuple[int]):
    """
    Divide uma tupla de números inteiros em duas metades e retorna uma lista contendo essas partes.

    Se a tupla for vazia, retorna uma lista vazia.
    Se a tupla tiver um número ímpar de elementos, a segunda metade conterá um elemento a mais.

    Args:
        tupla (tuple[int]): Tupla de números inteiros a ser dividida.

    Returns:
        list[tuple[int]]: Lista contendo duas tuplas — a primeira metade e a segunda metade.
        Caso a tupla de entrada seja vazia, retorna uma lista vazia.
    """
    if len(tupla) == 0:
        lista = []
    else:
        lista = [(tupla[:len(tupla)//2]),(tupla[len(tupla)//2:])]
    return lista
