import requests
res = res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

res.status_code == requests.codes.ok

len(res.text)

print(res.text[:100])

# Checking for Errors

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))


#Saving Downloaded files to the hard drive
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('C:\\python\\Romeo\\RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()


