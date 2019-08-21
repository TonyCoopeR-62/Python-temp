# how much matches in this 3 variables
a = 2
b = 1
c = 3
def ints(a,b,c):
    if (a == b) and (a == c):
        print('3 numbs similar')
    elif (a == b) or (a == c) or (b == c):
        print('2 numbs similar')
    else:
        print('not matches')
ints(a,b,c)