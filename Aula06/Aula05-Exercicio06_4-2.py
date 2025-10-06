def exercicio_4_1(string):
    if len(string) <= 1:
        return True
    else:
        for i in range(0, len(string)):
            if string[i] != string[-(i+1)]:
                return False
        return True