import random


n = random.randrange(1, 20) # n receives random value in range from 1 to 20
guess_num = int(input('Enter any number in range from 1 to 20: '))
while guess_num != n:
    if guess_num < n:
        print('Too low')
        guess_num = int(input('Try one more time!) '))
    elif guess_num > n:
        print('Too high')
        guess_num = int(input('Try one more time!) '))
    else:
        break
print('You guessed')
