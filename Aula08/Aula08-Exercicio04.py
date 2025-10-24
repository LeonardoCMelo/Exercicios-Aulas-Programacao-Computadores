def exercicio_4(L : list[str]):
    """Conta quantas strings da lista possuem mais de um caractere e 
    têm o primeiro e o último caracteres iguais.

    Args:
        L (list[str]): Lista de strings a serem analisadas.

    Returns:
        int: Quantidade de strings que atendem ao critério. 
    """
    count = 0
    
    if len(L) == 0:
        return count
    
    for string in L:
        if len(string) >= 2 and string[0]==string[-1]:
            count += 1
    
    return count