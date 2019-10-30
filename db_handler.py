import sqlite3


def init_db(): # make the database for the first time
    conn = sqlite3.connect('steven.sqlite3')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE entries (inbound TEXT, command TEXT, item TEXT, price INTEGER)''') # make entries table
    conn.commit()
    conn.close()


def add_entry(params):
    conn = sqlite3.connect('steven.sqlite3') # connect to steven database
    cur = conn.cursor() # cursor object to maneuver/manipulate database
    cur.execute('INSERT INTO entries VALUES (?, ? , ?, ?)', params) 
    cur.execute('SELECT * FROM entries') # in order to print/fetchall()
    print(cur.fetchall())
    conn.commit()
    conn.close()

def get_all_entries():
    conn = sqlite3.connect('steven.sqlite3') # connect to steven database
    cur = conn.cursor() # cursor object to maneuver/manipulate database
    cur.execute('SELECT * FROM entries') # in order to print/fetchall()
    print(type(cur.fetchall()))
    conn.close()



if __name__ == '__main__':
    init_db()
