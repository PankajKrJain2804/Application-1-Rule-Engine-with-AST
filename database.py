import sqlite3

def setup_database():
    connection = sqlite3.connect('rules.db')
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rule_string TEXT,
        ast_json TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rule_id INTEGER,
        key TEXT,
        value TEXT,
        FOREIGN KEY(rule_id) REFERENCES rules(id)
    )''')
    
    connection.commit()
    connection.close()

if __name__ == '__main__':
    setup_database()
