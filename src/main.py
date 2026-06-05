# -*- coding: utf-8 -*-

from export_csv import export_to_csv

from extract import extract_data
from extract_xml import extract_xml_data

from transform import transform_data
from load import load_data

def main():

    # =========================
    # JSON
    # =========================

    json_data = extract_data('../data/notas.json')

    # =========================
    # XML
    # =========================

    xml_data = extract_xml_data()

    # =========================
    # UNIR DADOS
    # =========================

    all_data = json_data + xml_data

    if not all_data:
        return

    # =========================
    # TRANSFORM
    # =========================

    transformed = transform_data(all_data)

    if not transformed:
        return

    # =========================
    # LOAD
    # =========================

    load_data(transformed)
    
    export_to_csv(transformed)

if __name__ == "__main__":
    main()