# importing three modules in separate statements to optimize imports
import glob
import os
import sys

# line below prints the value of my environment variable
print("\n HOMEPATH = ", os.getenv('HOMEPATH'))

# Get the directory name
# If os is windows, provide string HOMEPATH otherwise (for mac) provide HOME
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# print("\n", hdir)

# Construct a portable wildcard pattern
# Join the home directory path to the names of all contained files
pattern = os.path.join(hdir, '*')

# using the glob.glob() function to obtain the list of filenames
list_filenames = glob.glob(pattern)
print("\n File Names:", list_filenames)

# using os.path.getsize to find each file's size
print("\n Number of files =", len(list_filenames))
print("\n Printing sizes of all files")
# iterative loop prints for all the files in the list
for file in list_filenames:
    print("File "+file + " is of size: ", os.path.getsize(file))

# Add a test to only display files that are not zero length
print("\n Printing sizes of all Non-empty files Only")
# iterative loop prints for all the files in the list
for file in list_filenames:
    if os.path.getsize(file) > 0:
        print("File "+file + " is of size: ", os.path.getsize(file))

# Remove the leading directory name(s) from each filename before print using os.path.basename()
print("\n Now printing filenames without base directory")
# iterative loop prints for all the files in the list
for file in list_filenames:
    print(os.path.basename(file))
