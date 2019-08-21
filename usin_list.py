shoplist = ['apples', 'mango', 'carrot', 'bananas']

print('I must buy', len(shoplist), 'products')

print('Products:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nAlso i must buy reece')
shoplist.append('reece')
print('For now my products list:', shoplist)

print('Sort products')
shoplist.sort()
print('Sorted products list:'), shoplist

print('First i was buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I buy', olditem)
print('This is my product list', shoplist)
