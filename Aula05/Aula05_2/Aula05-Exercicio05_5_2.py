def fat(n):
    res = 1;
    for i in range(1,n+1):
        res *= i
    return res

def exercicio_5_5_2(n):
    result = 0
    if n < 0:
        result = None
    else:
        for i in range(0,n+1):
            result += (1 if i%2==0 else -1)/fat(i)
    return result

print(exercicio_5_5_2(400))