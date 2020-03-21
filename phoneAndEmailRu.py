#! python3
#phoneAndEmailRu.py

import pyperclip, re


phoneRegex = re.compile(r'''(
             (\(\d{5}\))?       #код города
             (\s)               #пробел
             (\d\-\d{2}\-\d{2}) #номер телефона
             )''', re.VERBOSE)         

text = str(pyperclip.paste())
#print(text)
matches = []
for groups in phoneRegex.findall(text):
    #print(groups)
    phoneNum = groups[3]
    #print(groups[3])
    matches.append(phoneNum)
print(len(matches))
       
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addreses found.')
