import sqlite3


class Database: 
    def __init__(self, db_file): 
        self.db_file = db_file
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def connect(self): 
        return sqlite3.connect(self.db_file)

    def create_table(self, tb_name, columns, drop=True):         
        if drop: 
            self.cursor.execute('DROP TABLE IF EXISTS {}'.format(tb_name))    
        self.cursor.execute('PRAGMA journal_mode = wal')
        self.cursor.execute('CREATE TABLE {tb_name} ({columns})'.format(tb_name=tb_name, columns=columns))
        return tb_name

    def insert(self, query, values, many=False): 
        if many: 
            self.cursor.executemany(query, values)
        else: 
            self.cursor.execute(query, values)
        
        

    def select(self, query): 
        self.cursor.execute(query)
        return self.cursor
        