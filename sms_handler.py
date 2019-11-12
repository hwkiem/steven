from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Body, Message
import steven


app = Flask(__name__)
@app.route("/sms", methods=['POST', 'GET']) # everything seems to be GET requests; should we be using others or just looking at Body
def sms_handler():
    try: # for errors when there isnt a text

        sms_body = request.values.get('Body', None).split(',') # tentative splitting on commas 
        sms_from = request.values.get('From', None)
        params = [sms_from, sms_body[0], sms_body[1], sms_body[2]] # sender, command, item, quantity
        s = steven.handle(params) # response returned by handle
        resp = MessagingResponse() # create MessageResponse object
        resp.message(s) # set message
        return str(resp)
    except AttributeError:
        return "waiting"


if __name__ == "__main__":
    app.run(debug=True)
