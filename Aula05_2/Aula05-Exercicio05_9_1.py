def exercicio_5_10(n):
    def frac(k):
        if k == n:  
            result = 1 / (10 ** n)
        else:
            seq = [5, 2, 3]
            result = seq[(k - 1) % len(seq)] + 1 / frac(k + 1)
        return result
    return frac(1)
