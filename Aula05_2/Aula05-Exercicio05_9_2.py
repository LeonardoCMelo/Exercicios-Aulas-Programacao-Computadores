def exercicio_5_9_2(n):
    if n < 0:
        result = None
    else:
        result = 0
        for i in range(0,n):
            result = 1/(2 + result)
    return result + 1

print(exercicio_5_9_2(400))