def exercicio_1(data: str):
    meses = ("janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
    data_split = data.split("/")
    return f"{data_split[0]} de {meses[int(data_split[1])-1]} de {data_split[2]}"
