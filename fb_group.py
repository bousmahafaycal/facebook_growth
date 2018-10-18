# 3d
import codecs
import re
import csv
from fbchat import Client

# project
from ffile import FFile


class FbGroup:
    def __init__(self, client):
        self.client = client
        self.ids = []

    def get_ids__list(self, location):
        self.ids = []
        with codecs.open(location, "r", encoding='utf-8', errors='ignore') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0 and row:
                    user_id = row[1]
                    r = re.match(r'/ajax/hovercard/user.php\?id=(?P<user_id>\d+).*', user_id)
                    if r:
                        f_user_id = int(r.group('user_id'))
                        if f_user_id not in self.ids:
                            self.ids.append(f_user_id)
                line_count += 1
        return self.ids

    def get_ids__string(self):
        string = ""
        for fid in self.ids:
            string += "{},".format(fid)
        string = string[:-1]
        return string

    def export(self, location):
        """
        Export ids separated by ,
        :return:
        """
        f = FFile(location)
        f.write_file(self.get_ids__string())