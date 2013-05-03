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
        self.location = location

    # Real methods
    def search(self, category, query):
        siteLink = 'http://' + self.location + '.craigslist.org/search/'
        payload = {'catAbb': category, 'query': query}
        r = requests.get(siteLink, params=payload)

        soup = BS(r.text)
        allItems = soup.find(id='toc_rows').find_all('p', {'class' : 'srch row'})
        i = 1
        result = []
        for html in allItems:
            item = Item(html)
            result.append("{0:{1}} {2}".format(str(i)+".", 4, str(item)))
            i = i + 1
        return result

    def getContinents(self):
        # Setting up the connection
        request = urllib2.Request("http://www.craigslist.org/about/sites/")
        response = urllib2.urlopen(request)
        soup = BS(response)

        continentLinks = []

        # Parsing the links
        for link in soup.find('div', {'class' : 'jump_to_continents'}).find_all('a'):
            continentLinks.append(str(link['href'].replace("#", "")) + "," + str(link.text))
        return continentLinks

    def getRegions(self, continentCode):
        # Setting up the connection
        request = urllib2.Request("http://www.craigslist.org/about/sites/")
        response = urllib2.urlopen(request)
        soup = BS(response)

        # Parsing the links
        continentLinks = soup.find_all('a', {'name' : continentCode})
        currentDiv = continentLinks[0].find_next('div')
        regions = []
        for region in currentDiv.find_all('h4'):
            regions.append(region.text)
        return regions 
    
    def getLocations(self, region):
        # Setting up the connection
        request = urllib2.Request("http://www.craigslist.org/about/sites/")
        response = urllib2.urlopen(request)
        soup = BS(response)

        # Parsing the links
        regionLinks = soup.find_all('h4')
        locationList = []
        locations = []
        print "region is " + region
        # again, unnecessary for loop
        for section in regionLinks:
            if (section.text == region):
                locations = section.find_next('ul').find_all('li')
                break
        for location in locations:
                locationList.append(str(location.find_next('a')['href'] + ',' + str(location.text)))

        return locationList

    def status(self):
        print "Username: " + str(self.username)
        print "Location: " + str(self.location)
