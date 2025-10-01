def exercicio3(n):
    sinal = 1
    if n<=0:
        result = None
    elif n==1:
        result = 1
    else:
        result = 0
        for i in range(1, n+1):
            result += sinal/i
            sinal = -sinal
    return result