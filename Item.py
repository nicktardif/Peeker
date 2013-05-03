class Item:
    def __init__(self, html):
        self.name = None
        self.date = None
        self.price = None
        self.descriptionLink = None
        self.ownerEmail = None
        self.ownerPhone = None
        self.generateItemAttributes(html)

    def generateItemAttributes(self, html):

        # Guaranteed attributes

        self.name = html.find('span', {'class' : 'title1'}).find('a').text
        # Truncate name to 59 characters
        self.name = (self.name[:59]) if len(self.name) > 30 else self.name
        self.name = self.name.encode('utf-8')

        self.date = html.find('span', {'class' : 'itemdate'}).text.encode('utf-8')

        # Not-guaranteed attributes
        priceHTML = html.find('span', {'class' : 'itemprice'})
        if (priceHTML == None):
            self.price = "???".encode('utf-8')
        else:
            self.price = priceHTML.text.encode('utf-8')

    def __str__(self): 
        return "{0} // {1:{2}} // {3}".format(self.date, self.price, 6, self.name)
