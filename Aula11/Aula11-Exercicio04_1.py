def exercicio_4_1(string: str):
    if string == "":
        result = None
    else:
        result = {}
        for c in string:
            if c.isalpha():
                result[c] = result.get(c, 0) + 1
    return result
