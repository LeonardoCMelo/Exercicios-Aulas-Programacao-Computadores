def exercicio_1_4_2(cores):
    plana = [item for c1 in cores for c2 in cores if c1 != c2 for item in (c1, c2)]
    
    listas = [[c1, c2] for c1 in cores for c2 in cores if c1 != c2]
    
    return (plana, listas)
