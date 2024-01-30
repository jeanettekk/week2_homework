# week 2 homework Exercise 9 part 1
# This program uses strings, list and dictionary to store first and last names and then prints full name

# Created two variables, first_name and last_name, with string values using snake case
first_name = "Anagha"
last_name = "Jawalekar"

# Following statement prints the values of variables assigned above
# prints in new line using the new line character '\n'
print("\n", first_name, last_name)

# Following statement assigns list values to variable full_name
full_name = [first_name, last_name]

# Following statement prints the two values in the list
print("\n", full_name[0], full_name[1])

first_name = "Jeanette"
last_name = "Kho"

# The print function concatenates the string values of first_name, a space and last_name
print('\n', first_name + ' ' + last_name)

# Created a dictionary, full_name_dict, with the keys 'first' and 'last'
# Used first_name and last_name variables as values for the keys
full_name_dict = {'first': first_name, 'last': last_name}

# Print function outputs the keys and values in the dictionary, full_name_dict
print('\n', full_name_dict)

# the values() method returns values (without keys) from dictionary and the join() method
# joins values from any list together with a character in-between (in this case a white space)
print('\n' + ' '.join(full_name_dict.values()))
