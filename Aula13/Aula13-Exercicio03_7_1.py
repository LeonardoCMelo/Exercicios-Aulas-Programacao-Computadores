def exercicio_3_7_1(texto):
    resultado = ""
    vogais = "aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛ"
    
    for char in texto:
        if char not in vogais:
            resultado += char
            
    return resultado
