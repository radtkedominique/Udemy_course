for i in range(1,11):
    print('\U0001f600'*i)

i = 1
while i < 11:
    print('\U0001f600'*i)
    i += 1

i = 1
while i < 11:
    print('\U0001f600'*i)
    i += 2

answer = input('Hey how is it going? ')
while answer != 'stop copying me':
    print(answer)
    answer = input()

print('UGH FINE YOU WIN')



while True:
    command = input('What would you like to do? ')
    if command == 'nothing':
        break

