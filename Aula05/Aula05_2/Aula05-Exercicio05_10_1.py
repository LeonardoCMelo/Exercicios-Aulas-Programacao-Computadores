def exercicio_5_10(n):
    seq = [5, 2, 3]

    def rec(k):
        if k == n:
            return 1 / (10 ** n)
        else:
            termo = seq[(k - 1) % len(seq)]
            return termo + 1 / rec(k + 1)

    return rec(1)
