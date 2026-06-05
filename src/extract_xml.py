# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

def extract_xml_data():

    try:

        tree = ET.parse('../data/notas.xml')

        root = tree.getroot()

        data = []

        for nota in root.findall('nota'):

            item = {
                "numero": nota.find('numero').text,
                "data": nota.find('data').text,
                "cliente": nota.find('cliente').text,
                "valor": float(nota.find('valor').text),
                "imposto": float(nota.find('imposto').text)
            }

            data.append(item)

        print("Extracao XML concluida!")

        return data

    except Exception as error:

        print(f"Erro na extracao XML: {error}")

        return []