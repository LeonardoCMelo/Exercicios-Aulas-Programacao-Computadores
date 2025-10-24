def exercicio_9(linhas):
    """Gera e retorna uma árvore de asteriscos.
    
    Args:
        linhas (int): Número de linhas (altura) da parte superior.
    Returns:
        str | None: Uma string contendo a árvore de asteriscos, 
            ou None se o número de linhas for menor ou igual a zero.
    """
    arvore = ""
    if linhas <= 0:
        arvore = None
    else:
        for i in range(linhas):
            arvore += " "*(linhas-i-1)+"*"*(2*i+1) + "\n"
        for i in range(linhas//2, linhas-1):
            arvore += " "*(linhas-i)+"*"*(2*i-1) + "\n"
        arvore = arvore[:-1]
    return arvore