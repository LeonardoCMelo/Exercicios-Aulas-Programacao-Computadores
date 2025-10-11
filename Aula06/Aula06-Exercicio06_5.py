def FindChar(string, searchChar):
    for i in range(0, len(string)):
        if searchChar == string[i]:
            return i
    return -1

def exercicio_5(hora1, hora2):
    hour1 = int(hora1[: FindChar(hora1, ":")])
    minutes1 = int(hora1[FindChar(hora1, ":") + 1 :]) 
    hour2 = int(hora2[: FindChar(hora2, ":")])
    minutes2 = int(hora2[FindChar(hora2, ":") + 1 :])
    
    totalMin1 = hour1 * 60 + minutes1
    totalMin2 = hour2 * 60 + minutes2

    if totalMin1 <= totalMin2:
        dif = totalMin2 - totalMin1
    else:
        dif = (24*60 - totalMin1) + totalMin2

    return f"{(dif//60):02d}:{(dif%60):02d};{dif};{dif*60}"