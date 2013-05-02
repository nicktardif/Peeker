import urllib2 
import requests 
from bs4 import BeautifulSoup as BS
from Item import Item

class CLInterface:
    def __init__(self):
       self.username = None
       self.password = None
       self.location = 'gainesville' 

    # Getters and setters
    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.password = location

    # Real methods
    def search(self, category, query):
        siteLink = 'http://' + self.location + '.craigslist.org/search/'
        payload = {'catAbb': category, 'query': query}
        r = requests.get(siteLink, params=payload)

        soup = BS(r.text)
        allItems = soup.find(id='toc_rows').find_all('p', {'class' : 'srch row'})
        i = 1
        for html in allItems:
            item = Item(html)
            #print str(i) + '. ' + str(item)
            print("{0:{1}} {2}".format(str(i)+".", 4, str(item)))
            i = i + 1
    def status(self):
        print "Username: " + str(self.username)
        print "Location: " + str(self.location)
