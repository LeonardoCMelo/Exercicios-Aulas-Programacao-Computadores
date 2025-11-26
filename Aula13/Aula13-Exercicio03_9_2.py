def exercicio_3_9_2(ini: int, fim: int) -> dict[int, int]:
    resultado = {
        n: next(d for d in range(9, 0, -1) if n % d == 0)
        for n in range(ini, fim + 1)
    }
    
    return resultado
