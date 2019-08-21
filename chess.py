# shows matches if selected cells has similar color
# 8*8 cells
def chess(a1,b1,a2,b2):
    if (((a1 % 2 == 1) and (b1 % 2 == 1)) or ((a1 % 2 == 0) and (b1 % 2 ==0))):
        a1b1 = 'black'
        print('a1-b1 is black')
    else:
        a1b1 = 'white'
        print('a1-b1 is white')
    if (((a2 % 2 == 1) and (b2 % 2 == 1)) or ((a2 % 2 == 0) and (b2 % 2 ==0))):
        a2b2 = 'black'
        print('a2-b2 is black')
    else:
        a2b2 = 'white'
        print('a2-b2 is white')
    if (a1b1 == a2b2):
        print ('cells is similar')
chess(1,3,3,3)
     