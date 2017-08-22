# import statements.
from globals import STATUS_MESSAGES

def add_status(current_status_message):
    # update status message.
    if current_status_message != None:
        print 'Your current status messsge is ' + current_status_message + "\n"
    else:
        print " you don't have status message currently \n "
        default = raw_input(" do you want to select from the older message (y/n)? ")

        if default.upper() == 'N':
            new_status_message = raw_input(" what status message do you want to set?")

            if len(new_status_message) > 0:
                update_status_message = new_status_message
                STATUS_MESSAGES.append(update_status_message)
            elif default.upper() == 'Y':
                item_position = 1
                for message in STATUS_MESSAGES:
                    print item_position + ". " + message
                    item_position = item_position + 1
                    message_selection = int(raw_input("\n choose from the above messages "))
                    if len(STATUS_MESSAGES) >= message_selection:
                        updated_status_message = STATUS_MESSAGES[message_selection - 1]
                        return updated_status_message
                    current_status_message = add_status(current_status_message)


