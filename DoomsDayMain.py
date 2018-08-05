# decided to go with twisted, much more easy to work with.

try:
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
try:
    print("[**] Making falsified www root directory [**]")
    os.system("mkdir ./wwwroot")
    os.system("cd ./wwwroot")
except FileExistsError:
    print("[!!] Folder Exists, skipping for now [!!]")
    pass

os.system("mkdir ./wwwroot")
os.system("cd ./wwwroot")

database = sqlite3.connect('admin_databse.sqlite')
c = database.cursor()
#creating the junk filled and falsely encrypted database(make it mimic a glob)
#@todo database is complete, just missing the email address generation.
#@todo make a relational database, add some more hashes maybe sha1 and faked access times.
#@todo, alter the join times to reflect at least a month back in time.
c.execute('''CREATE TABLE IF NOT EXISTS Site_Info(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, jointime TIMESTAMP DEFAULT 
            CURRENT_TIMESTAMP NOT NULL, username TEXT, email TEXT, password TEXT)''')
#@todo, ok so this works. Need to find a way to populate legit looking IP address's
#@todo
''' or just take all the IP address's from lastb and cram them in here, 
    that way it all resolves back to "legit" sources.'''
c.execute('''CREATE TABLE IF NOT EXISTS Access_times(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT,
            FORIGN_KEY email REFERENCES username, Accessed_Last CURRENT_TIMESTAMP NOT NULL, Login_IP TEXT)''')
sql_stmt = "INSERT INTO Site_Info(username, email, password) VALUES ('%s', '%s', '%s')"
sql_stmt = str(sql_stmt)


def name_generate(num):
    digest_name = "INSERT INTO Site_Info(username, email, password) VALUES ('%s', '%s', '%s')"
    accessed_table = "INSERT INTO Access_times(login_ip) VALUES ('%s')"
    namer = set()
    for i in range(num):
        name = names.get_full_name()
        ename = name.lower()
        ename = ename.split(' ')
        email = email_generate(ename[0], ename[1])
        namer.add(name)
        ename = name.lower()
        ename = ename.split(' ')
        email = email_generate(ename[0], ename[1])
        print(name, email)
        database.commit()
        style = name.encode()
        hashed_pass = hashlib.sha512(style).hexdigest()
        c.execute(digest_name % (name, email, hashed_pass))
        c.execute(accessed_table % (lice))
        database.commit()


def email_generate(first, last):
    domains = ['sbcglobal.net', 'live.com', 'comcast.net', 'yahoo.com', 'gmail.com', 'icloud.com', 'gmx.com', 'lavabit.com',
               'charter.net', 'yandes.com', 'rocketmail.com', 'cox.net']
    numbers = randint(0,3)
    i = 0
    n = ''
    while i < numbers:
        n += str(randint(0, 9))
        i +=1
    if numbers > 0 and randint(0, 10) % numbers == 1:
        sep = '.'
    else:
        sep = ''
    return first+sep+last+str(n)+'@'+domains[randint(0, len(domains)-1)]


name_generate(100)
c.close()


#@todo set up on connection recieved, so we are not hogging precious system resources.

resource = File('./wwwroot')
factory = Site(resource)
endpoint = endpoints.TCP4Server(reactor, 8888)
endpoint.listen(factory)
reactor.run()
