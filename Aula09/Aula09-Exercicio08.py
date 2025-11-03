def exercicio_8(lista_de_cotacoes: list[tuple]):
    """
    Formata uma lista de tuplas de conversão (gerada pela função exercicio_7)
    em uma tabela de valores de 1 a 100, mostrando tanto a conversão de dólar
    para real quanto de real para dólar.

    Args:
        lista_de_cotacoes (list[tuple]): Lista com pares (valor, conversão).

    Returns:
        str: Texto formatado mostrando as conversões.
    """
    values = ""
    for i in range(0,len(lista_de_cotacoes),2):
        values += f"US$ {lista_de_cotacoes[i][0]:6.2f} = R$ {lista_de_cotacoes[i][1]:6.2f}\tR$ {lista_de_cotacoes[i+1][0]:6.2f} = US$ {lista_de_cotacoes[i+1][1]:6.2f}\n"
        values += "-"*22 + "\t" + "-"*22+"\n"
    return values[:-1]
