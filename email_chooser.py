import random
import re
import requests
from twitter_scraper import get_tweets
#-----------------------------------------------------------------------------------------------------------------------------
# TODO: will make this more interactive, may use a class here.
# TODO: May use generator here...
domains_list = [domain.rstrip('\n') for domain in open('data/domains.txt')]
# set up this word list from my phone in a bar, so pardon the liquor names in there.

#---------------------------------------------------------

def genEmail(length=1,pages=1):
    userlist = getUsers(pages)
    if len(userlist) < length:
        return "Sorry we were only able to gather {} of the requested {} users try increasing pages".format(len(userlist),length)
    return [random.choice(userlist) + random.choice(domains_list) for _ in range(length)]


def getDumpUrl(pages):
    print("Gathering Links")
    urls = []
    for tweet in get_tweets('dumpmon', pages=pages):
        urls.append(re.findall(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})", tweet['text']))
    return urls

def getUsers(pages):
    urls = getDumpUrl(pages)
    e = []
    users = []
    print('Extracting Emails')
    for url in urls:
        s = str(url)[2:-2]
        r = requests.get(s)
        content = str(r.content)
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@", content)
        for email in emails:
            if email.find('-')==-1:
                e.append(email)
                #print(email)
    print('Building user list')
    for email in e:
        if len(email)>5 and len(email)<24:
            #print(email, len(email))
            ind = len(email)-2
            user = email[0:ind]
            if re.match('^(?=.*[a-zA-Z])', user):
                users.append(user)
    users = list(set(users)) #Remove duplicates
    for u in users:
        for c in u:
            if c.isdigit():
                c = replaceDigit(c)

    print("Collected {} users".format(len(users)))
    return users


def replaceDigit(digit):
    d = random.randrange(0,9)
    if d != digit:
        return d
    else:
        replaceDigit(d)








