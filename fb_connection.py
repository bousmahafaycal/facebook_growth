# 3d
from fbchat import Client


class FbConnection:
    def __init__(self, email, password):
        self.client = Client(email, password)
