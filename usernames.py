# TODO: May use generator here...
users = [user.rstrip('\n') for user in open('users.txt')]

print(len(users))
