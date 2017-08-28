# import statments.
from globals import friends

# add new friends.
def add_friend():
    new_friend = {
    'name': '',
    'salutation': '.',
    'age': 0,
        'rating': 0.0,
        'is_online': False
    }
    new_friend['name'] = raw_input(" Please add your friend's name: ")
    new_friend['salutation'] = raw_input(" Are they Mr. , Miss or Mrs.?: ")

    # concatination.
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = int(raw_input(" age? "))

    new_friend['rating'] = float(raw_input(" spy rating? "))

    if len(new_friend['name']) > 0 and new_friend['age'] >15 and new_friend['age'] < 50:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print ' Sorry..! Invalid entry. Spy can\'t be added with invalid details'

        return  len(friends)



