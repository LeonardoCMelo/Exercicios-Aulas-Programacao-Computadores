def exercicio_5_1_2(n):
    result = 0
    if n < 0:
        result = None
    else:
        for i in range(0,n):
            result = (1 + result)**(1/2)
    return result