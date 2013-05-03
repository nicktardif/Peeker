from CLInterface import CLInterface
import sys

class UserInterface:
    # This class handles user input, output, and
    # program flow

    def __init__(self):
        self.cli = CLInterface()
        self.commandFunctions = {
            'login'     :self.promptCredentials, 
            'help'      :self.help, 
            'status'    :self.cli.status,
            'exit'      :sys.exit, 
            'search'    :self.search, 
            'logout'    :self.logout, 
            'location'  :self.locationSet }
            #'view'      :sys.exit }
        # TODO use saved settings?
        self.inputCommand()


    def inputCommand(self):
        print "\n---Enter a command---"
        try:
            command = raw_input("") 
        except KeyboardInterrupt:   #handles ^C input
            sys.exit()
        except EOFError:            #handles ^D input
            sys.exit()

        commandArgs = command.split(' ')
        
        # Checks for valid input, and then executes appropriate code
        try:
            if (commandArgs[0] == "search"):
                self.search(commandArgs[1], commandArgs[2])
            else:
                self.commandFunctions[command]()
        # If input is invalid, displays error
        except KeyError:
            print "* \"" + command + "\" is not a valid command, try again"
    
        #except TypeError:
            #print "* Wrong number of input arguments, try again"

        # Allows for next command to be inputted
        self.inputCommand()

    def promptCredentials(self):
        username = raw_input("* What is your username?\n")
        password = raw_input("* What is your password?\n")

        # TODO Check if combination is valid

        self.cli.setUsername(username)
        self.cli.setPassword(password)
        print "* You are successfully logged in"

    def logout(self):
        self.cli.setUsername(None)
        self.cli.setPassword(None)
        print "* You are successfully logged out"

    def locationSet(self):

        # --- Gets the continent ---
        print "* Select your continent"
        continentList = self.cli.getContinents()
        i = 1
        # Outputs the continent list
        for continent in continentList:
            print("{0:{1}} {2}".format(str(i)+".", 4, continent.split(',')[1]))
            i = i + 1
        # User selects the continent
        inputNum = raw_input("* Input the number of your continent. ")
        continentCode = continentList[int(inputNum) - 1].split(',')[0]
        print continentCode

        # --- Gets the region ---
        print "* Select your region"
        regionList = self.cli.getRegions(continentCode)
        i = 1
        # Outputs the region list
        for region in regionList:
            print("{0:{1}} {2}".format(str(i)+".", 4, region))
            i = i + 1
        # User selects the region
        inputNum = raw_input("* Input the number of your region. ")
        regionCode = regionList[int(inputNum) - 1]
        print regionCode

        # --- Gets the location ---
        print "* Select your location"
        locationList = self.cli.getLocations(regionCode)
        i = 1
        # Outputs the location list
        for location in locationList:
            print("{0:{1}} {2}".format(str(i)+".", 4, location.split(',')[1]))
            i = i + 1
        # User selects the location
        inputNum = raw_input("* Input the number of your location. ")
        locationCode = locationList[int(inputNum) - 1].split(',')[0]

        # Set the location in the program
        locationCode = locationCode.split('//')[1].split('.')[0]
        self.cli.setLocation(locationCode) 
        print "* Location successfully set to " + locationCode

    def search(self, category, query):
        itemList = self.cli.search(category, query) 
        for item in itemList:
            print item
        

    def help(self):
        print "\nAvailable Commands"
        print "Exit: exits the program immediately"
        print "Location"
        print "-- [change]: changes the location"
        print "-- [list]: lists all locations"
        print "Login: accepts user information and logs into Craigslist"
        print "Logout: logs current user out of Craigslist"
        print "Search"
        print "-- [category] [query]: searches the input query in the specified category"
        print "-- [category] [list]: displays all the possible categories to search"
        print "Status: display the current user status"
