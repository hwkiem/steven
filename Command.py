class Cmd:
    cmd = None
    flags = list()
    timestamp = None
    origin = None

    def __init__(self, sms_body, sms_from, sms_timestamp):
        if len(sms_body) < 2:
            return None
        else:
            # Filling command fields
            cmd_entry = True
            for elem in sms_body:
                if cmd_entry is True:
                    self.cmd = elem
                    cmd_entry = False
                else:
                    self.flags.append(elem)

            self.timestamp = sms_timestamp
            self.origin = sms_from
