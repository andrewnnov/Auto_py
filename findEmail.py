#! python3
# findEmail - searching email on the clipboard

import pyperclip, re
#example info@nostarch.com
emailRegex = re.compile(r'''(
             [a-zA-Z0-9._%+-]+
             @
             [a-zA-Z0-9.-]+
             (\.[a-zA-Z]{2,4})
             )''',re.VERBOSE)

# TODO: Find matches in clipboard text.

text = str(pyperclip.paste())
matches = []

for groups in emailRegex.findall(text):
    matches.append(groups[0])


# TODO: Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    
