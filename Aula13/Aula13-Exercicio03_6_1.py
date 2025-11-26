def exercicio_3_6_1(texto):
    contador = 0
    for char in texto:
        if char == ' ':
            contador += 1
    return contador
