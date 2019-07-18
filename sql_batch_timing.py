import mysql.connector
from mysql.connector import Error
import time
import datetime
import glob, os
import sys


def get_date():
    timing = datetime.datetime.now().strftime("%H:%M:%S")
    return "[" + timing + "]"


def output_file(file, sql_record, start_time, end_time):
    file_name = file + "_output.txt"
    sample = open(file_name, "w")
    print(file, file=sample)
    print("Start:", start_time, file=sample)
    print("End:  ", end_time, file=sample)
    print(sql_record, file=sample)
    sample.close()


def do_query(file, sql_query):
    start_time = get_date()
    print("Start time:", start_time)
    try:
        mySQLconnection = mysql.connector.connect(
            host="",
            database="",
            user="",
            password="",
        )
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_query)
        records = cursor.fetchall()

        qSize = len(records)
        print("Query Size:", qSize)

        # if non zero set output content to a file
        if qSize != 0:
            output_file(file, records, start_time, get_date())
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if mySQLconnection.is_connected():
            mySQLconnection.close()
            print("MySQL connection is closed")

    end_time = get_date()
    print("End time:", end_time)


def get_stats():
    print()


def main():
    directory = sys.argv[1]
    os.chdir(directory)
    for file in glob.glob("*.sql"):
        print("=== Starting run for:", file, "===")
        f = open(file, "r")
        sql_query = f.read()
        do_query(file, sql_query)
        get_stats()


if __name__ == "__main__":
    main()
