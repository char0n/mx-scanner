import os


class Output(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_object = open(self.file_name, 'ar+')

    def write(self, hostname, status):
        self.file_object.write('{0};{1}\n'.format(hostname, status))

    def get_last(self):
        return os.popen('tail -n1 {0}'.format(self.file_name)).readline().strip()

    def __del__(self):
        self.file_object.close()