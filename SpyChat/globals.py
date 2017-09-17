from spy_details import Spy
from datetime import datetime


status = ['My name is Pallavi, Ms. Pallavi', ' I C Python', 'Its gonna high']

# Spy object
spy = Spy("Dubey", "Mr. ", 31, 2.1)

# Friends
friend_one = Spy('Rohan', 'Mr.', 21, 4)
friend_two = Spy('rashmi', 'Ms.', 21, 5)
friend_three = Spy('anand bhagat', 'Dr.', 50, 4.5)

friends = [friend_one, friend_two, friend_three]

# Class to store Chat messages


class ChatMessage:

  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me

