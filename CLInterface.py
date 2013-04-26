import urllib2 
import requests 

class CLInterface:
    def __init__(self):
       self.username = None
       self.password = None
       self.location = None

    # Getters and setters
    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    # Real methods
    def search(self, category, query):
        response = urllib2.urlopen('http://gainesville.craigslist.org')
        html = response.read()
        payload = {'catAbb': category, 'query': query}
        r = requests.get('http://gainesville.craigslist.org/search/', params=payload)
        print r.text

    def status(self):
        print "Username: " + str(self.username)
        print "Location: " + str(self.location)
