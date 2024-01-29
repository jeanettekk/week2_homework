# Imported the getpass module which prevents echoing inputs on screen
import getpass

# The pin_attempts variable stores the max number of pin attempts
pin_attempts = 3

# The correct_pin variable stores an integer, the correct pin to access the bank
correct_pin = 2906

# The security_answer variable stores the correct answer to the security question.
security_answer = 'fluffy'

# A function was created because this block of code needs to be called twice.
# def defines a function called pin_reset with the parameter, attempts_parameter
# The pin_reset function will be used to reset correct_pin if the security question is answered correctly
def pin_reset(attempts_parameter):

    # if the argument called in the attempts_parameter variable is equal to 0, execute the next code.
    if attempts_parameter == 0:

        # Prints a string to inform the user of failed attempts and ask their security question.
        print('All attempts failed. Reset pin by answering this security question.\nWhat is your first pet\'s name?')

        # input() function requests an answer and stores it as a string in the user_answer variable
        user_answer = input('Enter answer here: ')

        # if the strings in security_answer is the same as user_answer, execute the next code.
        if security_answer == user_answer:

            # global indicates variables are global variables, belonging to the global scope.
            # Declaring global means, use these global variables instead of creating new local variables
            global correct_pin
            global pin_attempts

            # getpass.getpass() function securely takes the input of a new pin without displaying it on screen.
            # int() function converts the input string into and integer.
            # The new pin is stored in the global variable, correct_pin.
            correct_pin = int(getpass.getpass('Enter NEW pin: '))

            # Add 3 to pin_attempts value and store the new value in that variable.
            # This wil reset the max pin attempts and allow the user to try again with their new pin.
            pin_attempts += 3

        # if the strings in security_answer and user_answer are NOT the same, execute the next code.
        else:
            # Informs the user that security is being called due to suspicious activity
            print('Answer incorrect: Calling security...')

# The while loop will keep executing this block of code until the pin_attempts variable is 0
while pin_attempts > 0:
    
    # Used the str() function to convert correct_pin into a string
    correct_string = str(correct_pin)

    # The getpass.getpass() function securely takes input without displaying it on screen
    # The input is stored in the supplied_pin variable
    supplied_pin = getpass.getpass('Enter your pin: ')

    # If the strings in supplied_pin is equal to the correct_pin, execute the next code
    if supplied_pin == correct_string:

        # Prints a string to indicate the user has entered their pin successfully
        print('Welcome to High Street Bank!')

        # break statement is used to exit a loop
        break

    # If supplied_pin is NOT equal to the correct_pin, execute the next code
    else:
        # != checks if the length of characters in supplied_pin is NOT equal to correct_string
        # != is a comparison and boolean operator, returns True or False
        # .isnumeric() is a method that checks if a string contains only numeric characters, returns True or False
        # 'not' negates the truth value, it checks if supplied_pin is NOT only numeric characters
        # 'or' means, if either statements are True, execute the next code
        if len(supplied_pin) != len(correct_string) or not supplied_pin.isnumeric():

            # Subtract 1 from pin_attempts value and store the new value in that variable.
            pin_attempts -= 1

            # Prints a string and integer to inform the user how many digits is required and pin attempts left.
            print('Pin needs to be 4 digits. You have', pin_attempts, 'attempts left')

            # Calls the function pin_reset and uses the value of pin_attempts as an argument
            pin_reset(pin_attempts)

        # if either of the previous if statements are NOT True, execute the next code
        else:
            # Subtracts 1 from pin_attempts then assigns the new value to the pin_attempts variable
            pin_attempts -= 1

            # Prints a string to indicate the user input the wrong pin and how many attempts left.
            print('Incorrect pin. You have', pin_attempts, 'attempts left')

            # Calls the function pin_reset and uses the value of pin_attempts as an argument
            pin_reset(pin_attempts)
