myPets = ['q', 'w', 'e', 'r', 't', 'y']
print('Enter name: ')
name = input()
if name not in myPets:
    print('not')
else:
    print('name ' + name)
