zoo = 'zebra', 'elephant', 'tiger', 'penguin'
a = len(zoo)
print('Numbers of enimals:', a)
new_zoo = 'monkey', 'camel', zoo
print('Number of cells:', len(new_zoo))
print('All animals in new zoo:', new_zoo)
print('animals from old zoo:', new_zoo[2])
print('last animal from old zoo:', new_zoo[2][a-1])
print('animals in new zoo:', len(new_zoo)-1 + len(new_zoo[2]))