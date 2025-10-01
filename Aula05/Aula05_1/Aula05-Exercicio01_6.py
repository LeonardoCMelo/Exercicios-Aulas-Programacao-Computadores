def exercicio_1_6(a,b):
    """
    Calcula o logaritmo inteiro (parte inteira de log_b(a)) de forma recursiva.

    Parâmetros:
        a: Base.
        b: Logaritmando.

    Retorno:
        Se a for menor ou igual a 1 ou b for menor ou igual a zero retorna None
        Se não retorna maior inteiro x tal que b^x <= a.
    """
    if a <= 1 or b <= 0:
        return None
    if b < a:   # caso base da recursão
        return 0
    return 1 + exercicio_1_6(a, b//a)