def exercicio_6(L1 : list, L2: list):
    """Verifica se duas listas possuem pelo menos um elemento em comum.
    Args:
        L1 (list): Primeira lista.
        L2 (list): Segunda lista.
    
    Returns:
        bool: True se tiver algum elemento em comum,
            False caso contrário.
    """
    for item in L1:
        if item in L2:
            return True
    return False