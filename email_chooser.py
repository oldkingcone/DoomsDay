import random

#-----------------------------------------------------------------------------------------------------------------------------
# will make this more interactive, may use a class here.    
domains_list = ["@gmail.com",
                "@yahoo.com",
                "@yandex.com",
                "@protonmail.com",
                "@hotmail.com",
                "@1and1.com",
                "@mail.com",
                "@inbox.com",
                "@aol.com",
                "@outlook.com",
                "@icloud.com",
                "@office365.com",
                "@zoho.mail",
                "@hushmail.com",
                "@fastmail.com",
                "@gmxmail.com"]
# set up this word list from my phone in a bar, so pardon the liquor names in there.
words = ["barbie",
         "rocker",
         "diamond",
         "leet",
         "beer",
         "rockstar",
         "bulleit",
         "moon",
         "draught",
         "tanaka",
         "yankee",
         "aviator",
         "queen",
         "cocktail",
         "absolute",
         "mountain",
         "light",
         "yankee",
         "beef"
         ]
#---------------------------------------------------------
# need to expand the list. big time.lots of repeats for words in the emails.
def genEmail(iteration):
    email_list = list()
    while iteration != 0:
        email = random.choice(words) + random.choice(words) + random.choice(domains_list)
        email_list.append(email)
        iteration -= 1
    return email_list
