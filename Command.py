class Cmd:
    cmd = None
    flags = list()
    params = list()
    timestamp = None
    origin = None

    def __init__(self, sms_body, sms_from):
        if len(sms_body) < 2:
            return None
        else:
            # Filling command fields
            self.cmd = sms_body[0]
            self.origin = sms_from

            for i in range(1, len(sms_body)):
                elem = sms_body[i]
                if elem.startswith('-'):
                    self.flags.append(elem)
                else:
                    self.params.append(elem)

    def to_string(self):
        cmd = str(self.cmd)
        flags = str(self.flags)
        params = str(self.params)
        timestamp = str(self.timestamp)
        origin = str(self.origin)
        res = "cmd: " + cmd, "flags: " + flags, "params: " + params, "origin: " + origin
        return res
