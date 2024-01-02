        global conn
        with conn:
            with conn.cursor() as curs:
                curs.execute(open("../sql-scripts/test1.sql", "r").read())
                conn.commit()
                print('Your selected file is executed')
