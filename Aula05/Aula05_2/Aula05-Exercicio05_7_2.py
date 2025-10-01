def exercicio_5_7_2(n):
    if n == 0: 
        result = 0
    elif n == 1:
        result = 1
    else:
        a = 0
        b = 1
        for i in range(2,n+1):
            temp = a+b
            a = b
            b = temp
        result = b
    return result