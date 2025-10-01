def exercicio_5_1_1(n):
    result=0
    if n<0:
        result = None
    elif n==0:
        result = 1
    else:
        result = (1+exercicio_5_1_1(n-1))**(1/2)
    return result