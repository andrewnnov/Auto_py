#OS system
import os
print(os.path.join('usr', 'bin', 'spam'))

myFiles = ['account.txt', 'details.csv', 'invite.docs']
for fileName in myFiles:
    print(os.path.join('C:\\Java\\ex', fileName))
