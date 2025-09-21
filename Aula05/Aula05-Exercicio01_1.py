def exercicio_1_1(a,b):
    """
    Calcula a soma de forma recursiva
    
    Parâmetros:
        a: Primeiro Termo
        b: Segundo Termo
    
    Retorno:
        None se o valor de a ou b for negativo
        Se não retorna a soma de A e B
    """
    if a < 0 or b < 0:
        a = None
    elif b>0:
        a = exercicio_1_1(a+1, b-1)
    return a