def exercicio_4(n):
    if n <= 0:
        return
    div = ''
    for i in range(1,n+1):
        if n % i == 0:
            div += str(i) + " "
    return div[:-1]