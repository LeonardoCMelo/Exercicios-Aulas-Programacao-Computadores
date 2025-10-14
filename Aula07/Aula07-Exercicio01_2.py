def exercicio_1_2(n):
    if n <= 0:
        return
    ans = True
    while ans != "N" or ans != "n":
        for i in range(n):
            print(i)
            ans = input("Quer continuar? ([Ss]/Nn) ")
            if ans == "N" or ans == "n":
                print("Fim")
                return