# -*- coding: utf-8 -*-

import csv

def export_to_csv(data):

    try:

        with open(
            '../output/notas_exportadas.csv',
            mode='w',
            newline='',
            encoding='utf-8'
        ) as file:

            writer = csv.writer(file)

            # cabecalho
            writer.writerow([
                'numero_nota',
                'data_emissao',
                'cliente',
                'valor',
                'imposto'
            ])

            # dados
            writer.writerows(data)

        print("Exportacao CSV concluida!")

    except Exception as error:

        print(f"Erro ao exportar CSV: {error}")