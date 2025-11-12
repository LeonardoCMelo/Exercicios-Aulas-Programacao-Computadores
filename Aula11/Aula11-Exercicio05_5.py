def exercicio_5_5(agenda: dict, nome: str):
    if nome not in agenda:
        return None
    telefones = "; ".join(agenda[nome])
    return f"{telefones};"
