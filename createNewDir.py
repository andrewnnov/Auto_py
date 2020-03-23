import os
#os.makedirs('C:\\java\\pythonfolder')


path_to_file = 'C:\\java\\pythonfolder\\ex.txt'

#return file's name with ext
print(os.path.basename(path_to_file))

#return path without filename
print(os.path.dirname(path_to_file))

#return both with a tuple
print(os.path.split(path_to_file))

#return array with all part of path
print(path_to_file.split(os.path.sep))

#Finding File Sizes and Folder Contents

#return file's size
print(os.path.getsize(path_to_file))

#return all files in directories
print(os.listdir('C:\\Projects'))

#Checking Path Validity
print(os.path.exists('C:\\Projects'))

print(os.path.isdir('C:\\Projects'))

print(os.path.isfile('C:\\java\\pythonfolder\\ex.txt'))
