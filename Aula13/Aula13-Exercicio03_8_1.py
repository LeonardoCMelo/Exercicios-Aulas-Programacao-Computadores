def exercicio_3_8_1(texto: str) -> dict:
    tamanhos_palavras = {}
    
    palavras = texto.split()
    
    for palavra in palavras:
        tamanho = len(palavra)
        tamanhos_palavras[palavra] = tamanho
        
    return tamanhos_palavras
