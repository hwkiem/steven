import sqlite3


def init_db():  # make the database for the first time
    conn = sqlite3.connect('steven.sqlite3')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE entries (inbound TEXT, command TEXT, item TEXT, price INTEGER)''')  # make entries table
    conn.commit()
    conn.close()


def add_entry(params):  # sender, command, item, quantity
    conn = sqlite3.connect('steven.sqlite3')  # connect to steven database
    cur = conn.cursor() # cursor object to maneuver/manipulate database
    cur.execute('INSERT INTO entries VALUES (?, ? , ?, ?)', params) 
    cur.execute('SELECT * FROM entries')  # in order to print/fetchall()
    conn.commit()
    conn.close()
    return params[2] + " added successfully"


def get_all_entries():
    conn = sqlite3.connect('steven.sqlite3')  # connect to steven database
    cur = conn.cursor() # cursor object to maneuver/manipulate database
    cur.execute('SELECT * FROM entries')  # in order to print/fetchall()
    resp = str(cur.fetchall())
    conn.close()
    return resp


if __name__ == '__main__':
    init_db()
