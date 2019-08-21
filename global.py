x = 10
def func():
    global x
    print('x equals ', x)
    x = 2
    print('change global x to ', x)
func()
print('x equals ', x)
