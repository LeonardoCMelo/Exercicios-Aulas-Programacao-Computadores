def exercicio_5_3(n: int):
    pascal = [[1]]
    
    for i in range(1, n):
        anterior = pascal[-1]
        nova = [1]
        for j in range(len(anterior) - 1):
            nova.append(anterior[j] + anterior[j + 1])
        nova.append(1)
        pascal.append(nova)
    
    linhas = []
    i = 0
    for linha in pascal:
        if i < n - 1:
            alinhamento = '\t' * (n - i - 1)
        else:
            alinhamento = ''
        
        conteudo = ""
        for j in range(len(linha)):
            conteudo += str(linha[j])
            if j < len(linha) - 1:
                conteudo += "\t\t"
        
        linhas.append(alinhamento + conteudo)
        i += 1
    
    resultado = '\n'.join(linhas)
    return resultado
