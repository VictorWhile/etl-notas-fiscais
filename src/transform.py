# -*- coding: utf-8 -*-

def transform_data(data):

    transformed = []

    try:
        for item in data:

            if item["valor"] < 0:
                print(f"Valor invalido na nota {item['numero']}")
                continue

            transformed.append((
                item["numero"],
                item["data"],
                item["cliente"],
                float(item["valor"]),
                float(item["imposto"])
            ))

        print("Transformacao concluida!")

        return transformed

    except Exception as error:
        print(f"Erro na transformacao: {error}")
        return []