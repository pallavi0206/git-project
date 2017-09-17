from globals import status


def add_status(status_message, status1):
    if status_message is None:
        print " You do not have any status \n"
    else:
        print " Your current status %s \n " % status_message
    default = raw_input(" would you want to select from older status(Y/N) :")

    if default == "n" or default == "N":
        new_status_message = raw_input(" Which status message do you want to select?: ")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            status.append(updated_status_message)

    elif default == "y" or default == "Y":
        item_position = 1
        for message in status1:
            print " %d. %s " % (item_position, message)
            item_position += 1
        message_selection = int(raw_input(" \nChoose from the above message : "))
        if len(status) >= message_selection:
            updated_status_message = status1[message_selection - 1]

    return updated_status_message






