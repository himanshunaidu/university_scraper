import mysql

class DBConnector:
    def __init__(self):
        self.db = 'university'
        self.universityDB = None
        self.universityDBCursor = None
    
    def connect(self):
        self.universityDB = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database=self.db
        )
    
    def insert(self, table, **kwargs):
        keys, values = [], []
        for key, value in kwargs:
            keys.append(key)
            values.append(value)
        
        query = f"INSERT INTO {table} {(','.join(keys))} VALUES {(','.join(['%s' for i in range(len(values))]))}"
        self.universityDBCursor.execute(query, values)
        self.universityDB.commit()
        print(self.universityDBCursor.rowcount, "record inserted.")

