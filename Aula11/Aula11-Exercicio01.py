def exercicio_1(string: str, numero_da_representacao: int):
    if numero_da_representacao not in range(1,4):
        result = None
    else:
        count = {}
        for c in string:
            if c.isalpha():
                count[c] = count.get(c, 0) + 1

        if numero_da_representacao == 1:
            letras = list(count.keys())
            quantidades = list(count.values())
            result = (letras, quantidades)

        elif numero_da_representacao == 2:
            resultado = []
            for letra, qtd in count.items():
                resultado.extend([letra, qtd])
            result = resultado

        elif numero_da_representacao == 3:
            result = list(count.items())
    return result
