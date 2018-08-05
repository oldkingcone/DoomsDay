# decided to go with twisted, much more easy to work with.

try:
    from faker import Faker
    import sqlite3
    import names
    import hashlib
    from twisted.web.server import Site
    from twisted.web.static import File
    from twisted.internet import reactor
    from twisted.internet import endpoints
    import os
    from time import sleep
    from random import randint
except ImportError as e:
    print(
        "Sorry... Something went wrong, try running pip install -r REQUIREMENTS and run the app again. \n {}".format(e))
    import sys
    sys.exit(1)
# ok, so tailor to your companies needs, but this should be a template.
# more to follow on this, trying to determine the best way to impliment this.
#@todo, impliment a streamlined way to generate false emails, that look rather legit.
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

# again, tailor to suit your needs, but this should be a good start.
words = ["barbie",
         "rocker",
         "diamond",
         "leet"
         ]

os.system("mkdir ./wwwroot")
os.system("cd ./wwwroot")

database = sqlite3.connect('admin_databse.sqlite')
c = database.cursor()
#creating the junk filled and falsely encrypted database(make it mimic a glob) - DONE
#@todo database is complete, just missing the email address generation.
#@todo make a relational database, add some more hashes maybe sha1 and faked access times.
#@todo, ok so this works. Need to find a way to populate legit looking IP address's - DONE
c.execute('''CREATE TABLE IF NOT EXISTS Site_Info(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                username TEXT, email TEXT, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Access_times(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT,
            FORIGN_KEY email REFERENCES username, login_ip TEXT)''')
sql_stmt = "INSERT INTO Site_Info(username, email, password) VALUES ('%s', '%s', '%s')"
sql_stmt = str(sql_stmt)

def name_generate():
    digest_name = "INSERT INTO Site_Info(username, password) VALUES ('%s', '%s')"
    accessed_table = "INSERT INTO Access_times(login_ip) VALUES ('%s')"
    namer = set()
    for i in range(100):
        faker = Faker()
        ip_addr = faker.ipv4()
        lice = str(ip_addr)
        name = names.get_full_name()
        namer.add(name)
        database.commit()
        style = name.encode()
        hashed_pass = hashlib.sha512(style).hexdigest()
        c.execute(digest_name % (name, hashed_pass))
        c.execute(accessed_table % (lice))
        database.commit()


name_generate()
c.close()


#@todo set up on connection recieved, so we are not hogging precious system resources.

resource = File('./wwwroot')
factory = Site(resource)
endpoint = endpoints.TCP4Server(reactor, 8888)
endpoint.listen(factory)
reactor.run()
