import random

num = random.randint(1,100)
val = 10

print('\n\nGuess a number between 1 and 100 \n')
while val>0:
    print("Chances left is {}".format(val))
    try:
        guess = int(input())
    except:
        print('Enter a valid integer')
        continue
    if guess == num:
        print('Congratulations')
        break
    elif guess>num:
        print('Try a lower number')
    elif guess<num:
        print('Try a greater number')
    val-=1

print('The correct guess should be {}'.format(num))