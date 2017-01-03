import random

a = random.randint(1,9)

b = int(input("Enter your guess(Numbers between 1-9)"))

print("your guess was too high :/ Try again Next time" if b>a else "your guess was perfect" if  b==a else "Your guess was too low :/ Try again Next Time")


