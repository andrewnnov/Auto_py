number = 0

def collatz(number):
    try:
        if number % 2 == 0:
            print(int(number//2))
        else:
            print(int(number * 3 + 1))           
        
    except TypeError:
        print('Please type number')
    
    
collatz(3)
collatz(5)
collatz(8)
collatz(2)
collatz(0)
collatz('root')
