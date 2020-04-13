#! python3
# mapIt.py - Launches a map in the browser usingan address from the cpmand line

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #Get address from command line.
    address=' '.join(sys.argv[1:])
else:
    #Get addreses from clipboard
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)






    
