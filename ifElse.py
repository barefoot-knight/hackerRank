try : 
    integer = input()
    integer = int(integer) 
except :
    print('Please enter a numerical integer.')

elif integer % 2 != 0:
    print('Weird')
elif integer >= 2 and integer <= 5:
    print('Not Weird')
elif integer >= 6 and integer <= 20:
    print('Weird')
elif integer > 20: 
    print('Not Weird')