nums = [1, 2, 3, 4, 5]
nums_com = [x*10 for x in nums]
print(nums_com)



friends = ["moritz", "lavinia", "nico"]
friends_upper = [friends.upper() for friends in friends]
friends_firstupper = [friends[0].upper()+ friends[1:] for friends in friends]
print(friends_upper)
print(friends_firstupper)



nums_string = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
nums_int = [int(x) for x in nums_string] #to convert all elements from string to integer
nums_even = [x for x in nums_int if x%2==0] #to get all even number
print(nums_even)

nums_whatever = [x*2 if x%2==0 else x/2 for x in nums_int]
nums_whatever = []
for x in nums_int:
    if x % 2 == 0:
        nums_whatever.append(x*2)
    else:
        nums_whatever.append(x/2)


print(nums_whatever)


answer = [[i for i in range(0,3)] for num in range(0,3)]
print(answer)

answer2 = []
for num in range(0,3):
    answer3 = []
    for i in range(0,3):
        answer3.append(i)
    answer2.append(answer3)

print(answer2)