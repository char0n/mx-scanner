
class Output(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def write(self, hostname, status):
        if status == 'OK':
            print '{0}: {1}{2}{3}'.format(hostname, self.OKGREEN, status, self.ENDC)
        else:
            print '{0}: {1}{2}{3}'.format(hostname, self.FAIL, status, self.ENDC)