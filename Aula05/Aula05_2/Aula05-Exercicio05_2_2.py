def exercicio_5_2_2(n):
    result = 0
    if n < 0:
        result = None
    else:
        for i in range(0,n):
            result = 1/(1+result)
    return result + 1

print(exercicio_5_2_2(400))