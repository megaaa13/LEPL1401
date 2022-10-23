command = input('Enter your command: ')
try:
    parameters = command.split ()
    if parameters[0] == "divide":
        print ( "The value of your division is: {0}".format ( float(parameters[1])/float(parameters[2])))
    elif parameters[0] == "showfile":
        with open( parameters[1] ) as file:
            print ( file.read () )
    else:
        print ( "Command not recognized")
except:
    print("There was an error")
