def exercicio_3(cpf: str):
    if len(cpf) != 14:
        valido = False
    elif cpf[3] != '.' and cpf[7] != '.' and cpf[-3] != '-':
        valido = False
    else:
        cpf = cpf[:3]+cpf[4:7]+cpf[8:11]+cpf[-2:]

        soma1 = 0
        for i in range(9):
            soma1 += int(cpf[i]) * (10 - i)
        digito1 = (soma1 * 10) % 11
        if digito1 == 10 or digito1 == 11:
            digito1 = 0

        soma2 = 0
        for i in range(9):
            soma2 += int(cpf[i]) * (11 - i)
        soma2 += digito1 * 2
        digito2 = (soma2 * 10) % 11

        if digito2 == 10 or digito2 == 11:
            digito2 = 0

        valido = cpf[-2:] == f'{digito1}{digito2}'

    return valido
