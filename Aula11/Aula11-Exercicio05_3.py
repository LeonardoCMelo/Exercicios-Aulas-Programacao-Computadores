def exercicio_5_3(agenda: dict, nome1: str, numero1: str, nome2: str, numero2: str) -> dict | None:
    result = None

    if nome1 != "" and numero1 != "" and nome2 != "" and numero2 != "":
        if nome1 in agenda.keys():
            agenda.pop(nome1)
        agenda[nome2] = [numero2] 
        result = agenda.copy()

    elif nome1 != "" and numero1 == "" and nome2 != "" and numero2 == "":
        temp_number = []
        if nome1 in agenda.keys():
            temp_number = agenda[nome1]
            agenda.pop(nome1)
        agenda[nome2] = temp_number
        result = agenda.copy()

    elif nome1 != "" and numero1 != "" and nome2 == "" and numero2 != "":
        if nome1 in agenda.keys():
            for i in range(len(agenda[nome1])):
                if agenda[nome1][i] == numero1:
                    agenda[nome1][i] = numero2
        result = agenda.copy()

    elif nome1 != "" and numero1 == "" and nome2 != "" and numero2 != "":
        if nome1 in agenda.keys():
            agenda.pop(nome1)
            agenda[nome2] = [numero2]
        result = agenda.copy()

    elif nome1 == "" and numero1 != "" and nome2 == "" and numero2 != "":
        for i in range(len(agenda)):
            for j in range(len(agenda[i])):
                if numero1 in agenda[i][j]:
                    agenda[i][j].remove(numero1)
                    agenda[i][j].append(numero2)
    
    elif nome1 == "" and numero1 != "" and nome2 != "" and numero2 != "":
        agenda[nome2].append([numero1, numero2,])
        result = agenda.copy()
    return result