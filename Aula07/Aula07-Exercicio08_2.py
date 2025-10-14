def exercicio_8_2(a, b):
    if a > b or a == 5:
        return a
    a += 1
    if a != 5:
        print(f"a: {a}")
    return exercicio_8_2(a, b)
