def exercicio_6_1():
    def soma_rec(n):
        result = 0.0
        if n == 1:
            result = 1 / 1
        else:
            result = (2 * n - 1) / n + soma_rec(n - 1)
        return result
    return soma_rec(50)