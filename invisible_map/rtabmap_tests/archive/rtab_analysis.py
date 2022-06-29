import sqlite3

DATABASE_FILEPATH = 'test1.db'
RELEVANT_TABLES = 'Node'

class DatabaseConnector():
    def __init__(self, database_filepath):
        self.database_filepath = database_filepath
        self.connection = sqlite3.connect(database_filepath)
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def close_connection(self):
        self.connection.close()

    def query_table(self, table_name):
        query = f"""SELECT * FROM {table_name}"""
        return self.execute(query)
        # return self.cursor.fetchall()


def find_tables_in_database(databaseConnection):
    table_name_query = """SELECT name FROM sqlite_master WHERE type='table';"""
    table_names = databaseConnection.execute(table_name_query)
    return table_names


def main():
    databaseConnection = DatabaseConnector(DATABASE_FILEPATH)
    table_list = find_tables_in_database(databaseConnection)
    print(table_list)
    print(databaseConnection.query_table(RELEVANT_TABLES)[0])
    databaseConnection.close_connection()

if __name__ == "__main__":
    main()