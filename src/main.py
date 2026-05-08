# -*- coding: utf-8 -*-

from extract import extract_data
from transform import transform_data
from load import load_data

def main():

    data = extract_data('../data/notas.json')

    if not data:
        return

    transformed = transform_data(data)

    if not transformed:
        return

    load_data(transformed)

if __name__ == "__main__":
    main()