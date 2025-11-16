def exercicio_3(nome_arquivo):
    """
    Recebe o nome de um arquivo de texto e substitui todas as vogais
    (maiúsculas e minúsculas) por asteriscos (*). O arquivo é atualizado
    com o novo conteúdo.

    Args:
        nome_arquivo (str): Nome do arquivo de texto a ser modificado.
    
    Returns:
        None
    """
    vogais = "aeiouAEIOU"
    try:
        with open(nome_arquivo, "r+") as arquivo:
            conteudo = arquivo.read()
            for c in conteudo:
                if c in vogais:
                    conteudo = conteudo.replace(c, "*")
            arquivo.writelines(conteudo)
    except:
        print("Erro ao abrir o arquivo.")
    return
