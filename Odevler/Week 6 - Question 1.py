import time
import random
cpu = int(random.randint(0,100))

start = time.time()
while True:
    try:
        guess = int(input("Guess a number between 0 - 100:"))
        if guess < 0:
            raise ArithmeticError("A Positief Number!")

    except ValueError:
        print("Guess a number between 0 - 100:")
        continue
    
    if guess == cpu:
        print("Correct!")
        break
    elif guess > cpu:
        print("Higher then")
    elif guess < cpu:
        print("Lower then")

finish = time.time()
print("Guess time:",finish - start)