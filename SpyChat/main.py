from globals import spy
from start_chat import start_chat
import re

# Continue as a existing user
print "Let's get Started"
question = "Continue as %s %s (Y/N)" % (spy.salutation, spy.name)
existinginput = raw_input(question)

# validating new user's input
if existinginput == "Y" or existinginput == "y":
    start_chat(spy.name, spy.age, spy.rating)

elif existinginput == "N" or existinginput == "n":
    spy.name = raw_input("Enter your name here :")
    pattern = '^[a-zA-Z\s]+$'
    if (re.match(pattern, spy.name) != None):
        if len(spy.name) > 0:
            spy.salutation = raw_input("What should we call you? : ")
            spy.name = spy.salutation + " " + spy.name
            spy.age = 0
            spy.rating = 0.0
            spy.is_online = False
            while True:
                try:
                    spy.age = int(raw_input("What is your age? "))
                    break
                except ValueError:
                    print "Invalid age. Try again"
            # Checking the required age of user
            if type(spy.age) is int:
                if 12 < spy.age < 50:
                    spy.rating = float(raw_input(" What is your spy rating: "))
                    if spy.rating > 4.5:
                        print " Awesome!!"
                    elif 3.5 < spy.rating < 4.5:
                        print " You are Good one "
                    elif 2.5 < spy.rating < 3.5:
                        print " try harder"
                    else:
                        print " u will be beter tommorow"
                    print " Welcome " + spy.name + " Good to have u back"
                    print "Let's get Started!"
                    start_chat(spy.name, spy.age, spy.rating)
                else:
                    print " You are not eligible to be a spy"
            else:
                print " Please type a valid number!!! "

        else:
            print "Invalid Name Please Try again"
    else:
        print "Invalid name.Please Try alphabets only"
else:
    print " Wrong choice.Please Try again"


