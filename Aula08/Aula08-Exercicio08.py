def exercicio_8(linhas:int):
    """Gera e retorna um triângulo de asteriscos começando da linha maior a menor.
    
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
            triangulo += " " * i + "*" * ((linhas-i)*2-1)
            if i != linhas - 1:
                triangulo += "\n"
    return triangulo