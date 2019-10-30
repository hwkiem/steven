import db_handler as db # making calls to db based on commans


def handle(params):
    res = 'Error: invalid command or formatting'
    cmd = params[1].lower()
    if cmd == 'add':
        #res = add_item(params[2], params[3])
        res = db.add_item(params)
    elif cmd == 'list':
        res = db.get_all_entries()
    elif cmd == 'bought': # not yet converted to DB call
        res = remove_item(params[1], int(params[2]))
    return res


# def add_item(item, cnt):
#     if item in shopping.keys():
#         shopping[item] += int(cnt)
#     else:
#         shopping[item] = int(cnt)
#     return gen_list_response()


# def gen_list_response():
#     return str(shopping)


# def remove_item(item, cnt):
#     if item in shopping:
#         if cnt >= shopping[item]:
#             del shopping[item]
#         else:
#             shopping[item] -= cnt
#         return gen_list_response()
#     else:
#         return "No such item in list"

