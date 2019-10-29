import sqlite3


def init_db():
    conn = sqlite3.connect('steven.sqlite3')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE entries (inbound TEXT, command TEXT, item TEXT, price INTEGER)''')
    conn.commit()
    conn.close()


def add_entry(params):
    conn = sqlite3.connect('steven.sqlite3')
    cur = conn.cursor()
    cur.execute('INSERT INTO entries VALUES (?, ? , ?, ?)', params)
    cur.execute('SELECT * FROM entries')
    print(cur.fetchall())
    conn.commit()
    conn.close()



if __name__ == '__main__':
    init_db()
