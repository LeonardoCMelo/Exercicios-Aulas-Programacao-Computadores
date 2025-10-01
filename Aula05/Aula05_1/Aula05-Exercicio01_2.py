def exercicio_1_2(a, b):
    """
    Calcula a subtração de forma recursiva
    
    Parâmetros:
        a: Subtraendo
        b: Minuendo
    
    Retorno:
        None se o valor de a ou b for negativo
        Se não retorna a subtração de b pelo sub
    """
    if a < 0 or b < 0:
        b = None
    elif a > 0:
        b = exercicio_1_2(a - 1, b - 1)
    return b