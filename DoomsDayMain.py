# decided to go with twisted, much more easy to work with.

try:
    import itertools
    import random
    import email_chooser
    from faker import Faker
    import sqlite3
    import names
    from faker import Faker
    import hashlib
    from twisted.web.server import Site
    from twisted.web.static import File
    from twisted.internet import reactor
    from twisted.internet import endpoints
    from twisted.internet.protocol import Factory, Protocol
    from twisted.internet.endpoints import TCP4ServerEndpoint
    import os
    from time import sleep
    from time import time
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

print("[**] Making falsified www root directory [**]")
if os.system("mkdir ./wwwroot") == FileExistsError or os.system("mkdir ./wwwroot") != FileExistsError: 
    os.system("cd ./wwwroot")

database = sqlite3.connect('./wwwroot/admin_databse.sqlite')
c = database.cursor()

#@todo database is complete, just missing the email address generation.
#@todo make a relational database, add some more hashes maybe sha1 and faked access times.
c.execute('''CREATE TABLE IF NOT EXISTS Site_Info(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                username TEXT, email TEXT, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Access_times(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT,
            FORIGN_KEY email REFERENCES username, login_ip TEXT)''')

<<<<<<< HEAD

def name_generate(num):
    digest_name = "INSERT INTO Site_Info(username, email, password) VALUES ('%s', '%s', '%s')"
    accessed_table = "INSERT INTO Access_times(login_ip, Accessed_Last) VALUES ('%s', '%s')"
    namer = set()
    current_time = time()
    for i in range(num):
        name = names.get_full_name()
        faker = Faker()

        access_time = randint(1501942129, int(current_time))
        ip_addr = faker.ipv4()
        lice = str(ip_addr)
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
        c.execute(accessed_table % (lice, access_time))
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
=======
def name_generate(length):
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
#while alcohol == true: break
length = random.randint(100, 400)
name_generate(length)
>>>>>>> master
c.close()


#@todo set up on connection recieved, so we are not hogging precious system resources.
# going to start working on this tomorrow at some point. Yall be patient.

class QOTD(Protocol):
    #@todo This is designed as a small piece of SE. Makes the system seem more juicy, tailor as needed.
    # Will refine this when I have more time, currently in an Airport.
    def connection_made(self):
        self.transport.write("\nFor Official Use Only (FOUO) is a document designation, not a classification. "
                             "This designation is used by Department of Defense and a number of other federal agencies "
                             "to identify information or material which, although unclassified, may not be appropriate "
                             "for public release. In all cases the designations refer to unclassified, sensitive "
                             "information that is or may be exempt from public release under the Freedom of Information"
                             "Act. DoD Directive 5400.7 defines For Official Use Only information as unclassified "
                             "information that may be exempt from mandatory release to the public under the Freedom of "
                             "Information Act (FOIA). The policy is implemented by DoD Regulation 5400.7-R and 5200.1-R."
                             "\n")
        #@Todo, Need to impliment a "Login" method.

        self.transport.loseConnection()

class QOTDFactory(Factory):
    def buildProtocol(self, addr):
        return QOTD()


if __name__ == "__main__":
    port_range = random.randint(8123,45950) # Using random port range, so things cannot be so easily finger printed.
    print("[!!]\n\tVERY IMPORTANT! This port was selected: {} [!!]".format(port_range))
    endpoint = TCP4ServerEndpoint(reactor, port_range)
    endpoint.listen(QOTDFactory())
    reactor.run()
    # resource = File('./wwwroot')
    # factory = Site(resource)
    # endpoint = endpoints.TCP4ServerEndpoint(reactor, port_range)
    # endpoint.listen(factory)
    # reactor.run()
