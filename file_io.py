file.read()
file.close()
file.closed #return False or True
file = open(file)

with open('filename', 'w'#for writing
    ) as f:
    #opens file, reads it, and then closes it for you
    data = f.read()
    #f.__exit__() is called
    file.write('something') #doesnt add to end, it replaces, creates file doesnt exist

#a for appending
#w for writing
#r is default and for reading
#r+ read and write toa file based on cursor, will not create a file if it doesnt exsist


