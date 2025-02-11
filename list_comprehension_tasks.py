#Practice

#I needed practice, so I used this list.

#1. Find all of the numbers from 1-1000 that are divisible by 7
numbers = [x for x in range(1,1001) if x%7==0]
print(numbers)
#2. Find all of the numbers from 1-1000 that have a 3 in them
numbers = [x for x in range(1,1001) if '3' in str(x)]
print(numbers)
#3. Count the number of spaces in a string
sentence = "hallo wie geht es dir?"
count = len([x for x in sentence if x==" "])
print(count)
#4. Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
consonats = [x for x in 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
             if x not in 'aeiouAEIOU ']
print(consonats)

#5. Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)

#6. Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common = [x for x in list_a if x in list_b]
print(common)

#7. Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
numbers = [x for x in 'In 1984 there were 13 instances of a protest with over 1000 people attending'.split(" ")
           if x.isdigit()]
print(numbers)

#8. Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word
# ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
numbers = ['even' if x%2==0 else 'odd' for x in list(range(0,20))]
print(numbers)

#9. Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9,
# list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)

#10. Find all of the words in a string that are less than 4 letters
sentence = "hallo wie geht es dir?"
numbers = [x for x in sentence.split(" ") if len(x)<5]
print(numbers)

#11. Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit
# besides 1 (2-9)
#i=2
#divisible = [x for x in range(1,1001) if x%i==0 for i in [2,3,4,5,6,7,8,9,]]
#print(divisible)
#with help:
divisible = [x for x in range(1, 1001) if any(x%i == 0 for i in range(2,10))] #instead of range(2,10) could do [2,3,5,7] bc of multiples
print(divisible)

divisible = []
for x in range(1, 1001):
    for i in range(2, 10):
        if x % i == 0:
            divisible.append(x)
            break
print(divisible)