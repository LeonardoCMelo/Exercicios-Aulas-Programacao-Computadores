import math
def exercicio_5_11_2(n,x):
    if n<0:
        result = None
    else:
        result = 1
        for i in range(n,0,-2):
            result = i/x - (1/result)
    return 1/result

print(exercicio_5_11_2(400, 3.14/4))