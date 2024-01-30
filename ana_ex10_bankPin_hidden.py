# Week 2 homework: Exercise 10 Part 3

# This program asks for user input (PIN) discreetly (masks the input on screen) for up to three times if
# previous input is incorrect. Appropriate messages are printed for successful and unsuccessful attempts

# importing getpass package to access getpass module inside it which hides user input (shows blank)
# import getpass
# importing getpass4 package to access getpass module inside it which masks user input with asterix
import getpass4

# hardcode correct value of user PIN
pin = '7860'

# Getting user PIN in first for loop by using getpass module from getpass package masking user pin with blank and then
# repeating the same in second for loop by using getpass module from getpass4 package masking user pin with asterix
#
# # iterative loop runs three times, from value of integer attempt_getpass = 1 to attempt_getpass =3 (excludes 4)
# for attempt_getpass in range(1, 4):
#     # assigns the value of pin string provided by user via getpass method to supplied_pin
#     # the getpass module from getpass package works fine with any string prompt
#     supplied_pin = getpass.getpass(prompt='Please enter your PIN: ')
#     # following code checks for condition if user input is equal to hardcoded value of user PIN
#     if supplied_pin == pin:
#         # if true, print success message and exit the program
#         print("Validation Success!")
#         break
#     else:
#         # otherwise print message that input is incorrect and count attempt_getpass
#         print(f"Incorrect PIN, you have used {attempt_getpass} attempt(s)\n{3 - attempt_getpass}
#         attempt(s) remaining!")
#         # if three wrong attempts have been taken print pin is blocked and exit
#         if attempt_getpass == 3:
#             print("Your PIN is now blocked!")

# print('\nRound 2 of entering PIN using another input method...')

# iterative loop runs three times, from value of integer attempt_getpass4 = 1 to attempt_getpass4 =3 (excludes 4)
for attempt_getpass4 in range(1, 4):
    # assigns the value of pin string provided by user via getpass method to supplied_pin
    supplied_pin = getpass4.getpass(prompt='Please enter your PIN: ')
    # following code checks for condition if user input is equal to hardcoded value of user PIN
    if supplied_pin == pin:
        # if true, print success message and exit the program
        print("Validation Success!")
        break
    else:
        # otherwise print message that input is incorrect and count attempt_getpass4
        print(f"Incorrect PIN, you have used {attempt_getpass4} attempt(s)\n{3 - attempt_getpass4}"
              f" attempt(s) remaining!")
        # if three wrong attempts have been taken print pin is blocked and exit
        if attempt_getpass4 == 3:
            print("Your PIN is now blocked!")
