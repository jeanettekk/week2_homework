# import package getpass4
import getpass4

# hardcode correct value of user PIN
pin = '7860'

# iterative loop runs three times, from value of integer attempt = 1 to attempt =3 (excludes 4)
for attempt in range(1, 4):
    # print("\nPlease enter your PIN: ")
    # calls the module getpass() from package getpass4 and asks for user input discreetly (masks the input with asterix)
    supplied_pin = getpass4.getpass(prompt='Password: ')
    # checks for condition if user input is equal to hardcoded value of user PIN
    if supplied_pin == pin:
        # if true, print success message and exit the program
        print("Validation Success!")
        break
    else:
        # otherwise print message that input is incorrect and count attempt
        print("Incorrect PIN \nYou have used " + str(attempt) + " attempt(s)!")
        # if three wrong attempts have been taken print pin is blocked and exit
        if attempt == 3:
            print("Your PIN is now blocked!")
