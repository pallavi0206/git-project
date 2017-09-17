from select_friend import select_a_friend
from steganography.steganography import Steganography
from globals import ChatMessage, friends
from termcolor import colored


def read_message():
    sender = select_a_friend()
    # Selecting Friend to read message
    while True:
        try:
            output_path = raw_input("What is the name of the file? : ")
            secret_text = Steganography.decode(output_path)
            print secret_text
            break
        except TypeError:
            print(colored("image as no such thing to decode", 'red'))
        # Number of words spoken by spy
        words = secret_text.split()
        friends[sender].words += len(words)
        # Deleting friend who talk too much
        if len(words) > 100 :
            friends.remove(friends[sender])
            print "You are blocked due to abusive speaking"


    new_chat = ChatMessage(secret_text, False)

    friends[sender].chats.append(new_chat)
