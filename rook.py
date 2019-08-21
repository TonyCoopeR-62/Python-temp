# show if possible to make a move for rook (vert and horiz lines)
# 8*8 cells
# a1,b1 - is first cell coords
# a2,b2 - second cell coords
def rook(a1,b1,a2,b2):
    if a2 == a1 or b2 == b1:
        print('yes') 
    else:
        print('no')
rook(2,6,3,3)
     