#lists
list = [x for x in iterierbarem_object if ...]
#dictionaries
dic = {k: v for k,v in dict if ...}
#tuples
tuple1 = tuple(i for i in (1, 2, 3))
tuple2 = (i for i in (1, 2, 3)) #kein tuple sondern genrator object
print(tuple1, tuple2)
#sets
set = {s for s in [1, 2, 1, 0] }
set[1]