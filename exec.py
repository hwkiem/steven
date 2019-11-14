from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Command import Cmd
import cmd_handler
import db_handler

app = Flask(__name__)
@app.route("/steven", methods=['GET'])
def steven():
    try:
        #  Getting HTTP request
        sms_body = request.values.get('Body', None).split(' ')
        sms_from = request.values.get('From', None)

        # Check user
        db_handler.create_user(sms_from)

        #  Creating a response object
        resp = MessagingResponse()

        #  Creating command object
        cmd = Cmd(sms_body, sms_from)

        #  Checking if cmd is valid
        if cmd is None:
            resp.message('Invalid command. Type \'help\' for a list of commands.')
        else:
            resp.message(cmd_handler.handle(cmd))

        return str(resp)
    except AttributeError:
        return "waiting..."


if __name__ == '__main__':
    app.run(debug=True)