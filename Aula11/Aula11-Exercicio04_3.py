def exercicio_4_3(dicionario: dict, letra: str, codigo: int):
    if not dicionario or letra not in dicionario:
        result = None
    else:
        if codigo == 0:
            dicionario[letra] = 0
            result = dicionario.copy()
        elif codigo == -1:
            dicionario.pop(letra)
            result = dicionario.copy()
        else:
            result = None

    return result
