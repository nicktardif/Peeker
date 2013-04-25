import urllib2 
import requests 
class UserInterface:
    # This class handles user input, output, and
    # the current position in the program

    def __init__(self):
        self.username = None

    # Getters and setters
    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    # Real methods
    def promptUsername(self):
        username = raw_input("What is your username?\n")
        self.setUsername(username)
        print "Your username is " + self.username

response = urllib2.urlopen('http://gainesville.craigslist.org')
html = response.read()
payload = {'areaID': '210', 'catAbb': 'sss', 'query': 'bike'}
r = requests.get('http://gainesville.craigslist.org/search/', params=payload)
print r.url
print r.status_code
print r.text

ui = UserInterface()
ui.promptUsername()
print ui.getUsername()
