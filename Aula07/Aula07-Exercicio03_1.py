def exercicio_3_1(n):
    if n <= 0:
        return
    sumOdd = 0 # Soma dos impares
    sumEven = 0 # Soma dos pares
    i = 0
    while i<=n:
        if i % 2 == 0:
            sumEven += i
        else:
            sumOdd += i
        i+=1
    return (sumEven, sumOdd)