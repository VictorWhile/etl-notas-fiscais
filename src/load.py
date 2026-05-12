# -*- coding: utf-8 -*-

import psycopg2
from dotenv import load_dotenv
import os

from logger import logger
from validator import validate_data

load_dotenv()

def load_data(data):

    conn = None

    inseridas = 0
    duplicadas = 0
    erros_validacao = 0

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

            # =========================
            # VALIDACAO DOS DADOS
            # =========================

            valid, message = validate_data(item)

            if not valid:

                logger.error(
                    f"Erro de validacao: {message} | Dados: {item}"
                )

                print(f"Erro de validacao: {message}")

                erros_validacao += 1

                continue

            # =========================
            # VERIFICAR DUPLICIDADE
            # =========================

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

                logger.warning(
                    f"Nota {numero_nota} ja existe no banco."
                )

                print(f"Nota {numero_nota} ja existe no banco.")

                duplicadas += 1

                continue

            # =========================
            # INSERT
            # =========================

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

            logger.info(
                f"Nota {numero_nota} inserida com sucesso!"
            )

            print(f"Nota {numero_nota} inserida com sucesso!")

            inseridas += 1

        conn.commit()

        # =========================
        # RESUMO DA EXECUCAO
        # =========================

        logger.info("Resumo da execucao:")
        logger.info(f"Notas inseridas: {inseridas}")
        logger.info(f"Notas duplicadas: {duplicadas}")
        logger.info(f"Erros de validacao: {erros_validacao}")
        logger.info(f"Total processado: {len(data)}")

        print("\nResumo da execucao:")
        print(f"Notas inseridas: {inseridas}")
        print(f"Notas duplicadas: {duplicadas}")
        print(f"Erros de validacao: {erros_validacao}")
        print(f"Total processado: {len(data)}")

    except Exception as error:

        logger.error(f"Erro ao inserir dados: {error}")

        print(f"Erro ao inserir dados: {error}")

    finally:

        if conn:

            cursor.close()
            conn.close()

            logger.info("Conexao encerrada.")