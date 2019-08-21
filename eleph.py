# shows if possible to make a move for elephant (diag cells)
# 8*8 cells

# enume = range(-8, 8, 1)
def elephant(a1,b1,a2,b2):
    if ((a2 - a1 <=8) and (b2 - b1 <=8)):
        print('yes')
    else:
        print('nop')


elephant(6,5,4,8)