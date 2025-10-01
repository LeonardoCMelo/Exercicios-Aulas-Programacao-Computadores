def exercicio_5_5_2(n):
    if n<0:
        result = None
    else:
        result = 3
        for i in range(1,n+1):
            term = 2*i
            result += (-1 if i%2 == 0 else 1)*(4/((term)*(term+1)*(term+2)))
    return result

print(exercicio_5_5_2(400))