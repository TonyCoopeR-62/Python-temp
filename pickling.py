import pickle
# name of file that we used for saving
shoplistfile =  'shoplist.data'
# shopping list
shoplist = ['apples', 'mango', 'carrot']

# record file
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # append obj in file
f.close() # close file

del shoplist # del var
# read from memory
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # load from file
print(storedlist)