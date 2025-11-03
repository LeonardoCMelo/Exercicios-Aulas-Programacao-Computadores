def exercicio_4(tupla: tuple[int]):
    """
    Separa os números pares e ímpares de uma tupla de inteiros.

    Retorna uma lista contendo duas tuplas: 
    - A primeira com todos os números pares.
    - A segunda com todos os números ímpares.
    Se a tupla de entrada for vazia, retorna uma lista vazia.

    Args:
        tupla (tuple[int]): Tupla de números inteiros a ser processada.

    Returns:
        list[tuple[int]]: Lista com duas tuplas (pares, ímpares). 
        Caso a tupla de entrada seja vazia, retorna uma lista vazia.
    """
    if len(tupla) == 0:
        lista = []
    else:
        tuplaPar = tuple()
        tuplaImpar = tuple()
        for i in tupla:
            if i%2 == 0:
                tuplaPar += (i,)
            else:
                tuplaImpar += (i,)
        lista = [tuplaPar,tuplaImpar]
    return lista
