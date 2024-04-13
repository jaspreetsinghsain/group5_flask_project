import sqlite3
import csv
def create_database(database_name):
    conn = sqlite3.connect(database_name)
    conn.close

def create_table(table_name, columns):
    conn = sqlite3.connect('customer_database.db')
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({columns});")
    conn.commit()
    conn.close()

def insert_data_csv(table_name,csv_file):
    conn = sqlite3.connect('customer_database.db')
    cursor = conn.cursor()

    with open(csv_file,'r') as file:
        data = csv.reader(file)
        next(data)
        
        for row in data:
            cursor.execute(f"REPLACE INTO {table_name} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
    conn.commit()
    conn.close()