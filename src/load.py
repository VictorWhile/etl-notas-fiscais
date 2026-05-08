# -*- coding: utf-8 -*-

import psycopg2
from dotenv import load_dotenv
import os
from logger import logger

load_dotenv()

def load_data(data):

    conn = None

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        cursor = conn.cursor()

        for item in data:

            numero_nota = item[0]

            # verifica se a nota ja existe
            cursor.execute(
                """
                SELECT 1
                FROM notas_fiscais
                WHERE numero_nota = %s
                """,
                (numero_nota,)
            )

            nota_existe = cursor.fetchone()

            if nota_existe:
                logger.warning(f"Nota {numero_nota} ja existe no banco.")
                continue

            query = """
            INSERT INTO notas_fiscais
            (
                numero_nota,
                data_emissao,
                cliente,
                valor,
                imposto
            )
            VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(query, item)

            logger.info(f"Nota {numero_nota} inserida com sucesso!")

        conn.commit()

    except Exception as error:
        logger.error(f"Erro ao inserir dados: {error}")

    finally:
        if conn:
            cursor.close()
            conn.close()

            logger.info("Conexao encerrada.")