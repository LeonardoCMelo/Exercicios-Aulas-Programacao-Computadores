def exercicio_5_7_1(n):
    if n < 0:
        result = None
    elif n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        return exercicio_5_7_1(n-1) + exercicio_5_7_1(n-2)
    return result