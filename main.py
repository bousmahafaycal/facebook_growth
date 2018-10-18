# -*- coding: utf-8 -*

# std
import os
import sys

# 3d
from getpass import getpass


# project
from fb_friends import FbFriends
from fb_messenger import FbMessenger
from fb_connection import FbConnection
from fb_group import FbGroup


EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
CSV_FILE = os.environ.get('CSV_FILE')


def send_group(client, message):
    csv = CSV_FILE
    fbg = FbGroup(client)
    if csv is None:
        csv = input("Entrez le nom du fichier : ")
    friends = fbg.get_ids__list(csv)
    fbm = FbMessenger(fbc.client, friends)
    print("Les messages vont être envoyés à votre liste d'amis")
    fbm.send_messages(message)


def send_friends(client, message):
    fbf = FbFriends(client)
    friends = fbf.get_friends_ids__list()
    fbm = FbMessenger(fbc.client, friends)
    print("Les messages vont être envoyés à votre liste d'amis")
    fbm.send_messages(message)


if __name__ == '__main__':
    if EMAIL is None:
        EMAIL = input("Entrez votre adresse email : ")
    if PASSWORD is None:
        PASSWORD = getpass()
    fbc = FbConnection(EMAIL, PASSWORD)

    message = input("Quel message souhaitez-vous envoyé : ")

    if sys.argv[1] == "send_group":
        send_group(fbc.client, message)
    elif sys.argv[1] == "send_friends":
        send_friends(fbc.client, message)
    else:
        print("Erreur, la commande entrée doit etre choisie entre send_group et send_friends")

