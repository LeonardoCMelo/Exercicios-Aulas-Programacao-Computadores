def exercicio_5_11_1(n,):
    def neper(n,i):
        if n<0:
            result = None
        elif n == 0:
            result = 1
        else:
            result = i/(i+neper(n-1,i+1))   
        return result
    return 2 + (2/neper(n,2))
print(exercicio_5_11_1(400))