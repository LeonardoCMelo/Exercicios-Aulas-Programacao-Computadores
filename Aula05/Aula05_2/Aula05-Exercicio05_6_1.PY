def exercicio_5_6_1(n):
    if n<0:
        result = None
    elif n==0:
        result = 3
    else:
        term = 2*n
        result = (-1 if n%2 == 0 else 1)*(4/((term)*(term+1)*(term+2))) + exercicio_5_6_1(n-1)
    return result

print(exercicio_5_6_1(400))