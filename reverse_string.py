# This Program will reverse whatever string is
# given in the input and then proint it back out
# in the terminal/command line.


def backwards():
    # gets input from user as a string
    start_string = input("Please in put a string you would like reversed. ")
    # this reverses the string characters
    new_string = start_string[::-1]
    # this print statment will print out the the new reversed string to the terminal/ command line
    print ("The new reversed string is:", new_string)
# calls reverse string function
backwards()