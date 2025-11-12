def exercicio_3_1(representacao):
    if not representacao:  # vazia
        result = (0, 0)
    else:
        vogais = "aeiouAEIOU"
        total_vogais = []
        total_consoantes = []
        if type(representacao) == tuple and len(representacao) == 2:
            letras = representacao[0]
            quantidades = representacao[1]
            for i in range(len(letras)):
                letra = letras[i]
                qtd = quantidades[i]
                if letra in vogais:
                    total_vogais.append((letra, qtd))
                elif letra.isalpha():
                    total_consoantes.append((letra, qtd))

        elif type(representacao) == list and len(representacao) > 0 and type(representacao[0]) == str:
            for i in range(0, len(representacao), 2):
                letra = representacao[i]
                qtd = representacao[i + 1]
                if letra in vogais:
                    total_vogais.append((letra, qtd))
                elif letra.isalpha():
                    total_consoantes.append((letra, qtd))

        elif type(representacao) == list and len(representacao) > 0 and type(representacao[0]) == tuple:
            for par in representacao:
                letra = par[0]
                qtd = par[1]
                if letra in vogais:
                    total_vogais.append((letra, qtd))
                elif letra.isalpha():
                    total_consoantes.append((letra, qtd))

        else:
            result = (0, 0)

        for lista in (total_vogais, total_consoantes):
            trocou = True
            while trocou:
                trocou = False
                for i in range(len(lista) - 1):
                    if lista[i][0] > lista[i + 1][0]:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        trocou = True

        result = (total_vogais, total_consoantes)
    return result
