baconFile = open('C:\\java\\pythonfolder\\bacon.txt', 'w')
baconFile.write('Hello bacon!\n')
baconFile.close()

baconFile = open('C:\\java\\pythonfolder\\bacon.txt', 'a')
baconFile.write('Bacon is not a vegetables')
baconFile.close()

baconFile = open('C:\\java\\pythonfolder\\bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)



