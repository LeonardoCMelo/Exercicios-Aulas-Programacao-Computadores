def exercicio_2(nome_arquivo: str) -> int:
    """
    Recebe o nome de um arquivo de texto e conta quantas vezes a palavra 'PC'
    aparece no arquivo, independentemente de maiúsculas ou minúsculas.

    Args:
        nome_arquivo (str): Nome do arquivo de texto a ser lido.

    Returns:
        int: Quantidade de vezes que a palavra "pc" aparece no arquivo.
    """
    palavra = "pc"
    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read().lower()
            contador: int = conteudo.count(palavra)
    except:
        contador: int = 0
    return contador
