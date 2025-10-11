def exercicio_6_1(numero):
    resultado = 0
    if len(numero) == 0:
        resultado = 0
    else:
        resultado = (ord(numero[0])-ord("0"))*(10**(len(numero)-1)) + exercicio_6_1(numero[1:])
    return resultado

print(exercicio_6_1("12345"))