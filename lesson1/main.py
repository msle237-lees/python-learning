
# Test Install
print("Hello World")
print('Hello World')

# While Loops
i = 0
while i < 10:
    print(i)
    i += 1

import random





number = random.randint(1, 100)
attempts = 0


# Main loop
while True:
    try:
        guess = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    attempts += 1

    if guess == number:
        print(f"Congratulations! You got it in {attempts} attempts.")
        break
    elif guess < number:
        print("Try higher")
    else:
        print("Try lower")

