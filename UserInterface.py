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
            'search'    :sys.exit, 
            'logout'    :self.logout, 
            'location'  :sys.exit }
            #'view'      :sys.exit }
        # TODO use saved settings?
        self.inputCommand()


    def inputCommand(self):
        print "\n---Enter a command---"
        command = raw_input("") 
        
        # Checks for valid input, and then executes appropriate code
        try:
            self.commandFunctions[command]()
        # If input is invalid, displays error
        except KeyError:
            self.displayInvalidCommand(command)

        # Allows for next command to be inputted
        self.inputCommand()

    # Real methods
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

    def displayInvalidCommand(self, command):
        print "* \"" + command + "\" is not a valid command, try again"

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
