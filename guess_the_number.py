import random

rand = random.randrange(1,100)

guess=5

print("Start entering your number\n")
while guess!=0:
    user=int(input())
    guess=guess-1
    if user<rand:
        print("Number is less\n")
        print("Number of guesses left" , guess)
    elif user>rand:
        print("Number is greater")
        print("Number of guesses left" , guess)
    elif user==rand:
        print("You guessed the number is right")
        print("Number of guesses left" , guess)
        break
print("Game over")