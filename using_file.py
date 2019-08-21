poem ='''\
    Programming is fun
    If work too bored
    To give her cheerful tone
    Just use Python!
    '''
f = open('poem.txt', 'w') # open for writing
f.write(poem) # write in file
f.close() # close file

f = open('poem.txt') # default is reading

while True:
    line = f.readline()
    if len(line) == 0: # end of line if length = 0
        break
    print(line, end='')
f.close() # close file
