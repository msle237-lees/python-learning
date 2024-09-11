# python-learning

## About
This repository is to teach python to the members of AUV and get them ready to go as fast as possible.
They learn the fundamentals of programming within their course work so we skip a lot to focus on what we use in our software. 

# Lesson 1
Installing latest python version
Quick test of python install and showing that strings can be created with both '' and ""
```python
# Test Install
print("Hello World")
print('Hello World')
```

Example of loops in python
```python
# While loops
i = 0
while i < 10:
    print(i)
    i += 1

# For loops
for i in range(0, 10):
    print(i)
for i in range(10):
    print(i)
```

Random Number guesser
```python
import random

number = random.randint(1, 100)
attempts = 0

while True:
    try: 
        guess = int(input("Enter a number:"))
    except ValueError:
        print("Please enter a valid number")
        continue
    attempts += 1

    if guess == number:
        print(f'Congragulations! You got it in {attempts}.')
        break
    elif guess < number:
        print("Try Higher")
    else:
        print("Try Lower")
```

# Lesson 2
