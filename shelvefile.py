#Saving Variables with the shelve Module
import shelve
shelfFile = shelve.open('C:\\java\\pythonfolder\\mydata')
cats = ['Zo', 'Po', 'Si']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('C:\\java\\pythonfolder\\mydata')
print(type(shelfFile))
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()



