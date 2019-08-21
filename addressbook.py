import os
import string
import pickle


adbookfile = 'adbook.txt'
addressbook = {
    "ann"  : 89123,
    "magg" : 2399,
    "peter": 83734,
    "john" : 11112
}
f = open(adbookfile, 'wb')
pickle.dump(addressbook, f) # put obj into file
f.close()

#del addressbook # delete var adrbook

f = open(adbookfile, 'rb')
showadr = pickle.load(f)
for i in addressbook:
    print(i)
print("=======================")
inp = input('''Input command -> :\n
    type update(x) to add, type pop(x) to remove: ''')
exec(inp)
print(addressbook)