def exercicio_1_4_1(cores):
    lista_plana = []
    lista_de_listas = []
    
    for cor1 in cores:
        for cor2 in cores:
            if cor1 != cor2:
                lista_plana.append(cor1)
                lista_plana.append(cor2)
                
                lista_de_listas.append([cor1, cor2])
                
    return (lista_plana, lista_de_listas)
