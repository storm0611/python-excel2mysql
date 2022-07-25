import threading
import time
import keyboard
import pandas as pd
from getpass import getpass
from mysql.connector import connect, Error


exitFlag = 0

# Delete old table


def delete_table_data():
    delete_query = "DELETE FROM dati1_table"
    with connection.cursor() as cursor:
        cursor.execute(delete_query)
        connection.commit()

# Insert data from excel to database table


def insert_excel2db(excel_data):
    for i in range(len(excel_data)):
        insert_query = "INSERT INTO dati1_table VALUES("
        insert_query += str(excel_data.iloc[i]['NumeroRiga']) + ", "
        insert_query += str(excel_data.iloc[i]['NumeroGE']) + ", "
        insert_query += "'" + \
            str(excel_data.iloc[i]['ultima_visita']) + "'" + ", "
        insert_query += str(excel_data.iloc[i]['deltaTmax']) + ", "
        insert_query += "'" + \
            str(excel_data.iloc[i]['next_deadline_']) + "'" + ", "
        insert_query += str(excel_data.iloc[i]['next_deadline']) + ", "
        insert_query += "'" + str(excel_data.iloc[i]['Loc']) + "'" + ", "
        if str(excel_data.iloc[i]['CAP']) == 'nan':
            insert_query += '0'
        else:
            insert_query += str(excel_data.iloc[i]['CAP'])
        insert_query += ", "
        insert_query += "'" + str(excel_data.iloc[i]['Re']) + "'" + ", "
        insert_query += "'" + str(excel_data.iloc[i]['coord']) + "'" + ", "
        insert_query += str(excel_data.iloc[i]['lat']) + ", "
        insert_query += str(excel_data.iloc[i]['long'])
        insert_query += ")"
        print(insert_query)
        with connection.cursor() as cursor:
            cursor.execute(insert_query)
            connection.commit()


class myThread (threading.Thread):
    def __init__(self, threadID, name, delayTime):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delayTime = delayTime

    def run(self):
        print("Starting " + self.name)

        data = pd.read_excel('dati1.xlsx', sheet_name='Rubr')

        while not exitFlag:
            # Check file is modified
            data_new = pd.read_excel('dati1.xlsx', sheet_name='Rubr')
            if not data_new.equals(data):
                # Delete all data from table
                delete_table_data()
                data = data_new
                # Insert new data to table
                insert_excel2db(data)
            time.sleep(self.delayTime)
            print(self.name, time.ctime(time.time()))

        print("Exiting " + self.name)


if __name__ == "__main__":
    try:
        # Connect table in db

        global connection

        with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            database='mysql_db'
        ) as connection:
            print(connection)

            # Create new threads
            check_file_thread = myThread(0, "Thread-1", 0.5)

            # Start new Threads
            check_file_thread.start()

            while check_file_thread.is_alive():
                if keyboard.is_pressed("esc"):
                    exitFlag = 1

            print("Exiting Main Thread")

    except Error as e:
        print(e)
