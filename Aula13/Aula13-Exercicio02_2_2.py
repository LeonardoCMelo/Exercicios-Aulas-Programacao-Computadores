def exercicio_2_2_2(lista_cores_objetos):
    dict_cor_chave = {cor: obj for cor, obj in lista_cores_objetos}
    
    dict_objeto_chave = {obj: cor for cor, obj in lista_cores_objetos}
    
    return (dict_cor_chave, dict_objeto_chave)
