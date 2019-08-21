# shows if possible to make a move for king (hor, vert and diag, 1 cell)
# 8*8 cells
def king(a1,b1,a2,b2):
    if ((-1 <= (a2-a1) <= 1) and (-1 <= (b2 - b1) <= 1)):
        print('yes')
    else:
        print('nop')
king(4,4,6,4)
king(2,3,3,4)