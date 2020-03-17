import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
print(mo.group(1))
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
