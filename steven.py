from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Body, Message
from twilio.rest import Client

app = Flask(__name__)
shopping = ["cheese", "bread", "coffee"]


def add_item(item):
    if item in shopping:
        return "item already added"
    else:
        shopping.append(item.lower())
        return "added " + item


def gen_list_response():
    return str(shopping)


def remove_item(item):
    if item in shopping:
        shopping.remove(item)
        return gen_list_response()
    else:
        return "item not in shopping list"


@app.route("/sms", methods=['POST', 'GET'])
def sms_handler():
    sms = request.values.get('Body', None)
    resp = MessagingResponse()

    params = sms.split(" ")
    print(params)
    if params[0].lower() == 'add':
        resp.message(add_item(params[1]))
    elif params[0].lower() == 'list':
        resp.message(gen_list_response())
    elif params[0].lower() == 'bought':
        resp.message(remove_item(params[1]))
    else:
        resp.message("invalid command")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
