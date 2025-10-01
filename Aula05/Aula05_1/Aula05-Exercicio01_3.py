def exercicio_1_3(a,b):
    """
    Calcula a multiplicação de forma recursiva
    
    Parâmetros:
        a: Primeiro Termo
        b: Segundo Termo
    
    Retorno:
        None se o valor de a ou b for negativo
        0 se o valor de a ou b for 0
        Se não retorna a multiplicação de A por B
    """
    result = None
    if a < 0 or b < 0:
        result = None
    elif a == 0 or b == 0:
        result = 0
    elif b>0:
        result = a + exercicio_1_3(a, b-1)
    return result