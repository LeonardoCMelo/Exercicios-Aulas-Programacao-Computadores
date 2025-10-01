def exercicio_5_2_1(n):
    def calcPhi(n):
        result=0
        if n<0:
            result = None
        elif n==0:
            result = 1
        else:
            result = 1/(1+calcPhi(n-1))
        return result
    return calcPhi(n)+1 

print(exercicio_5_2_1(400))