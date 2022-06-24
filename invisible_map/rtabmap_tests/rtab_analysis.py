import sqlite3

DATABASE_FILEPATH = 'rtabmap_tests/220624-120055.db'

def find_tables_in_database():
    try:
        databaseConnection = sqlite3.connect(DATABASE_FILEPATH)
    except:
        print("could not connect to specified databse")
        return None
    table_name_query = """SELECT name FROM sqlite_master WHERE type='table';"""
    cursor = databaseConnection.cursor()
    cursor.execute(table_name_query)
    table_names = cursor.fetchall()
    databaseConnection.close()
    return table_names


def main():
    table_list = find_tables_in_database()
    print(table_list)

if __name__ == "__main__":
    main()