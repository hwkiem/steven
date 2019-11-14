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
            UserID INTEGER NOT NULL,
            CurGroup INTEGER NOT NULL,
            AllGroups TEXT NOT NULL,
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
        print("create_connection error")
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
        print("create table error")


def user_create_item(name, origin):
    conn = create_connection()
    if conn is None:
        print("failed to make connection")
    try:
        c = conn.cursor()
        sql = (
            '''
            INSERT INTO Items (
            GroupID,
            UserID,
            Name,
            StatusID
            ) VALUES(?, ?, ?, 0)
            '''
        )
        curgroup = user_retrieve_cur_group(origin)
        c.execute(sql, (curgroup, origin, name))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
        print("user create item error")



def user_retrieve_cur_group(phone):
    conn = create_connection()
    if conn is None:
        print("failed to make connection")
    try:
        c = conn.cursor()
        sql = (
            '''
            SELECT CurGroup FROM Users WHERE UserID=?
            '''
        )
        c.execute(sql, phone)
        r = c.fetchall()
        return int(r)
    except Error as e:
        print(e)
        print("user retrieve cur group error")


def user_create_group(name, usernum):
    conn = create_connection()
    if conn is None:
        print("failed to make connection")

    groups = user_retrieve_groups(usernum)
    if name not in groups:
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
            user_update_groups(usernum, name)
        except Error as e:
            print(e)
            print("user create group error")


def user_update_groups(usernum, groupname):
    conn = create_connection()
    if conn is None:
        print("failed to make connection")

    groups = user_retrieve_groups(usernum)
    for g in groups:
        print(g)
    if groupname not in groups:
        try:
            c = conn.cursor()
            sql = (
                '''
                UPDATE Users SET AllGroups = ?
                WHERE UserID = ?
                '''
            )
            groups = groups + (groupname,)
            c.execute(sql, (groups + (usernum, )))
            conn.commit()
            conn.close()
        except Error as e:
            print(e)
            print("user update groups error")


def user_retrieve_groups(user):
    conn = create_connection()
    if conn is None:
        print("failed to make connection")
    try:
        c = conn.cursor()
        sql = (
            '''
            SELECT AllGroups from USERS WHERE UserID=?
            '''
        )
        c.execute(sql, (user,))
        r = c.fetchall()[0]
        return r
    except Error as e:
        print(e)
        print("user retrieve groups error")


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


def create_user(usernum):
    conn = create_connection()
    if not retrieve_user(usernum):
        try:
            c = conn.cursor()
            sql = (
                '''
                INSERT INTO Users (UserID, CurGroup, AllGroups)
                VALUES(?, ?, ?)
                '''
            )
            allgroups = 'general'
            c.execute(sql, (usernum, 1, allgroups))
            conn.commit()
            conn.close()
        except Error as e:
            print(e)
            print("create_user error")


def retrieve_user(usernum):
    conn = create_connection()
    try:
        c = conn.cursor()
        sql = (
            '''
            SELECT * FROM Users WHERE UserID=?
            '''
        )
        c.execute(sql, (usernum,))
        res = c.fetchall()
        return res
    except Error as e:
        print(e)
        print("retrieve create group error")


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


