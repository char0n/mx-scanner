import csv


class DomainSource(object):

    def __init__(self, source_file):
        self.source_file = source_file
        self.file_object = open(self.source_file, 'rb')
        for r in range(10):
            self.file_object.readline()
        csv_start = self.file_object.tell()
        dialect = csv.Sniffer().sniff(self.file_object.read(4096))
        self.file_object.seek(csv_start)
        self.reader = csv.DictReader(self.file_object, dialect=dialect)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next()['domena']

    def __del__(self):
        self.reader = None
        self.file_object.close()