import sqlite3
from sqlite3 import Error
from datetime import datetime, date


def init_db():  # make the database for the first time
    conn = create_connection()
    if conn is None:
        print("unable to connect to db.")
    else:
        conn.close();
        # Groups Table
        sql = (
            '''
            CREATE TABLE IF NOT EXISTS Groups (
            GroupID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL
            )
            '''
        )
        create_table(sql)
        # Users Table
        sql = (
            '''
            CREATE TABLE IF NOT EXISTS Users (
            UserID INTEGER PRIMARY KEY,
            Username TEXT NOT NULL,
            AllGroups TEXT NOT NULL,
            CurGroup INTEGER NOT NULL,
            FOREIGN KEY (CurGroup) REFERENCES Groups (GroupID)
            )
            '''
        )
        create_table(sql)

        # Items Table
        sql = (
            '''
            CREATE TABLE IF NOT EXISTS Items (
            GroupID integer NOT NULL,
            UserID integer NOT NULL,
            Name varchar(255) NOT NULL,
            StatusID integer NOT NULL,
            Price integer,
            Quantity int,
            UnitCode int,
            ts TIMESTAMP,
            FOREIGN KEY (GroupID) REFERENCES Groups (GroupID)
            FOREIGN KEY (UserID) REFERENCES Users (UserID)
            )
            '''
        )
        create_table(sql)


def create_connection(db='steven.sqlite3'):
    conn = None
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
        return None


def create_table(sql):
    conn = create_connection()
    if conn is None:
        print("failed to make connection")
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)


def create_group(name):
    conn = create_connection()
    if conn is None:
        print("failed to make connection")
    try:
        c = conn.cursor()
        sql = (
            '''
            INSERT INTO Groups(Name)
            VALUES(?)
            '''
        )
        c.execute(sql, (name,))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)


def retrieve_groups(user):
    conn = create_connection()
    if conn is None:
        print("failed to make connection")
    try:
        c = conn.cursor()
        sql = (
            '''
            SELECT AllGroups FROM Users WHERE UserID=?
            '''
        )
        c.execute(sql, user)
        r = c.fetchall()
        return r
    except Error as e:
        print(e)


def see_db_groups():
    conn = create_connection()
    try:
        c = conn.cursor()
        sql = (
            '''
            SELECT * FROM Groups
            '''
        )
        c.execute(sql)
        rows = c.fetchall()
        for r in rows:
            print(r)
    except Error as e:
        print(e)


def see_db_items():
    conn = create_connection()
    try:
        c = conn.cursor()
        sql = (
            '''
            SELECT * FROM Items
            '''
        )
        c.execute(sql)
        rows = c.fetchall()
        for r in rows:
            print(r)
    except Error as e:
        print(e)


def see_db_users():
    conn = create_connection()
    try:
        c = conn.cursor()
        sql = (
            '''
            SELECT * FROM Users
            '''
        )
        c.execute(sql)
        rows = c.fetchall()
        for r in rows:
            print(r)
    except Error as e:
        print(e)


def invite_user(conn, group, newuser):
    return None


if __name__ == '__main__':
    print(
        "Select an option:\n1) initialize\n2)see_databases"
    )
    choice = input()
    if choice == '1':
        init_db()
    elif choice == '2':
        see_db_groups()
        print("--------------")
        see_db_items()
        print("--------------")
        see_db_users()
        print("--------------")
    else:
        print("invalid command")
