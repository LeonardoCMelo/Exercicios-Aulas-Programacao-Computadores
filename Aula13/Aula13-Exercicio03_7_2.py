def exercicio_3_7_2(texto):
    vogais = "aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛ"
    
    lista_sem_vogais = [char for char in texto if char not in vogais]
    return "".join(lista_sem_vogais)
