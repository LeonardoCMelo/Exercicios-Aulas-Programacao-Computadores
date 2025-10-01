import math
def exercicio_5_11_1(n,x):
    def tan(n, x, k):
        if n<0:
            result = None
        elif n == 0:
            result = 1
        else:
            result = (k / x) - (1 / tan(n - 1, x, k+2))
        return result
    return 1/tan(n,x,1)
print(exercicio_5_11_1(20,3.14/4))