var = input('Please enter a value: ')
# The input function displays a prompt and waits for the user to enter a string value
# The entered value is stored in the variable 'var'

results_dict = {'uppercase': var.upper(),'number_of_characters': len(var), 'numeric_characters': var.isdecimal()}
# Created the dictionary, results_dict, to store the outcomes of the methods and functions

# The .upper() method converts the string value of 'var' to uppercase
# The leng() function returns the number of characters in the string 'var'
# The .isdeccimal() method is a boolean that checks if all characters in the string 'var' are numeric

# Keys, 'uppercase', 'number_of_characters' and 'numeric_characters', are associated with these outputs

print(results_dict)
# Print function outputs the dictionary, results_dict