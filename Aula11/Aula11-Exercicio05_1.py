def exercicio_5_1(agenda: dict, nome:str, numero:str):
    if nome == "" or numero == "":
        result = agenda
    else:
        agenda[nome] = numero
    return result