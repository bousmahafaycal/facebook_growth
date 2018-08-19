
from fbchat import Client
from fbchat.models import *
from ffile import FFile
from random import randint
from time import sleep


class FbMessenger:
    def __init__(self, client, ids=None, threshold=100, wait_after_threshold=1200, min_wait_beetween_message=45, max_wait_beetween_message=75):
        self.client = client
        self.ids = ids
        self.threshold = threshold
        self.wait_after_threshold = wait_after_threshold
        self.min_wait_beetween_message = min_wait_beetween_message
        self.max_wait_beetween_message =  max_wait_beetween_message

    def import_ids(self, location):
        """
        Import ids separated by ,
        :param location:
        :return:
        """
        f = FFile(location)
        string = f.read_file()
        self.ids = string.split(",")

    def send_messages(self, message):
        """
        Send messages to all people in self.ids list
        :return:
        """
        if self.ids is None:
            raise ValueError("ids cannot be None when you want to send messages in the FbMessenger class")

        i = 0
        for friend_id in self.ids:
            print("Send message to {}".format(friend_id))
            self.client.send(Message(text=message), thread_id=friend_id,  thread_type=ThreadType.USER)
            i += 1
            if i%self.threshold == 0:
                sleep(self.wait_after_threshold)
            else:
                sleep(randint(self.min_wait_beetween_message, self.max_wait_beetween_message))


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
