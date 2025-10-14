def exercicio_7_1(n):
    def soma_rec(val):
        result = 0.0
        if val == 1:
            result = 1 / 1
        else:
            result = (2 * val - 1) / val + soma_rec(val - 1)
        return result
    return soma_rec(n)