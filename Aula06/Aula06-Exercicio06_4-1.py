def exercicio_4_1(string):
    if len(string) <=1:
        result = True
    elif string[0] != string[-1]:
        result = False
    else:
        result = exercicio_4_1(string[1:-1])
    return result