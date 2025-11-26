def exercicio_3_8_2(texto: str) -> dict:
    tamanhos_palavras = {palavra: len(palavra) for palavra in texto.split()}
    
    return tamanhos_palavras
