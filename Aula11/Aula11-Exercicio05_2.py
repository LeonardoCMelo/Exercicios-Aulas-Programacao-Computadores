def exercicio_5_2(agenda: dict, nome: str, numero: str):
    result = None
    if nome == "":
        encontrado = False
        for pessoa, numeros in list(agenda.items()):
            if numero in numeros:
                numeros.remove(numero)
                encontrado = True
                if not numeros:
                    agenda.pop(pessoa)
        if encontrado:
            result = agenda
    elif numero == "":
        if nome in agenda:
            agenda[nome].clear()
            result = agenda
    elif nome in agenda and numero in agenda[nome]:
        agenda[nome].remove(numero)
        if not agenda[nome]:
            agenda.pop(nome)
        result = agenda

    return result
