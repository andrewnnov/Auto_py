catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames)+1) + ' (Or enter nothin to stop)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat name are: ')
for name in catNames:
    print(' ' + name)
          
