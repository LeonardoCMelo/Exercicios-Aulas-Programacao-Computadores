def exercicio_3_3(representacao, letra, codigo):
    result = None

    if codigo not in (0, -1):
        result = None

    else:
        if not representacao:
            result = None

        else:
            if type(representacao) == tuple and len(representacao) == 2:
                letras = representacao[0]
                contagens = representacao[1]

                if not letras or letra not in letras:
                    result = None
                else:
                    i = letras.index(letra)
                    if codigo == 0:
                        contagens[i] = 0
                    else:  # codigo == -1
                        letras.pop(i)
                        contagens.pop(i)
                    result = (letras, contagens)

            elif type(representacao) == list and type(representacao[0]) == list:
                achou = False
                for i in range(len(representacao)):
                    if representacao[i][0] == letra:
                        achou = True
                        if codigo == 0:
                            representacao[i][1] = 0
                        else:
                            representacao.pop(i)
                        break
                if achou:
                    result = representacao
                else:
                    result = None

            elif type(representacao) == list and type(representacao[0]) == tuple:
                achou = False
                for i in range(len(representacao)):
                    if representacao[i][0] == letra:
                        achou = True
                        if codigo == 0:
                            representacao[i] = (letra, 0)
                        else:
                            representacao.pop(i)
                        break
                if achou:
                    result = representacao
                else:
                    result = None

    return result
