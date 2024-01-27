import os
# Imports os module
# Now we can use functions/methods that interact with the operating system
import glob
# Imports glob module, a standard library module, to use the glob() function

home_path = os.environ.get ('HOME')
# os.environ is a dictionary-like object containing key-value pairs for system information
# The HOME environment variable stores the user's home directory
# The get() method retrieves the value of the HOME environment variable
# The home_path variable stores the string value of the user's home directory

folder_name = 'HTMLPractise2024'
# No files in home_path. So added another folder with files to path.

wildcard_pattern = '*.html'
# A wildcard pattern is a file pattern designed to work consistently across different operating systems
# * matches any sequence of characters.
# Matches all files with a '.html' extension
# The wildcard_pattern variable stores the *.html wildcard pattern

full_path_pattern = os.path.join(home_path, folder_name, wildcard_pattern)
# os.path.join concatenates home_path, folder_name and wildcard_pattern
# os.path.join constructs the path by using the correct path separator for each platform.
# This ensures the code is portable and will work on different operating systems.

matching_files = glob.glob(full_path_pattern)
# glob.glob() returns files matching the full_path_pattern
# It is stored in the matching_files variable

print('Matching files using wildcard pattern:')
# Labels what output will be

for file_path in matching_files:
    # for loop iterates over each file in matching_files
    # Variable file_path stores the current file being processed in each iteration

    file_size = os.path.getsize(file_path)
    # Get the size of the current file and store it in file_size variable

    if file_size > 0:
    # If file_size is greater than 0

        print(os.path.basename(file_path), 'Size:', file_size, 'bytes')
        # As loop iterates, each file_path and file_size will be printed if the size is greater than 0
        # os.path.basename() returns the basename of a file path
    else:
        print(file_path, 'File has 0 bytes')
        # If a file has 0 bytes, this will be printed