def exercicio_3_2(representacao, letra):
    if not representacao:
        result = None
    else:
        if type(representacao) == tuple and len(representacao) == 2:
            letras = representacao[0]
            quantidades = representacao[1]
            for i in range(len(letras)):
                if letras[i] == letra:
                    result = quantidades[i]

        elif type(representacao) == list and len(representacao) > 0 and type(representacao[0]) == str:
            for i in range(0, len(representacao), 2):
                if representacao[i] == letra:
                    result = representacao[i + 1]

        elif type(representacao) == list and len(representacao) > 0 and type(representacao[0]) == tuple:
            for par in representacao:
                if par[0] == letra:
                    result = par[1]
        else:
            result = None
    return result
