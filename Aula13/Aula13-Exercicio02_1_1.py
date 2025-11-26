def exercicio_2_1_1(cores, objetos):
    resultado = []
    for cor in cores:
        for obj in objetos:
            resultado.append((cor, obj))
    return resultado
