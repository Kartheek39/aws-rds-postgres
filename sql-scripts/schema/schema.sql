def create_pagila_db():
    """
    Creates Pagila database by running DDL and DML scripts
    """

    try:
        global conn
        with conn:
            with conn.cursor() as curs:
                curs.execute(open("../sql-scripts/test1.sql", "r").read())
                conn.commit()
                print('Your selected file is executed')
