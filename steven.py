import pickle

shopping = {}


def handle(params):
    global shopping
    pickle_in = open("shopping.p", "rb")
    shopping = pickle.load(pickle_in)
    res = 'Error: invalid command'
    cmd = params[1].lower()
    if cmd == 'add':
        res = add_item(params[2], params[3])
    elif cmd == 'list':
        res = gen_list_response()
    elif cmd == 'bought':
        res = remove_item(params[1], int(params[2]))
    pickle_out = open("shopping.p", "wb")
    pickle.dump(shopping, pickle_out)
    pickle_out.close()
    return res


def add_item(item, cnt):
    if item in shopping.keys():
        shopping[item] += int(cnt)
    else:
        shopping[item] = int(cnt)
    return gen_list_response()


def gen_list_response():
    return str(shopping)


def remove_item(item, cnt):
    if item in shopping:
        if cnt >= shopping[item]:
            del shopping[item]
        else:
            shopping[item] -= cnt
        return gen_list_response()
    else:
        return "No such item in list"

