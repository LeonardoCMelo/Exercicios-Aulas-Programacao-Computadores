def fat(n):
    res = 1;
    for i in range(1,n+1):
        res *= i
    return res

def exercicio_5_4_1(n,x):
    if n < 0:
        result = None
    elif n == 0:
        result = 1
    else:
        result = (x**n)/fat(n) + exercicio_5_4_1(n-1,x)
    return result

print(exercicio_5_4_1(400,3))