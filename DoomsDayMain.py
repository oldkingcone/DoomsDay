# decided to go with twisted, much more easy to work with.

try:
    import email_chooser
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

try:
    print("[**] Making falsified www root directory [**]")
    os.system("mkdir ./wwwroot")
    os.system("cd ./wwwroot")
except FileExistsError:
    print("[!!] Folder Exists, skipping for now [!!]")
    pass

database = sqlite3.connect('./wwwroot/admin_databse.sqlite')
c = database.cursor()

#@todo database is complete, just missing the email address generation.
#@todo make a relational database, add some more hashes maybe sha1 and faked access times.
c.execute('''CREATE TABLE IF NOT EXISTS Site_Info(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                username TEXT, email TEXT, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Access_times(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT,
            FORIGN_KEY email REFERENCES username, login_ip TEXT)''')
sql_stmt = "INSERT INTO Site_Info(username, email, password) VALUES ('%s', '%s', '%s')"
sql_stmt = str(sql_stmt)
def email_generate():
    return "[!!] Work in progress, sorry! [!!]"

def name_generate(length):
    ip_net = set()
    digest_name = "INSERT INTO Site_Info(username, password) VALUES ('%s', '%s')"
    accessed_table = "INSERT INTO Access_times(login_ip) VALUES ('%s')"
    email_gend = set()
    fake_names = set()
    email_gend.add(email_chooser(genEmail(length)))
    for i in range(length):
        faker = Faker()
        ip_addr = faker.ipv4()
        ip_net.add(str(ip_addr))
        name = names.get_full_name()
        styled_names = name.encode()
        fake_names.add(str(styled_names))
        hashed_pass = hashlib.sha512(style).hexdigest()
        c.execute(digest_name % (name, hashed_pass))
        c.execute(accessed_table % (lice))
        database.commit()
#while alcohol == true: break
length = random.randint(100, 400)
name_generate(length)
c.close()


#@todo set up on connection recieved, so we are not hogging precious system resources.

resource = File('./wwwroot')
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
endpoint.listen(factory)
reactor.run()
