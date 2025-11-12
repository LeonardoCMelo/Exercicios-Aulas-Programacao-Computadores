def exercicio_5_4(agenda: dict):
    result = ""
    for key, values in agenda.items():
        result += f"{key}: {'; '.join(values)};\n"
    return result
