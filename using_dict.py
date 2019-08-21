ab = {
    'swaroop' : 'swaroop@mail.ru',
    'larry'   : 'ldlksj',
    'ann'     : 'sdfggrrrr',
    'spam'    : 'ssgg'
}
print('adress of swaroop is:', ab['swaroop'])

del ab['spam']

for name, address in ab.items():
    print('contact {0} with adress {1}'.format(name, address))

ab['guido'] = 'gui@mail.ru'
if 'guido' in ab:
    print("\nAdress of guido:", ab['guido'])
