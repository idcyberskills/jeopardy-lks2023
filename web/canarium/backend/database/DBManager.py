import mysql.connector

class DBManager:
    def __init__(self, database='example', host="db", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password=pf.read(),
            host=host, # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        pf.close()
        self.cursor = self.connection.cursor(dictionary=True, buffered=True)
    
    def populate_db(self):
        self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute('DROP TABLE IF EXISTS canary_blacklist')
        self.cursor.execute('DROP TABLE IF EXISTS canary')

        self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
        self.cursor.execute('CREATE TABLE canary_blacklist (id INT AUTO_INCREMENT PRIMARY KEY, canary_id VARCHAR(255), since DATETIME, is_valid BOOLEAN)')
        self.cursor.execute('CREATE TABLE canary (id INT AUTO_INCREMENT PRIMARY KEY, canary_id VARCHAR(255), user_agent VARCHAR(255), ip_address VARCHAR(255))')

        self.cursor.execute('INSERT INTO blog (id, title) VALUES (%s, %s);', (1, 'Black Silk (International Bestseller)'))
        self.cursor.execute('INSERT INTO blog (id, title) VALUES (%s, %s);', (2, 'The History of KFC'))
        self.cursor.execute('INSERT INTO blog (id, title) VALUES (%s, %s);', (3, 'Tell Me to Rise Up Again'))
        self.cursor.execute('INSERT INTO blog (id, title) VALUES (%s, %s);', (4, 'Mystery of the Pale Cricketeer'))
        self.cursor.execute('INSERT INTO blog (id, title) VALUES (%s, %s);', (5, 'Dos Vamos'))

        self.connection.commit()
    
    def query_titles(self):
        self.cursor.execute('SELECT * FROM blog')
        rec = []
        for c in self.cursor:
            rec.append(c)
        return rec

    def query_canary_entry(self, canary_id):
        if not canary_id:
            return None
        
        query = "SELECT * FROM canary WHERE canary_id = %s;"
        print(query, canary_id)
        
        self.cursor.execute(query, (canary_id, ))
        return self.cursor.fetchone()
    
    def query_canary_blacklist(self, canary_id):
        if not canary_id:
            return None
        
        query = "SELECT * FROM canary_blacklist WHERE canary_id = %s;"
        print(query, canary_id)

        self.cursor.execute(query, (canary_id, ))
        return self.cursor.fetchone()
    
    