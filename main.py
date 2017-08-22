# import statments
from spy_details import spy_name, spy_salutation, spy_age, spy_rating
from spy_chat import start_chat

print "let's get started!"
question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N): "
existing = raw_input(question)

# validating user input
if existing == 'Y' or existing == 'y' :
    # logic here
    start_chat (spy_name, spy_age, spy_rating)
    pass
elif existing == 'N' or existing == 'n' :
    # new code here
   pass
else:
    print " Invalid output. Try Again. "

spy_name = raw_input("enter your name here : ")
spy_age = 0
spy_rating = 0.0
spy_is_online = False

# Check whether spy has input something or not
if len(spy_name) > 0:
    # code block if the condition is true.
    # concatination of saluttion and name.
    spy_salutation = raw_input('what should we call you ?: ')
    spy_age = int(raw_input("Enter your age "))
    if spy_age > 12 or spy_age <= 50:
        spy_rating =float(raw_input(" What is your spy rating:"))
        if spy_rating > 4.5:
            print ("exellent")
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print ("great")
        elif spy_rating > 2.5 and spy_rating <= 3.5:
            print ('good')
        elif spy_rating > 1.5 and spy_rating <= 2.5:
            print ("satisfactory")
        else:
            print (" work hard and do better")
        spy_name = spy_salutation + " " + spy_name
        print 'welcome ' + spy_name + ' happy to see you '
        print "Alright " + spy_name + " I'd like to know more about you before we proceed further"
    else:
        print  "Sorry.. You are not eligible for spy."
else:
    print "Invalid Name. Try Again."
print "Authentication complete. welcome " + spy_name + " age: " +  str(spy_age) + " spy rating: " + str(spy_rating) + " happy to see you"



