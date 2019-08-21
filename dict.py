#ab adress book
ab = {
    'name' : 'sdsdsd',
    'adress' : 'sdosdeee',
    'male' : 'john@mail.ru'
}


def func(name):
    for name in ab:
        if name == 'male':
            print(ab['male'])
func('john')

del ab['name']
print (ab)
print('\nВ адресной книге {} контактов\n'.format(len(ab)))
    

