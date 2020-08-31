# -*- coding: utf-8 -*

# std
import sys

# 3d
from getpass import getpass


# project
from fb_friends import FbFriends
from fb_messenger import FbMessenger
from fb_connection import FbConnection
from fb_group import FbGroup


EMAIL = None
PASSWORD = None  # put your password here if you doesn't want to enter your password at each time.
CSV_FILE = None


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
    print("Quel message souhaitez-vous envoyé (Entrez / collez votre message. Entrez #fin sur la dernière ligne pour terminer):")
    messages = []
    while True:
        line = input()
        if line == '#end':
            break
        messages.append(line)
    message = '\n'.join(messages)
    if sys.argv[1] == "send_group":
        send_group(fbc.client, message)
    elif sys.argv[1] == "send_friends":
        send_friends(fbc.client, message)
    else:
        print("Erreur, la commande entrée doit etre choisie entre send_group et send_friends")

