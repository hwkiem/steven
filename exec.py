from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import Command
import cmd_handler

app = Flask(__name__)
@app.route("/steven", methods=['GET'])
def steven():
    try:
        #  Getting HTTP request
        sms_body = request.values.get('Body', None).split(' ')
        sms_from = request.values.get('From', None)
        sms_timestamp = request.vales.get('date_sent', None)

        #  Creating a response object
        resp = MessagingResponse()

        #  Creating command object
        cmd = Command(sms_body, sms_from, sms_timestamp)

        #  Checking if cmd is valid
        if cmd is None:
            resp.message('Invalid command. Type \'help\' for a list of commands.')
        else:
            resp.message(cmd_handler(cmd))

        return str(resp)
    except AttributeError:
        return "waiting..."


if __name__ == '__main__':
    app.run(debug=True)