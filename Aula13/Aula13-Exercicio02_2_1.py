def exercicio_2_2_1(lista_cores_objetos):
    dict_cor_chave = {}
    dict_objeto_chave = {}
    
    for cor, objeto in lista_cores_objetos:
        
        dict_cor_chave[cor] = objeto
        
        dict_objeto_chave[objeto] = cor
        
    return (dict_cor_chave, dict_objeto_chave)
