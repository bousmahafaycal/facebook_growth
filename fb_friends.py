# 3d
from fbchat import Client

# project
from ffile import FFile


class FbFriends:
    def __init__(self, client):
        self.client = client
        self.friends = None
        self.friends_ids = []
        self.get_all_friends()
        self.get_friends_ids__list()

    def get_all_friends(self):
        """
        Get all friends
        :param email:
        :param password:
        :return: array: user ids
        """
        self.friends = self.client.fetchAllUsers()

    def get_friends_ids__list(self):
        """
        Return friends ids separated by a ,
        :return: str
        """
        self.friends_ids = []
        for friend in self.friends:
            self.friends_ids.append(friend.uid)

        return self.friends_ids

    def get_friends_ids__string(self):
        string = ""
        for fid in self.friends_ids:
            string += "{},".format(fid)
        string = string[:-1]
        return string

    def export(self, location):
        """
        Export ids separated by ,
        :return:
        """
        f = FFile(location)
        f.write_file(self.get_friends_ids__string())
