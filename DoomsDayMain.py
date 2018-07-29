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

os.system("mkdir ./wwwroot")
os.system("cd ./wwwroot")

database = sqlite3.connect('admin_databse.sqlite')
c = database.cursor()
#creating the junk filled and falsely encrypted database(make it mimic a glob)
c.execute('''CREATE TABLE IF NOT EXISTS Site_Info(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, jointime TIMESTAMP DEFAULT 
            CURRENT_TIMESTAMP NOT NULL, username TEXT, email TEXT, password TEXT)''')
sql_stmt = "INSERT INTO Site_Info(username, email, password) VALUES ('%s', '%s', '%s')"
sql_stmt = str(sql_stmt)

def name_generate():
    digest_name = "INSERT INTO Site_Info(username, password) VALUES ('%s', '%s')"
    namer = set()
    for i in range(100):
        name = names.get_full_name()
        namer.add(name)
        print(name)
        database.commit()
        style = name.encode()
        hashed_pass = hashlib.sha512(style).hexdigest()
        c.execute(digest_name % (name, hashed_pass))
        database.commit()

name_generate()
c.close()


def random_seeding(time):
    # going to be very hackish here.. sorry.
    sleep(time)

#@todo set up on connection recieved, so we are not hogging precious system resources.

resource = File('./wwwroot')
factory = Site(resource)
endpoint = endpoints.TCP4Server(reactor, 8888)
endpoint.listen(factory)
reactor.run()
