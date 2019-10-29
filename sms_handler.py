from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Body, Message
from twilio.rest import Client
import steven
import db_handler as db

app = Flask(__name__)
@app.route("/sms", methods=['POST', 'GET'])
def sms_handler():
    try:

        sms_body = request.values.get('Body', None).split(' ')
        sms_from = request.values.get('From', None)
        params = [sms_from, sms_body[0], sms_body[1], sms_body[2]]
        s = steven.handle(params)
        db.add_entry(params)
        resp = MessagingResponse()
        resp.message(s)
        return str(resp)
    except AttributeError:
        return "waiting"


if __name__ == "__main__":
    app.run(debug=True)
