# TODO: May use generator here...
users = [user.rstrip('\n') for user in open('data/usernames.txt')]

print(len(users))
