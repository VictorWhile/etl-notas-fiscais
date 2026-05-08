# -*- coding: utf-8 -*-

import json

def extract_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        print("Dados extraidos com sucesso!")

        return data

    except Exception as error:
        print(f"Erro na extracao dos dados: {error}")
        return []