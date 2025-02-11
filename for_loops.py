for x in list(['Rock', 'Paper', 'Scissor']):
    print(x)

#ranges
range(7) #creates integers from 0 thru 6
range(1,8) #creates integers from 1 to 7
range(1,10.2) #will start at 1 and ends at 9, in steps by 2


numb = int(input('How many times do I have to tell you? '))
for i in range(numb):
    print('CLEAN UP YOUR ROOM')


for x in range(1,21):
    if x == (4 or 13):
        print(f'{x} is unlucky')
    elif x%2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')

#or
for x in range(1,21):
    if x == 4 or x == 13:
        state = 'unlucky'
    elif x%2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{x} is {state}')


numb = int(input('How many times do I have to tell you? '))
for i in range(numb):
    print('CLEAN UP YOUR ROOM')
    if i == 1:
        print('I\'m not gonna tell you a third time!')
        break