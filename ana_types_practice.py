# week 2 homework Exercise 9 part 1

# This program uses strings, list and dictionary to store first and last names and then prints full name

# Following two statements initialize two variables with strings
first_name = "Anagha"
last_name = "Jawalekar"

# Following statement prints the values of variables assigned above
print("\n", first_name, last_name)

# Following statement assigns string value to variable full_name which is
# concatenation of variables first_name, last_name and space in-between
full_name = first_name + " " + last_name

# Following statement prints the value of variable full_name
print("\n", full_name)

# Following statement assigns list values to variable full_name
full_name = [first_name, last_name]

# Following statement prints the two values stored in the list full_name
print("\n", full_name[0], full_name[1])

# Following statement concatenated strings from list full_name with space in-between
# before printing the combined string
print("\n", full_name[0] + " " + full_name[1])

# Storing key and value pairs for first and last names in dictionary variable full_name
full_name = {'name': first_name, 'surname': last_name}

# the values() method returns values (without keys) from dictionary and the join() method
# joins values from any list together with a character in-between (in this case a white space)
print('\n' + ' '.join(full_name.values()))






