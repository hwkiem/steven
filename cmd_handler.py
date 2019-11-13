from Command import Cmd
import db_handler

db = 'steven.sqlite3'


def handle(c: Cmd):
    if c.cmd == 'Group':
        group(c)
    elif c.cmd == 'Item':
        return item(c.flags, c.params, c.origin)
    else:
        return "invalid command. Type \'help\' for a list of valid commands."


def group(c: Cmd):
    print(c.to_string())

    if '-c' in c.flags and len(c.params) == 1:
        db_handler.create_group(c.params[0])

    """
    if '-l' in f and len(p) == 0:
        return str(db_handler.retrieve_groups(o))
    elif '-s' in p and len(p) == 1:
        res = db_handler.update_user(p[0], o)
        if res:
            return res
        else:
            return "Usage: Group -s <name> where name is a group you are a member of"
    elif '-i' in f and len(p) == 2:
        db_handler.invite_user(p[0], p[1])
    elif '-m' in f and len(p) == 1:
        return db_handler.retrieve_group_members(p[0])
    elif '-x' in f and len(p) == 1:
        db_handler.leave_group(p[0])
    """


def item(f, t, o):
    return None