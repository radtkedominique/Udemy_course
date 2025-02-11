test = ["a", True, 47]
print(len(test))

nums = list(range(1,100))

for i in test:
    print(i)

while i < len(test):
    print(test[i])
    i += 1


test.append("b")
len(test) # is now 4

test.append([4, 5])
len(test) #is now 5, because [4, 5] is one element

test.extend([5, 6]) #appends multiple elements at the end


test.insert(2, "c") # inserts 'c' at position 2
test.insert(len(test), "end") #inserts at the end

test.clear() #delets all elements in a list
test.pop(3) #delets element at position 3
test.pop(0) #delets last element

test.remove("c") #will remove "c" at the first instance found that matches, if none found error

test.index("c") #will give you the index of the first instance that matches
test.index(47, 1) #start at index 1 and search from there on
test.index("c", 1, 4)  #starts at 1 and stops at 4

test.count("c") #counts the amount of instances of 'c'

test.reverse() #reverses list

test.sort() #sorts in ascending order

#join-method actually a string method
#used to convertes lists to string
"_".join(test) #will join elements of list in a string with '_' in between as connector

#slicing
test[1:6:2] #start:1 end:6 step:2
test2 = test[:] #copies test, own address in memory

sum(test2) #gives you the sum of all elements

#list comprehension
#list in list

