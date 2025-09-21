def exercicio_1_5(a,b):
    """
    Calcula a multiplicação de forma recursiva
    
    Parâmetros:
        a: Base
        b: Expoente
    
    Retorno:
        None se o valor de a ou b for negativo
        1 se o valor de b for 0 ou o valor de a for 1
        Se não retorna a multiplicação de A por B
    """
    if a < 0 or b < 0:
        return None
    if b == 0 or a == 1:
        return 1
    return a * exercicio_1_5(a, b-1)