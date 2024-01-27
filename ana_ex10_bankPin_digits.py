# hardcode correct value of user PIN
pin = '7860'

# iterative loop runs three times, from value of integer attempt = 1 to attempt =3 (excludes 4)
for attempt in range(1, 4):
    # asks for user input and assigns it to variable supplied_pin
    supplied_pin = input("\nPlease enter your PIN: ")
    if supplied_pin == pin:
        # if entered pin is correct pint success and exit
        print("Validation Success!")
        break
    else:
        # otherwise print incorrect pin and count attempt
        print("Incorrect PIN \nYou have used " + str(attempt) + " attempt(s)!")
        # if 3 wrong attempts are done print pin blocked and exit the program
        if attempt == 3:
            print("Your PIN is now blocked!")
