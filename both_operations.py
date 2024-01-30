# week 2 homework Exercise 9 part 2
# This program asks for user input and performs some string operations on it

# Following statement asks for user input and assigns it to variable
user_string = input("Please enter an alphanumeric value: ")

# Following if/else conditional implies, if user string is numeric print no upper case
# otherwise convert it into upper case and print it
if user_string.isdecimal():
    print("\n Your input is numeric, hence no upper case!")
else:
    print("\n Your input in upper case would be: " + user_string.upper())
# In above statement upper() function converts user_string into upper case
# and print statement prints it concatenated with relevant description

# len(user_string) returns the length of user input string that needs to be converted into
# string using str() method to be able to concatenate with message string in print function
print("\n Length of your input is: " + str(len(user_string)))

# Alternatively, assign length to a variable first and then use that in print statement
length = str(len(user_string))
print("\n Length of your input is: " + length)

# The isdecimal() method returns a boolean value true if user string contains
# all numbers - if any of the characters in the input is not number, it returns false
# str() method here converts the returned boolean value from isdecimal() method
# to string so that it can join with other string message before printing
print("\n Your input contains all numeric characters: " + str(user_string.isdecimal()))

# Alternatively, assign isdecimal() return value to a variable first
# and then use that variable in print statement
true_or_false = str(user_string.isdecimal())
print("\n Your input contains all numeric characters: " + true_or_false)

# Created the dictionary, results_dict, to store the outcomes of the methods and functions
# Keys, 'uppercase', 'number_of_characters' and 'numeric_characters', are associated with these outputs
results_dict = {'uppercase': user_string.upper(), 'number_of_characters': len(user_string),
                'all_numeric_characters': user_string.isdecimal()}

# Print function outputs the dictionary, results_dict
print(results_dict)
