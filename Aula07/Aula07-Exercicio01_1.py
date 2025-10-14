def exercicio_1_1(n):
    if n <= 0:
        return
    ans = ""
    i = 0
    while ans != "N" or ans != "n":
        print(i)
        ans = input("Quer continuar? ([Ss]/Nn) ")
        i = (i + 1) % n
    print("Fim")
    return