def exercicio_5(L : list):
    """Cria e retorna a clonagem de uma lista fornecida.
    
    Args:
        L (list): lista a ser clonada.
    
    Returns:
        list: Uma nova lista contendo os mesmos elementos de L.
    """
    outList = []
    
    for item in L:
        outList.append(item)
    
    return outList