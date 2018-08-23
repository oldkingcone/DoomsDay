import random
from usernames import users
#-----------------------------------------------------------------------------------------------------------------------------
# TODO: will make this more interactive, may use a class here.
# TODO: May use generator here...
domains_list = [domain.rstrip('\n') for domain in open('data/domains.txt')]
# set up this word list from my phone in a bar, so pardon the liquor names in there.

#---------------------------------------------------------
# Current list of fake users is about 5000.

def genEmail(length):
    return [random.choice(users) + random.choice(domains_list) for _ in range(length)]
