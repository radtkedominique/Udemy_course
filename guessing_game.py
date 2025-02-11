import random


while True:
    random_numb = random.randint(1, 100)
    #print(random_numb)
    print("Guess a number between 1 and 100: ")
    guess = int(input())

    while guess != random_numb:
        if guess > random_numb:
            print("Too high!")
            guess = int(input('Try again: '))

        elif guess < random_numb:
            print("Too low!")
            guess = int(input('Try again: '))

    print("You guessed right!")

    answer = input('Do you want to play again? (y/n): ')
    if answer.lower() == 'n':
        print('Thank you for playing!')
        break
