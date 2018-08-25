# decided to go with twisted, much more easy to work with.
try:
    import itertools
    import random
    import email_chooser
    from faker import Faker
    import sqlite3
    import names
    import hashlib
    from twisted.web.server import Site
    from twisted.web.static import File
    from twisted.internet import reactor
    from twisted.internet import endpoints
    from twisted.internet.protocol import Factory, Protocol
    from twisted.internet.endpoints import TCP4ServerEndpoint
    import os
    from time import sleep
    from random import randint
except ImportError as e:
    print(
        "Sorry... Something went wrong, try running pip install -r REQUIREMENTS and run the app again. \n {}".format(e))
    import sys
    sys.exit(1)

def name_generate(length):
    print("[**] Making falsified www root directory [**]")
    if os.system("mkdir ./wwwroot") == FileExistsError or os.system("mkdir ./wwwroot") != FileExistsError:
        os.system("cd ./wwwroot")
    database = sqlite3.connect('./wwwroot/admin_databse.sqlite')
    c = database.cursor()
    # @todo database is complete, just missing the email address generation.
    # @todo make a relational database, add some more hashes maybe sha1 and faked access times.
    c.execute('''CREATE TABLE IF NOT EXISTS Site_Info(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                    username TEXT, email TEXT, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Access_times(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT,
                FORIGN_KEY email REFERENCES username, login_ip TEXT)''')
    ip_net = list()
    digest_name = "INSERT INTO Site_Info(username, email, password) VALUES ('%s', '%s', '%s')"
    accessed_table = "INSERT INTO Access_times(login_ip) VALUES ('%s')"
    fake_names = list()
    for i in range(length):
        faker = Faker()
        ip_addr = faker.ipv4()
        ip_net.append(str(ip_addr))
        name = names.get_full_name()
        styled_names = name.encode('utf-8')
        fake_names.append(styled_names)
    for (emails, fakes, ips) in itertools.zip_longest(email_chooser.genEmail(length), fake_names, ip_net):
        hashed_pass = hashlib.sha1(fakes).hexdigest()
        print('[**] {} \n {} \n {}\n {}\n [**]'.format(emails, fakes, ips, hashed_pass))
        fake = fakes.decode()
        c.execute(digest_name % (fake, emails, hashed_pass))
        c.execute(accessed_table % (ips))
    database.commit()
    c.close()

# while alcohol == true: break

# @todo set up on connection received, so we are not hogging precious system resources. -!- done.
# going to start working on this tomorrow at some point. Y'all be patient.

class QOTD(Protocol):

    # @todo This is designed as a small piece of SE. Makes the system seem more juicy, tailor as needed.
    # Will refine this when I have more time, currently in an Airport.
    # need to make a variable, for user input to a designated path, or default to the data directory for this. -!- done.
    # @todo, need to make more of these, inside several files, and have a random choice be made to select the file(s).
    def connection_made(self):
        # I added in the stuff variable with logic, because everyone has different needs.
        # I enjoy screwing with an attackers head as much as possible, so, this will show a different warning
        # on every connection, @todo will add a way to control that.
        stuff = ''
        if stuff == '':
            choice = random.randint(1, 5)
            if choice == 1:
                disclaimer = open('data/fouo.txt', 'r')
            reader = disclaimer.readlines()
            disclaimer.close()
        # This seems a bit buggy/hacky, will need to come back later and fix.
        self.transport.write(reader)
        # @Todo, Need to impliment a "Login" method.
        # login method needs to be simple yet complex enough to fool even the most suspecting of attackers.
        # Don't want to leave the bait entirely out in the open, but still leave the bait out in the open.

        self.transport.loseConnection()

class QOTDFactory(Factory):

    def buildProtocol(self, addr):
        # Writes warning out through chosen port and into the terminal, closes connection.
        return QOTD()

    def fileProtocol(self, addr):
        # chooses our generated spring loaded trap.
        resource = File('./wwwroot')
        factory = Site(resource)
        return factory

if __name__ == "__main__":

    queue = random.randint(100, 400)
    name_generate(queue)
    port_range = random.randint(8123, 45950)  # Using a random port range, so things cannot be so easily finger printed.
    print("[!!]\n\tVERY IMPORTANT! This port was selected: {} [!!]".format(port_range))
    endpoint = TCP4ServerEndpoint(reactor, port_range)
    endpoint.listen(QOTDFactory())
    reactor.run()
