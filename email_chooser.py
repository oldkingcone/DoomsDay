import random

#-----------------------------------------------------------------------------------------------------------------------------
# will make this more interactive, may use a class here.    
domains_list = ["gmail.com",
                "yahoo.com",
                "yandex.com",
                "protonmail.com",
                "hotmail.com",
                "1and1.com",
                "mail.com",
                "inbox.com",
                "aol.com",
                "outlook.com",
                "icloud.com",
                "office365.com",
                "zoho.mail",
                "hushmail.com",
                "fastmail.com",
                "gmxmail.com"]
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

def genEmail(iteration):
    email_list = set()
    for i in range(iteration):
        email = random.choice(words) + random.choice(words) + '@' + random.choice(domains_list)
        email_list.add(email)
    return email_list
