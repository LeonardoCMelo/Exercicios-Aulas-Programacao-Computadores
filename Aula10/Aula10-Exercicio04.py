def exercicio_4(n: int):
    numero = ""

    if not (0 <= n <= 100):
        return "numero fora do intervalo"

    unidades = [
        "zero", "um", "dois", "tres", "quatro", "cinco", "seis",
        "sete", "oito", "nove"
    ]

    especiais = [
        "dez", "onze", "doze", "treze", "quatorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove"
    ]

    dezenas = [
        "", "", "vinte", "trinta", "quarenta", "cinquenta",
        "sessenta", "setenta", "oitenta", "noventa"
    ]

    if n < 10:
        numero = unidades[n]
    elif 10 <= n < 20:
        numero = especiais[n - 10]
    elif n < 100:
        dezena = n // 10
        unidade = n % 10
        if unidade == 0:
            numero = dezenas[dezena]
        else:
            numero = f"{dezenas[dezena]} e {unidades[unidade]}"
    else:
        numero = "cem"
    
    return numero
