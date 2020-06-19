import psycopg2

DB_NAME = "ulmhklzy"
DB_USER = "ulmhklzy"
DB_PASS = "L7hi0Sy1mW0EcEQNj-BKHv4de1OHXf3h"
DB_HOST = "rogue.db.elephantsql.com"
DB_PORT = "5432"

"""
TO DO:
create table (id, num days from beg, date, price , class, name)
"""

def postgre_sql_connection():
    """ connection to database """
    try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                                host=DB_HOST, port=DB_PORT)

        print('Database connected sucessfully')

    except:
        print('Database not connected ')

def postgre_sql_creating_table():
    """ creating table """

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                            host=DB_HOST, port=DB_PORT)

    print('Database connected sucessfully')

    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE cellphone_database
    (
    ID INT PRIMARY KEY NOT NULL,
    Num_of_days INT NOT NULL,
    Date DATE NOT NULL,
    Price FLOAT(2) NOT NULL,
    Class INT NOT NULL,
    Name TEXT NOT NULL
    )
    """)

    conn.commit()
    print('Table created sucesuffly')

def postgre_sql_inerting_data():
    """ insertion_data """

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                            host=DB_HOST, port=DB_PORT)

    print('Database connected sucessfully')

    # (ID, Num_of_days, Date, Price, Class, Name) VALUES(0, 0, '2016-06-01', 264.91, 2, 'Huawei P9 Lite')
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO cellphone_database
    
    (ID, Num_of_days, Date, Price, Class, Name) VALUES(1, 1, '2016-06-02', 265.91, 2, 'Huawei P9 Lite')  
    """)


    conn.commit()
    print('Data inserted sucesuffly')
    conn.close()

def postgre_sql_selecting_data():
    """ insertion_data """

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                            host=DB_HOST, port=DB_PORT)

    print('Database connected sucessfully')

    cur = conn.cursor()
    cur.execute("""
    SELECT ID, Num_of_days, Date, Price, Class, Name FROM cellphone_database
    """)

    rows = cur.fetchall()

    for data in rows:
        print("ID : " + str(data[0]))
        print("Num_of_days : " + str(data[1]))
        print("Date : " + str(data[2]))
        print("Price : " + str(data[3]))
        print("Class : " + str(data[4]))
        print("Name : " + str(data[5]))

    print('Data selected sucesuffly')
    conn.close()

def postgre_sql_updating_data():
    """ insertion_data """

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                            host=DB_HOST, port=DB_PORT)

    print('Database connected sucessfully')

    cur = conn.cursor()
    cur.execute("""
    UPDATE Test SET EMAIL = 'update@gmail.com' WHERE ID = 1
    """)

    conn.commit()

    print('Data updated sucesuffly')
    print('Total row affected: ' + str(cur.rowcount))
    conn.close()


def postgre_sql_deleting_data():
    """ deleting_data from table """

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                            host=DB_HOST, port=DB_PORT)

    print('Database connected sucessfully')

    cur = conn.cursor()
    cur.execute("""
    DELETE FROM cellphone_database
    """)

    conn.commit()

    print('Data deleted sucesuffly')
    # print('Total row affected: ' + str(cur.rowcount))
    conn.close()


def postgre_sql_populating_table():
    """ populating_table """

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                            host=DB_HOST, port=DB_PORT)

    print('Database connected sucessfully')


    # (ID, Num_of_days, Date, Price, Class, Name) VALUES(0, 0, '2016-06-01', 264.91, 2, 'Huawei P9 Lite')
    cur = conn.cursor()
    # cur.execute("""
    # COPY cellphone_database FROM '/data/test_sql.csv' DELIMITER ',' CSV;
    # """)
    f = open(r'C:\Users\Greg\PycharmProjects\Projects\WhenShouldIBuy\data\out_concat.csv', 'r')
    cur.copy_from(f, 'cellphone_database', sep=',')
    f.close()

    conn.commit()
    print('Data inserted sucesuffly')
    conn.close()

def postgre_sql_copy_table_to_csv_file():
    """ populating_table """

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                            host=DB_HOST, port=DB_PORT)

    print('Database connected sucessfully')


    # (ID, Num_of_days, Date, Price, Class, Name) VALUES(0, 0, '2016-06-01', 264.91, 2, 'Huawei P9 Lite')
    cur = conn.cursor()
    # cur.execute("""
    # COPY cellphone_database TO STDOUT DELIMITER ',' CSV;
    # """)

    f = open(r'C:\Users\Greg\PycharmProjects\Projects\WhenShouldIBuy\data\out_concat.csv', 'w')
    cur.copy_to(f, 'cellphone_database', sep=',')
    f.close()
    # f = open(r'C:\Users\Greg\PycharmProjects\Projects\WhenShouldIBuy\data\test_sql.csv', 'r')
    # cur.copy_from(f, 'cellphone_database', sep=',')
    # f.close()

    conn.commit()
    print('Data inserted sucesuffly')
    conn.close()

# postgre_sql_connection()
# postgre_sql_creating_table()
# postgre_sql_inerting_data()
# postgre_sql_selecting_data()
# postgre_sql_updating_data()
# postgre_sql_deleting_data()
# postgre_sql_populating_table()
# postgre_sql_copy_table_to_csv_file()