from select_friend import select_friend
from steganography.steganography import steganography
from datetime import datetime
from globals import friends

def read_message():
    # choose friend from the list
    sender = select_friend()

    encrypted_image = raw_input("Provide encrypted image : ")
    secret_message = steganography.decode(encrypted_image)

    # save the messages
    new_chats = {
        'message': secret_message,
        'time': datetime.now(),
        'sent_by_me': False
    }

    friends[sender]['chats'].append(new_chat)
    print "Your srcret message hs been saved. "
