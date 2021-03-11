### HackerRank Python If-Else
### barefoot.knight
### 03/10/2021

# Checks if user entered a numberical integer
try : 
    integer = input('Please enter an integer: ')
    integer = int(integer) 
except :
    print('Please enter a numerical integer.')

# Tests if even or odd
if integer % 2 != 0:
    print('Weird')

# Tests if between 2 and 5
elif integer >= 2 and integer <= 5:
    print('Not Weird')

# Tests if between 6 and 20
elif integer >= 6 and integer <= 20:
    print('Weird')

#  Tests if over 20
elif integer > 20: 
    print('Not Weird')