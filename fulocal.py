x = 50
def func(x):
    print('x equals', x)
    x = 2
    print('edit local x on', x)

func(x)
print('x also', x)