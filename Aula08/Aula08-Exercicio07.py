def exercicio_7(linhas : int):
    """Gera e retorna um triângulo de asteriscos começando da linha menor a maior.
    
    Args:
        linhas (int): Número de linhas (altura) do triângulo.
    Returns:
        str | None: Uma string contendo o triângulo de asteriscos, 
            ou None se o número de linhas for menor ou igual a zero.
    """
    triangulo = ""

    if linhas <= 0:
        triangulo = None
    else:
        for i in range(linhas):
            triangulo += " "*(linhas-i-1)+"*"*(2*i+1)
            if i != linhas - 1:
                triangulo += "\n"
    return triangulo