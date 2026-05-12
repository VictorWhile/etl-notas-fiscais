from datetime import datetime

def validate_data(item):

    numero_nota = item[0]
    data_emissao = item[1]
    cliente = item[2]
    valor = item[3]
    imposto = item[4]

    # numero nota vazio
    if not numero_nota:
        return False, "Numero da nota vazio"

    # cliente vazio
    if not cliente:
        return False, "Cliente vazio"

    # valor invalido
    if valor <= 0:
        return False, "Valor deve ser maior que zero"

    # imposto invalido
    if imposto < 0:
        return False, "Imposto nao pode ser negativo"

    # validar data
    try:
        datetime.strptime(data_emissao, "%Y-%m-%d")
    except ValueError:
        return False, "Data invalida"

    return True, "Dados validos"