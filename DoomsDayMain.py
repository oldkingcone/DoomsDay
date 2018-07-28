#decided to go with twisted, much more easy to work with.

try:
    import sqlite3
    from twisted.web.server import Site
    from twisted.web.static import File
    from twisted.internet import reactor
    from twisted.internet import endpoints
    import os
    from time import sleep
    from random import randint
except ImportError as e:
    print("Sorry... Something went wrong, try running pip install -r REQUIREMENTS and run the app again. \n {}".format(e))
    import sys
    sys.exit(1)
os.system("mkdir ./wwwroot")
os.system("cd ./wwwroot")
    
database = sqlite3.connect('admin_databse.sqlite')
c = database.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Site_Info(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, jointime TIMESTAMP DEFAULT 
            CURRENT_TIMESTAMP NOT NULL, username TEXT, email TEXT, password TEXT)''')
sql_stmt = "INSERT INTO Site_Info(username, email, password) VALUES ('%s','%s','%s')"
sql_stmt = str(sql_stmt)
def random_seeding(time):
    #going to be very hackish here.. sorry.
    sleep(time)
    
resource = File('./wwwroot')
factory = Site(resource)
endpoint = endpoints.TCP4Server(reactor, 8888)
endpoint.listen(factory)
reactor.run()
