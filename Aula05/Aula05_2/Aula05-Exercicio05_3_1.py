def fat(n):
    res = 1;
    for i in range(1,n+1):
        res *= i
    return res

def exercicio_5_3_1(n):
    if n < 0:
        result = None
    elif n == 0:
        result = 1
    else:
        result = 1/fat(n) + exercicio_5_3_1(n-1)
    return result

print(exercicio_5_3_1(400))