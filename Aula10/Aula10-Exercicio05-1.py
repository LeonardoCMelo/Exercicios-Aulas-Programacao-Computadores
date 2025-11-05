def exercicio_5_1():
    string = ""
    for i in range(2,10):
        for j in range (1,10):
            string += f"{i} x {j} = {i*j}" + '\t'
        string += "\n"
    return string[:-1]
