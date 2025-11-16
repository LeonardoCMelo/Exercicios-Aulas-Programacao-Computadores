def exercicio_1(lista_nomes: list[str]) -> None:
    """
    Recebe uma lista de nomes e grava em um arquivo de texto.
    Cada nome deve ser gravado em uma linha diferente.

    Args:
        lista_nomes (list[str]): Lista de nomes a serem gravados no arquivo.

    Returns:
        None
    """
    try:
        with open("exercicio_1_arquivo.txt", "w") as arquivo:
            for nome in lista_nomes[:-1]:
                arquivo.write(nome + "\n")
            arquivo.write(lista_nomes[-1])
    except:
        print("Erro ao criar o arquivo.")
    return
