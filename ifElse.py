try : 
    integer = input()
    integer = int(integer) 
except :
    print('Please enter a numerical integer.')

if integer < 0 or integer > 100:
    print('Please enter an integer between 1 and 100')
    exit()
elif integer % 2 != 0:
    print('Weird')
    exit()
elif integer >= 2 and integer <= 5:
    print('Not Weird')
    exit()
elif integer >= 6 and integer <= 20:
    print('Weird')
    exit()
elif integer > 20: 
    print('Not Weird')
    exit()