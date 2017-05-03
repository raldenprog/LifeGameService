import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, login VARCHAR(50), email VARCHAR(50), password VARCHAR(50))')
con.commit()
cur.execute('INSERT INTO users (id, login, email, password) VALUES(NULL, "test", "test@test.test", "test")')
con.commit()
print (cur.lastrowid)

cur.execute('SELECT * FROM users')
print (cur.fetchall())
con.close()