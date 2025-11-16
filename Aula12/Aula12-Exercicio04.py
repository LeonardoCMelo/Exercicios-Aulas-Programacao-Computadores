def exercicio_4(nome_arquivo: str, lista_emails: list[str]) -> None:
    """
    Recebe o nome de um arquivo de texto e uma lista de emails.
    Adiciona os emails ao final do arquivo, cada um em uma nova linha.

    Args:
        nome_arquivo (str): Nome do arquivo de texto a ser modificado.
        lista_emails (list[str]): Lista de emails a serem adicionados ao arquivo.

    Returns:
        None
    """
    try:
        with open(nome_arquivo, "a") as arquivo:
            for email in lista_emails[:-1]:
                arquivo.write(email + "\n")
            arquivo.write(lista_emails[-1])
    except:
        print("Erro ao abrir o arquivo.")
    return
