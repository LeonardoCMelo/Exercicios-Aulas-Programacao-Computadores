def exercicio_6_2(numero:str):
    inteiro = 0
    for i in range(0,len(numero)):
        inteiro += (ord(numero[i])-ord("0")) * (10**(len(numero)-i-1))
    return inteiro

print(exercicio_6_2('12345'))