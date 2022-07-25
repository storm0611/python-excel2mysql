# Construction DB

from getpass import getpass
from lib2to3.pgen2.token import N_TOKENS
from socket import NI_NAMEREQD
from mysql.connector import connect, Error
import numpy as np

try:

    # Establishing a Connection username ; root

    # with connect(
    #     host="localhost",
    #     user=input("Enter username: "),
    #     password=getpass("Enter password: "),
    # ) as connection:
    #     print(connection)

    # # Creating New Database named 'mysql_db'
    # create_db_query = "CREATE DATABASE mysql_db"
    # with connection.cursor() as cursor:
    #     cursor.execute(create_db_query)

    connection = connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database='mysql_db'
    )
    print(connection)
    global table_name
    table_name = 'dati1_table'
    # # Create table named 'dati1_table'
    # create_table_query = """
    #     CREATE TABLE dati1_table  (
    #         numeroRiga INT(255) NOT NULL,
    #         numeroGE INT(255) NOT NULL,
    #         ultimaVisita DATE NOT NULL,
    #         deltaTmax INT(255) NOT NULL,
    #         nextDeadline DATE NOT NULL,
    #         nextDeadlineN INT(255) NOT NULL,
    #         loc VARCHAR(255) NOT NULL,
    #         cap INT(255) NULL DEFAULT NULL,
    #         re VARCHAR(2) NOT NULL,
    #         coord VARCHAR(255) NOT NULL,
    #         lat DOUBLE NOT NULL,
    #         long_ DOUBLE NOT NULL,
    #         PRIMARY KEY (numeroRiga) USING BTREE
    #     )
    # """
    # with connection.cursor() as cursor:
    #     cursor.execute(create_table_query)
    #     connection.commit()

    # # Insert data from excel to database table
    # from sqlalchemy import create_engine
    # import pandas as pd
    # excel_data = pd.read_excel(r'dati.xltx', sheet_name='Rubr')
    # for i in range(len(excel_data)):
    #     insert_query = "INSERT INTO dati1_table VALUES("
    #     insert_query += str(excel_data.iloc[i]['NumeroRiga']) + ", "
    #     insert_query += str(excel_data.iloc[i]['NumeroGE']) + ", "
    #     insert_query += "'" + \
    #         str(excel_data.iloc[i]['ultima_visita']) + "'" + ", "
    #     insert_query += str(excel_data.iloc[i]['deltaTmax']) + ", "
    #     insert_query += "'" + \
    #         str(excel_data.iloc[i]['next_deadline_']) + "'" + ", "
    #     insert_query += str(excel_data.iloc[i]['next_deadline']) + ", "
    #     insert_query += "'" + str(excel_data.iloc[i]['Loc']) + "'" + ", "
    #     if str(excel_data.iloc[i]['CAP']) == 'nan':
    #         insert_query += '0'
    #     else:
    #         insert_query += str(excel_data.iloc[i]['CAP'])
    #     insert_query += ", "
    #     insert_query += "'" + str(excel_data.iloc[i]['Re']) + "'" + ", "
    #     insert_query += "'" + str(excel_data.iloc[i]['coord']) + "'" + ", "
    #     insert_query += str(excel_data.iloc[i]['lat']) + ", "
    #     insert_query += str(excel_data.iloc[i]['long'])
    #     insert_query += ")"
    #     print(insert_query)
    #     with connection.cursor() as cursor:
    #         cursor.execute(insert_query)
    #         connection.commit()
    lat = []
    long_ = []

    n_next = 50
    select_query = "SELECT * FROM " + table_name
    print(select_query)
    cursor = connection.cursor()
    cursor.execute(select_query)
    result = cursor.fetchmany(n_next)
    for row in result:
        # print(row[0], row[1], row[2])
        lat.append(row[10])
        long_.append(row[11])
    print(lat)
    print(long_)

except Error as e:
    print(e)
