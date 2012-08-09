
class MXParser(object):

    def __init__(self, regex):
        self.regex = regex

    def is_valid(self, mx_hosts):
        if not mx_hosts:
            return False
        for mx_host in mx_hosts:
            if self.regex.search(mx_host[1]):
                return True
        return False
