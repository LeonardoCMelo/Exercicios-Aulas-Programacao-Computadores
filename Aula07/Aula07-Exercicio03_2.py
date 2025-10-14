def exercicio_3_2(n):
    if n <= 0:
        return
    sumOdd = 0 # Soma dos impares
    sumEven = 0 # Soma dos pares
    for i in range(n+1):
        if i % 2 == 0:
            sumEven += i
        else:
            sumOdd += i
    return (sumEven, sumOdd)