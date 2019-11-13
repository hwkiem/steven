from Command import Cmd
import sqlite3

db = 'steven.sqlite3'


def handle(c: Cmd):
    if c.cmd == 'Group':
        return group(c.flags, c.timestamp, c.origin)
    elif c.cmd == 'Item':
        return item(c.flags, c.timestamp, c.origin)
    else:
        return "invalid command. Type \'help\' for a list of valid commands."


def group(f, t, o):
    conn = sqlite3.connect(db)
    cur = conn.cursor()


def item(f, t, o):
    return None