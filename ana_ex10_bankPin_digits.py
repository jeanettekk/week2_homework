# Week 2 homework: Exercise 10 Part 2

# This program asks for user input (PIN) for up to three times if previous input is incorrect
# Appropriate messages are printed for successful and unsuccessful attempts

# hardcode correct value of user PIN
pin = '7860'

# iterative loop runs three times, from number attempt = 1 to attempt =3 (excludes 4)
for attempt in range(1, 4):
    # asks for user input using the input() method and assigns entered user string to the variable supplied_pin
    supplied_pin = input("\nPlease enter your PIN: ")
    if supplied_pin == pin:
        # if entered pin is correct print success and exit
        print("Validation Success!")
        break
    else:
        # otherwise print incorrect and count attempts
        # following statement prints a formatted string so that a mix of string and other data types can be printed
        print(f"Incorrect PIN, you have used {attempt} attempt(s)...\n {3-attempt} attempt(s) remaining!")
        # if 3 wrong attempts are done print pin blocked and exit the program
        if attempt == 3:
            print("Your PIN is now blocked!")
