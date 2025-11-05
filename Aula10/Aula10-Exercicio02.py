def exercicio_2(texto: str):
    contEspacos = texto.count(' ')
    vogais = "AEIOU"
    vogais = vogais+vogais.lower()
    consoantes = "BCDFGHJKLMNPQRSTVWXYZ"
    consoantes = consoantes + consoantes.lower()
    pontuacoes = "?!.;:\n"
    listaVogais = []
    listaConsoantes = []
    listaPontuacoes = []
    for v in vogais:
        contVogal = texto.count(v)
        if contVogal!=0:
            listaVogais.append((v, contVogal))

    for c in consoantes:
        contConsoante = texto.count(c)
        if contConsoante!=0:
            listaConsoantes.append((c, contConsoante))

    for p in pontuacoes:
        contPontuacao = texto.count(p)
        if contPontuacao!=0:
            listaConsoantes.append((p, contPontuacao))
    return ([' ', contEspacos], listaVogais, listaConsoantes, listaPontuacoes)
