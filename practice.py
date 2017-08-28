# import statments
from spy_details import spy
from spy_chat import start_chat

print "let's get started!"
question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N): "
existing = raw_input(question)

# validating user input
if existing == 'Y' or existing == 'y' :
    # user wants to continue as a default users.

    # concatination of salutation and name of spy.
    spy_name = spy['salutation'] + " " + spy['name']

    # starting chat application.
    start_chat(spy['name'], spy['age'], spy['rating'])

elif existing == 'N' or existing == 'n' :

    pass
else:
    print " Invalid output. Try Again. "

# user wants to continue as a new user
spy['name'] = raw_input("provide your name here : ")

# Check whether spy has input something or not
if len(spy['name']) > 0:
    # code block if the condition is true.

    spy_salutation = raw_input('what should we call you ?: ')
    spy_age = int(raw_input("Enter your age "))

    # concatination of salutation and name.
    if spy['age'] > 12 and spy['age'] <= 50:
      spy_rating = float(raw_input(" What is your spy rating:"))
      if spy_rating > 4.5:
        print ("excellent")
      elif spy_rating > 3.5 and spy_rating <= 4.5:
        print ("great")
      elif spy_rating > 2.5 and spy_rating <= 3.5:
        print ("good")
      elif spy_rating > 1.5 and spy_rating <= 2.5:
        print ("satisfactory")
      else:
          print (" work hard and do better")
    else:
      print (" Sorry.. You are not eligible for spy. ")
    spy['name'] = spy['salutation'] + " " + spy['name']
    spy['is_online'] = True
    print 'welcome ' + spy['name'] + ' happy to see you '
    print "Alright " + spy['name'] + " I'd like to know more about you before we proceed further"
else:
    print "Invalid Name. Try Again."
print "Authentication complete. welcome " + spy['name'] + " age: " +  str(spy['age']) + " spy rating: " + str(spy['rating']) + " happy to see you"








