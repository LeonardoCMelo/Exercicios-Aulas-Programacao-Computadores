def exercicio_2(representacao):
    if not representacao:  # vazia
        result = (0, 0)
    else:
        vogais = "aeiouAEIOU"
        total_vogais = 0
        total_consoantes = 0

        if type(representacao) == tuple and len(representacao) == 2:
            letras = representacao[0]
            quantidades = representacao[1]
            for i in range(len(letras)):
                letra = letras[i]
                qtd = quantidades[i]
                if letra in vogais:
                    total_vogais += qtd
                elif letra.isalpha():
                    total_consoantes += qtd

        elif type(representacao) == list and len(representacao) > 0 and type(representacao[0]) == str:
            for i in range(0, len(representacao), 2):
                letra = representacao[i]
                qtd = representacao[i + 1]
                if letra in vogais:
                    total_vogais += qtd
                elif letra.isalpha():
                    total_consoantes += qtd

        elif type(representacao) == list and len(representacao) > 0 and type(representacao[0]) == tuple:
            for par in representacao:
                letra = par[0]
                qtd = par[1]
                if letra in vogais:
                    total_vogais += qtd
                elif letra.isalpha():
                    total_consoantes += qtd

        else:
            result = (0, 0)

        result = (total_vogais, total_consoantes)
    return result
