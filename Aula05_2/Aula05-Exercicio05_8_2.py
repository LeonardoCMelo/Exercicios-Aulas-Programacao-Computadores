def exercicio_5_8_2(n):
    if n < 0:
        result = None
    else:
        result = 0
        for i in range(1,n+1):
            result = 1/((1 if i%2 == 0 else 2 ) + result)
    return result + 1

print(exercicio_5_8_2(400))