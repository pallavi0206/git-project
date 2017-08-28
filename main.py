# import statements
from spy_details import spy
from spy_chat import start_chat

print "let's get started!"
question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N): "
existing = raw_input(question)

# validating user input
if existing == 'Y' or existing == 'y':
    # user wants to continue as a default users.

    # concatination of salutation and name of spy.
    spy_name = spy['salutation'] + " " + spy['name']

    # starting chat application.
    start_chat(spy['name'], spy['age'], spy['rating'])
    pass
elif existing == 'N' or existing == 'n':
    # new code here.
   pass
else:
    print " Invalid output. Try Again. "

spy['name'] = raw_input("enter your name here : ")
spy_age = 0
spy_rating = 0.0
spy_is_online = False

# Check whether spy has input something or not
if len(spy['name']) > 0:
    # code block if the condition is true.
    # concatination of salutation and name.
    spy_salutation = raw_input('what should we call you ?: ')
    spy_age = int(raw_input("Enter your age "))
    if spy_age > 15 or spy_age <= 50:
        spy_rating = float(raw_input(" What is your spy rating:"))
        if spy_rating > 4.5:
            print ("excellent")
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print ("great")
        elif spy_rating > 2.5 and spy_rating <= 3.5:
            print ('good')
        elif spy_rating > 1.5 and spy_rating <= 2.5:
            print ("satisfactory")
        else:
            print (" work hard and do better")
        spy_name = spy_salutation + " " + spy['name']
        print 'welcome ' + spy_name + ' happy to see you '
        print "Alright " + spy_name + " I'd like to know more about you before we proceed further"
    else:
        print "Sorry.. You are not eligible for spy."
else:
    print "Invalid Name. Try Again."
print "Authentication complete. welcome " + spy['name'] + " age: " + str(spy_age) + " spy rating: " + str(spy_rating) + "happy to see you"



