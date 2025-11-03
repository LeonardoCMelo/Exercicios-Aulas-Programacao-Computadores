def exercicio_7(cotacao: float):
    """
    Gera uma lista com duas tuplas por valor de 1 a 100, 
    contendo o valor em reais e sua conversão em dólar, 
    e vice-versa.

    Args:
        cotacao (float): Valor usado para conversão.

    Returns:
        list[tuple[float, float]]: Lista com 200 tuplas no formato (i, resultado).
    """
    lista = []
    for i in range(1,101):
        lista.append((i, round(cotacao*i,2)))
        lista.append((i, round(i/cotacao,2)))
    return lista
