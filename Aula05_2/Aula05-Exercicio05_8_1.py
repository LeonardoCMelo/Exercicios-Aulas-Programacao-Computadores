def exercicio_5_8_1(n):
    def sqrt3(n):
        if n < 0:
            result = None
        elif n == 0:
            result = 1
        else:
            result = 1/((1 if n%2 == 0 else 2 ) + sqrt3(n-1))
        return result
    return sqrt3(n) + 1

print(exercicio_5_8_1(400))