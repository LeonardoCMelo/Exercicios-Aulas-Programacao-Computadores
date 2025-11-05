def exercicio_5_2():
    length = []
    string = ""
    for i in range(4):
        length.append(len(str(20**(i+1))))
    print(length)
    for i in range(1,21):
        for j in range(1,5):
            string += f"{(i**j):>{length[j-1]}}" + ' '
        string += "\n"
    return string[:-1]
